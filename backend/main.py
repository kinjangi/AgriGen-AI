import sys
import os

# Add current directory (backend/) to sys.path for self-contained module resolution
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.settings import settings
from config.config import logger
from api.v1 import auth, orchestrator, telemetry

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup Events
    logger.info(f"Starting up {settings.PROJECT_NAME} Backend Server...")
    from database.database import engine, Base
    import database.models  # load models
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown Events
    logger.info(f"Shutting down {settings.PROJECT_NAME} Backend Server...")

def get_application() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        openapi_url=f"{settings.API_PREFIX}/openapi.json",
        description="AgriGen AI Multi-Agent Smart Farming Assistant API",
        lifespan=lifespan
    )

    # Set all CORS enabled origins
    if settings.BACKEND_CORS_ORIGINS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    
    # Ensure uploads & audio_cache directories exist and mount static files
    uploads_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "uploads")
    audio_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "audio_cache")
    os.makedirs(uploads_dir, exist_ok=True)
    os.makedirs(audio_dir, exist_ok=True)
    from fastapi.staticfiles import StaticFiles
    app.mount("/static/uploads", StaticFiles(directory=uploads_dir), name="uploads")
    app.mount("/static/audio_cache", StaticFiles(directory=audio_dir), name="audio_cache")

    # Register API Routers
    app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
    app.include_router(orchestrator.router, prefix="/api/v1/orchestrator", tags=["Multi-Agent Orchestration"])
    app.include_router(telemetry.router, prefix="/api/v1/telemetry", tags=["Farm Telemetry"])
    
    return app

app = get_application()

@app.get("/api/v1/health", tags=["Health"])
def health_check():
    """Base healthcheck for Docker and load balancers."""
    logger.debug("Health check endpoint hit.")
    return {"status": "active", "project": settings.PROJECT_NAME, "version": settings.VERSION}
