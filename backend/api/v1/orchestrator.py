import os
import uuid
import hashlib
import asyncio
from typing import List, Optional
from fastapi import APIRouter, Request, File, UploadFile, Form, HTTPException
from fastapi.responses import StreamingResponse, JSONResponse
from pydantic import BaseModel
from core.agents.workflow import app as langgraph_app
import pypdf
from gtts import gTTS

router = APIRouter()

MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10MB
MAX_PDF_SIZE = 20 * 1024 * 1024    # 20MB
MAX_VIDEO_SIZE = 50 * 1024 * 1024  # 50MB

class ChatRequest(BaseModel):
    query: str
    farm_id: Optional[str] = None
    language: Optional[str] = "en"
    lat: Optional[float] = 18.4491
    lon: Optional[float] = 83.6596
    crop: Optional[str] = "paddy"
    location_name: Optional[str] = "Razam, Andhra Pradesh"
    user_profile: Optional[dict] = None

class TTSRequest(BaseModel):
    text: str
    language: Optional[str] = "en"

async def async_generator(result: str):
    """Token-by-token fast streaming from the AI Orchestrator."""
    words = result.split(' ')
    for i in range(0, len(words), 2):
        chunk = " ".join(words[i:i+2])
        yield f"data: {chunk} \n\n"
        await asyncio.sleep(0.008)
    yield "data: [DONE]\n\n"

def process_uploaded_files(files: List[UploadFile]):
    """
    Validates file sizes, mime types, extracts PDF text, saves to static/uploads,
    and returns file metadata list + aggregated extracted text.
    """
    uploads_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "static", "uploads")
    os.makedirs(uploads_dir, exist_ok=True)

    saved_files = []
    extracted_text_chunks = []

    for file in files:
        if not file.filename:
            continue

        # Read content to check file size & MIME
        content = file.file.read()
        file_size = len(content)
        content_type = file.content_type or ""
        filename_lower = file.filename.lower()

        # Categorize File
        if content_type.startswith("image/") or filename_lower.endswith(('.jpg', '.jpeg', '.png', '.heic', '.webp')):
            category = "image"
            if file_size > MAX_IMAGE_SIZE:
                raise HTTPException(status_code=400, detail=f"Image {file.filename} exceeds max size limit of 10MB.")
        elif content_type == "application/pdf" or filename_lower.endswith(".pdf"):
            category = "pdf"
            if file_size > MAX_PDF_SIZE:
                raise HTTPException(status_code=400, detail=f"PDF {file.filename} exceeds max size limit of 20MB.")
        elif content_type.startswith("video/") or filename_lower.endswith(('.mp4', '.mov', '.webm', '.avi')):
            category = "video"
            if file_size > MAX_VIDEO_SIZE:
                raise HTTPException(status_code=400, detail=f"Video {file.filename} exceeds max size limit of 50MB.")
        else:
            raise HTTPException(status_code=400, detail=f"Unsupported file type for {file.filename}. Allowed: Images, PDFs, Videos.")

        # Save to static/uploads
        unique_name = f"{uuid.uuid4().hex[:8]}_{file.filename}"
        saved_path = os.path.join(uploads_dir, unique_name)
        with open(saved_path, "wb") as f:
            f.write(content)

        file_url = f"http://localhost:8000/static/uploads/{unique_name}"

        # PDF Text Extraction using pypdf
        pdf_text = ""
        if category == "pdf":
            try:
                reader = pypdf.PdfReader(saved_path)
                text_pages = [page.extract_text() for page in reader.pages if page.extract_text()]
                pdf_text = "\n".join(text_pages)
                if pdf_text:
                    extracted_text_chunks.append(f"[PDF Content from {file.filename}]:\n{pdf_text[:2000]}")
            except Exception as e:
                print(f"[PDF Extract Error] Failed to extract text from {file.filename}: {e}")

        saved_files.append({
            "name": file.filename,
            "path": saved_path,
            "url": file_url,
            "category": category,
            "size": file_size,
            "mime": content_type
        })

    extracted_context = "\n\n".join(extracted_text_chunks)
    return saved_files, extracted_context


