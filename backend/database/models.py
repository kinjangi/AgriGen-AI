import uuid
from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime, Boolean, Enum, Uuid as UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from database.database import Base

class RoleEnum(str, enum.Enum):
    FARMER = "Farmer"
    ADMIN = "Admin"
    AGRICULTURE_EXPERT = "Agriculture Expert"

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255))
    role = Column(Enum(RoleEnum), default=RoleEnum.FARMER)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    farms = relationship("Farm", back_populates="owner")
    chat_history = relationship("ChatHistory", back_populates="user")
    reports = relationship("Report", back_populates="user")

class Farm(Base):
    __tablename__ = "farms"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    name = Column(String(255), nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    total_area = Column(Float)
    climate_zone = Column(String(100))

    owner = relationship("User", back_populates="farms")
    crop_images = relationship("CropImage", back_populates="farm")
    soil_reports = relationship("SoilReport", back_populates="farm")
    weather_logs = relationship("WeatherLog", back_populates="farm")
    recommendations = relationship("Recommendation", back_populates="farm")

class CropImage(Base):
    __tablename__ = "crop_images"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    farm_id = Column(UUID(as_uuid=True), ForeignKey("farms.id"))
    image_path = Column(String, nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    farm = relationship("Farm", back_populates="crop_images")
    disease_report = relationship("DiseaseReport", back_populates="crop_image", uselist=False)

class DiseaseReport(Base):
    __tablename__ = "disease_reports"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    image_id = Column(UUID(as_uuid=True), ForeignKey("crop_images.id"), unique=True)
    disease_name = Column(String(255))
    confidence_score = Column(Float)
    severity_level = Column(String(100))
    organic_treatment = Column(String)
    chemical_treatment = Column(String)

    crop_image = relationship("CropImage", back_populates="disease_report")

class SoilReport(Base):
    __tablename__ = "soil_reports"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    farm_id = Column(UUID(as_uuid=True), ForeignKey("farms.id"))
    nitrogen = Column(Float)
    phosphorus = Column(Float)
    potassium = Column(Float)
    ph_level = Column(Float)
    organic_carbon = Column(Float)
    moisture = Column(Float)
    recorded_at = Column(DateTime, default=datetime.utcnow)

    farm = relationship("Farm", back_populates="soil_reports")

class WeatherLog(Base):
    __tablename__ = "weather_logs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    farm_id = Column(UUID(as_uuid=True), ForeignKey("farms.id"))
    temperature = Column(Float)
    humidity = Column(Float)
    precipitation = Column(Float)
    wind_speed = Column(Float)
    logged_at = Column(DateTime, default=datetime.utcnow)

    farm = relationship("Farm", back_populates="weather_logs")

class Recommendation(Base):
    __tablename__ = "recommendations"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    farm_id = Column(UUID(as_uuid=True), ForeignKey("farms.id"))
    recommendation_type = Column(String(100)) # e.g. Fertilizer, Crop
    ai_content = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    farm = relationship("Farm", back_populates="recommendations")

class MarketPrice(Base):
    __tablename__ = "market_prices"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    crop_name = Column(String(255), index=True)
    price_per_ton = Column(Float)
    currency = Column(String(10))
    trend = Column(String(50))
    demand_volume = Column(Float)
    supply_volume = Column(Float)
    date_recorded = Column(DateTime, default=datetime.utcnow)

class ChatHistory(Base):
    __tablename__ = "chat_history"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    query = Column(String)
    ai_response = Column(String)
    agent_type = Column(String(100))
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="chat_history")

class Report(Base):
    __tablename__ = "reports"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    report_type = Column(String(100))
    pdf_url = Column(String)
    generation_date = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="reports")

class WeatherForecast(Base):
    __tablename__ = "weather_forecasts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    farm_id = Column(UUID(as_uuid=True), ForeignKey("farms.id"))
    temperature = Column(Float)
    humidity = Column(Float)
    precipitation = Column(Float)
    wind_speed = Column(Float)
    forecast_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)

class MarketPrediction(Base):
    __tablename__ = "market_predictions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    crop_name = Column(String(255), index=True)
    predicted_price_per_ton = Column(Float)
    best_selling_date = Column(DateTime)
    profit_estimate = Column(Float)
    prediction_date = Column(DateTime, default=datetime.utcnow)
