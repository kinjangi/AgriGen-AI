import os
import shutil

def generate_full_unabridged_text_document():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    out_txt_path = os.path.join(base_dir, "AgriGen_AI_Complete_Source_Code.txt")
    artifact_dir = r"C:\Users\tarun\.gemini\antigravity-ide\brain\1300543b-86e2-46e5-91ed-0af92e846694"

    code_files = [
        ("SECTION 01: APPLICATION ENTRYPOINT & LIFECYCLE", "backend/main.py", 
         "FastAPI App, CORS configuration, static upload directories, application lifespan"),
        
        ("SECTION 02: SYSTEM SETTINGS & ENVIRONMENT VALIDATION", "backend/config/settings.py", 
         "Pydantic BaseSettings, API Key security validation, environmental variable parsing"),
        
        ("SECTION 03: DATABASE ENGINE & SESSION FACTORY", "backend/database/database.py", 
         "SQLAlchemy engine setup, SessionLocal generator, declarative base mapping"),
        
        ("SECTION 04: RELATIONAL DATABASE ORM MODELS", "backend/database/models.py", 
         "User, Farm, DiagnosticRecord, CropSchedule, and TelemetryLog database schemas"),
        
        ("SECTION 05: REST API GATEWAY & STREAMING HUB", "backend/api/v1/orchestrator.py", 
         "FastAPI endpoints, Server-Sent Events (SSE) token generator, Whisper ASR, gTTS"),
        
        ("SECTION 06: FARM TELEMETRY & SYSTEM HEALTH", "backend/api/v1/telemetry.py", 
         "Sensor telemetry ingestion, environmental status metrics, API health monitoring"),
        
        ("SECTION 07: LANGGRAPH MULTI-AGENT SUPERVISOR DAG", "backend/core/agents/workflow.py", 
         "AgentState TypedDict, Supervisor Intent Router, Open-Meteo & Soil API data tools"),
        
        ("SECTION 08: DEEP VISION PATHOLOGY DIAGNOSTIC SERVICE", "backend/services/vision_service.py", 
         "PyTorch EfficientNet-B0 Paddy leaf disease classification ensemble & confidence scoring"),
        
        ("SECTION 09: SPATIAL GEOLOCATION & MANDI INDEXING", "backend/services/geo_service.py", 
         "Mathematical Haversine formula, 25+ Mandis database, SoilGrids classification"),
        
        ("SECTION 10: DEEP LEARNING MODEL TRAINING PIPELINE", "backend/ml/train_disease_classifier.py", 
         "PyTorch model training loop, AdamW optimizer, CrossEntropy loss, accuracy checkpoints"),
        
        ("SECTION 11: DATASET PIPELINE & AUGMENTATION", "backend/ml/dataset_pipeline.py", 
         "Torchvision image preprocessing, class balancing, random affine transforms"),
        
        ("SECTION 12: FRONTEND PRESENTATION & CLIENT DASHBOARD", "frontend/src/App.jsx", 
         "React 19 single-page application, HTML5 MediaRecorder voice capture, Chart.js graphs"),
        
        ("SECTION 13: RESPONSIVE STYLING & DESIGN SYSTEM", "frontend/src/App.css", 
         "Modern dark-theme design tokens, CSS variables, glassmorphism, responsive grid layout")
    ]

    header = """================================================================================
🌾 AGRIGEN AI — COMPLETE 100% UNABRIDGED SOURCE CODE IMPLEMENTATION
Intelligent Multi-Agent Smart Farming Ecosystem
================================================================================
Academic Project Review Documentation
Architecture: React 19 • FastAPI • LangGraph • PyTorch • FAISS RAG • Whisper Speech
Scope: Complete, unabridged source code for ALL 13 core modules (Zero Truncation)
Format: Plain-text code listing with continuous line numbers, ready for MS Word.
================================================================================

TABLE OF CONTENTS:
"""
    for idx, (sec_title, file_rel, desc) in enumerate(code_files, start=1):
        header += f"  {idx:02d}. {sec_title}\n      File: {file_rel}\n      Scope: {desc}\n\n"

    header += "================================================================================\n\n"

    total_code_lines = 0

    with open(out_txt_path, "w", encoding="utf-8") as out_f:
        out_f.write(header)

        for sec_title, file_rel, desc in code_files:
            file_path = os.path.join(base_dir, file_rel.replace('/', os.sep))

            if not os.path.exists(file_path):
                out_f.write(f"\n# [Notice: File {file_rel} not found in workspace]\n\n")
                continue

            with open(file_path, "r", encoding="utf-8", errors="replace") as in_f:
                lines = in_f.readlines()

            num_lines = len(lines)
            total_code_lines += num_lines

            section_hdr = f"""
################################################################################
# {sec_title}
# File Path: {file_rel}
# Total Lines in File: {num_lines} (Complete 100% Unabridged)
# Functional Scope: {desc}
################################################################################

"""
            out_f.write(section_hdr)

            # Write every single line without ANY truncation
            for l_num, line in enumerate(lines, start=1):
                out_f.write(f"{l_num:04d}:  {line}")

            if lines and not lines[-1].endswith("\n"):
                out_f.write("\n")

            out_f.write("\n\n")

    # Copy to artifacts directory
    os.makedirs(artifact_dir, exist_ok=True)
    artifact_dst = os.path.join(artifact_dir, "AgriGen_AI_Complete_Source_Code.txt")
    shutil.copy2(out_txt_path, artifact_dst)

    file_size_kb = os.path.getsize(out_txt_path) / 1024
    print(f"Generated 100% UNABRIDGED text document successfully at:\n  {out_txt_path}")
    print(f"  Total Lines of Code: {total_code_lines}")
    print(f"  File Size: {file_size_kb:.1f} KB")

if __name__ == '__main__':
    generate_full_unabridged_text_document()