@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    """
    Standard JSON Chat Endpoint.
    Invokes LangGraph agentic workflow with location, crop, user query, and behavioral profile.
    """
    initial_state = {
        "user_query": request.query,
        "language": request.language or "en",
        "location": {
            "lat": request.lat or 18.4491,
            "lon": request.lon or 83.6596,
            "location_name": request.location_name or "Razam, Andhra Pradesh"
        },
        "crop": request.crop or "paddy",
        "user_profile": request.user_profile or {},
        "weather_data": {},
        "soil_data": {},
        "soil_type_data": {},
        "crop_calendar_data": {},
        "market_data": {},
        "forecast_data": {},
        "image_data": {},
        "file_context": "",
        "files": [],
        "intent": "general_chat",
        "final_answer": "",
        "messages": []
    }
    
    state_after_run = langgraph_app.invoke(initial_state)
    final_text = state_after_run.get("final_answer") or (state_after_run.get("messages", [])[-1].content if state_after_run.get("messages") else "Service unavailable.")
    return StreamingResponse(async_generator(final_text), media_type="text/event-stream")


@router.post("/chat_with_files")
async def chat_with_files_endpoint(
    query: str = Form(...),
    language: str = Form("en"),
    lat: float = Form(18.4491),
    lon: float = Form(83.6596),
    crop: str = Form("paddy"),
    location_name: str = Form("Razam, Andhra Pradesh"),
    user_profile: Optional[str] = Form(None),
    files: List[UploadFile] = File(None)
):
    """
    Multipart File Upload Endpoint (Images, PDFs, Videos).
    Processes files, extracts text, and invokes LangGraph agentic workflow.
    """
    saved_files, extracted_context = process_uploaded_files(files or [])

    parsed_profile = {}
    if user_profile:
        try:
            parsed_profile = json.loads(user_profile)
        except Exception:
            pass

    initial_state = {
        "user_query": query,
        "language": language or "en",
        "location": {
            "lat": lat,
            "lon": lon,
            "location_name": location_name
        },
        "crop": crop,
        "user_profile": parsed_profile,
        "weather_data": {},
        "soil_data": {},
        "soil_type_data": {},
        "crop_calendar_data": {},
        "market_data": {},
        "forecast_data": {},
        "image_data": {},
        "file_context": extracted_context,
        "files": saved_files,
        "intent": "general_chat",
        "final_answer": "",
        "messages": []
    }

    state_after_run = langgraph_app.invoke(initial_state)
    final_text = state_after_run.get("final_answer") or (state_after_run.get("messages", [])[-1].content if state_after_run.get("messages") else "Service unavailable.")

    return StreamingResponse(async_generator(final_text), media_type="text/event-stream")


@router.post("/tts")
async def text_to_speech_endpoint(request: TTSRequest):
    """
    Converts AI response text into natural audio using gTTS (Telugu 'te' or English 'en')
    and returns a cached static MP3 URL.
    """
    clean_text = request.text.replace("*", "").replace("#", "").replace("🌾", "").replace("•", "").strip()
    if not clean_text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    lang_code = "te" if request.language == "te" else "en"
    text_hash = hashlib.md5(f"{clean_text}_{lang_code}".encode('utf-8')).hexdigest()
    
    audio_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "static", "audio_cache")
    os.makedirs(audio_dir, exist_ok=True)
    
    audio_filename = f"{text_hash}.mp3"
    file_path = os.path.join(audio_dir, audio_filename)
    audio_url = f"http://localhost:8000/static/audio_cache/{audio_filename}"

    # Generate MP3 if not already cached
    if not os.path.exists(file_path):
        try:
            tts = gTTS(text=clean_text[:400], lang=lang_code, slow=False)
            tts.save(file_path)
        except Exception as e:
            print(f"[gTTS Error]: {e}")
            raise HTTPException(status_code=500, detail="Failed to synthesize speech audio.")

    return JSONResponse(content={"audio_url": audio_url})
