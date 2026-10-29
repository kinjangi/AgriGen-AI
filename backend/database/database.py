from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config.settings import settings
from config.config import logger

logger.info("Initializing database engine...")
engine_args = {"pool_pre_ping": True, "echo": settings.DEBUG}
if settings.DATABASE_URL and settings.DATABASE_URL.startswith("sqlite"):
    engine_args["connect_args"] = {"check_same_thread": False}

engine = create_engine(
    settings.DATABASE_URL,
    **engine_args
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """
    Dependency function that yields database sessions for FastAPI endpoints.
    closes the session once the request is completed.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
