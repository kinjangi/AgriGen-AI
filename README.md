# AgriGen AI - Intelligent Agriculture Platform

![AgriGen AI](https://via.placeholder.com/800x200.png?text=AgriGen+AI+-+Smart+Farming+Ecosystem)

AgriGen AI is a state-of-the-art, multi-agent AI farming ecosystem. It leverages cutting-edge deep learning, LLMs, and computer vision technologies to empower farmers with actionable insights, market predictions, weather forecasting, disease detection, and multilingual voice-assisted advisory.

---

## 📑 Table of Contents
1. [Architecture Overview](#architecture-overview)
2. [Folder Structure](#folder-structure)
3. [Installation Guide](#installation-guide)
4. [Deployment Guide](#deployment-guide)
5. [API Documentation](#api-documentation)
6. [User Manual](#user-manual)
7. [Developer Guide](#developer-guide)
8. [Future Scope](#future-scope)

---

## 🏗️ Architecture Overview

AgriGen AI utilizes a microservices-inspired architecture orchestrated by Docker and driven by a LangGraph AI Supervisor.

**Core Components:**
- **Frontend Dashboard (React/Vite)**: A responsive UI featuring dynamic Chart.js graphing for market/weather trends, and a Chatbot interface supporting Voice & Image inputs.
- **Backend (FastAPI)**: The central hub handling REST APIs, streaming AI responses, and business logic.
- **AI Supervisor (LangGraph)**: The intelligent core powered by LLMs (Llama 3). It routes user queries to specialist agents:
  - *Weather Agent*: Powered by custom PyTorch LSTMs and OpenWeatherAPI.
  - *Market Agent*: LSTM-driven crop price forecasting and profitability estimators.
  - *Disease Agent*: YOLO/Vision integration for leaf-disease tracing.
  - *RAG Knowledge Agent*: LangChain and FAISS vector database retrieving insights from official agriculture research papers.
  - *Voice Agent*: OpenAI Whisper STT and Text-To-Speech for multilingual (English, Hindi, Telugu) accessibility.
- **Infrastructure:**
  - **PostgreSQL**: Relational storage for user profiles and historical metrics.
  - **Redis**: Caching and AI state-machine memory.
  - **NGINX**: Reverse proxy and load balancing.

---

## 📂 Folder Structure

```text
agriGen_AI/
├── backend/               # Self-contained FastAPI application
│   ├── api/               # API endpoints (v1 routes for auth, orchestrator, etc.)
│   ├── config/            # Settings, logger, and environment config
│   ├── core/              # ML modules, LangGraph Agents, RAG & Security
│   │   ├── agents/        # LangGraph Multi-Agent Supervisor & workflows
│   │   ├── ai/            # RAG System & FAISS indexing
│   │   └── ml_models/     # PyTorch LSTMs for Market & Weather prediction
│   ├── database/          # SQLAlchemy database connection and models
│   ├── schemas/           # Pydantic schemas for request/response validation
│   ├── services/          # Business logic & services
│   ├── main.py            # FastAPI entry point
│   └── agrigen.db         # Local SQLite database
├── frontend/              # React dashboard (Vite + Vanilla CSS)
├── venv313/               # Python virtual environment
├── docker-compose.yml     # Multi-container orchestration 
├── Dockerfile             # Backend container image build definition
├── run_local.ps1          # Powershell convenience script for local launch
└── requirements.txt       # Python dependencies
```

---

## 💻 Installation Guide

### Prerequisites
- Docker & Docker Compose
- Node.js (for frontend local dev)
- Python 3.10+
- An OpenWeather API Key & an LLM provider Key (e.g., Groq / local Ollama)

### Local Setup
1. **Clone the repo**
   ```bash
   git clone https://github.com/organization/agriGen_AI.git
   cd agriGen_AI
   ```
2. **Environment Variables**
   Copy `.env.example` to `.env` and add real provider values only:
   ```env
   OPENAI_API_KEY=your_openai_key
   GEMINI_API_KEY=your_gemini_key
   GROQ_API_KEY=your_groq_key
   OPEN_METEO_API_KEY=your_open_meteo_key
   DATABASE_URL=sqlite:///./agrigen.db
   ```
3. **Run with Docker**
   ```bash
   docker-compose up -d --build
   ```
   *The backend is available at `http://localhost:8000` and the frontend at `http://localhost:80`.*

---

## 🚀 Deployment Guide

For a production environment, AgriGen AI is orchestrated via NGINX and Docker.

1. **Provision a Server**: Recommend AWS EC2 or DigitalOcean Droplet (min 4GB RAM).
2. **SSL Configuration**:
   Use Certbot to secure the NGINX proxy:
   ```bash
   sudo apt install certbot python3-certbot-nginx
   sudo certbot --nginx -d yourdomain.com
   ```
3. **Database Migration**:
   On the first run, initialize Postgres:
   ```bash
   docker-compose exec backend alembic upgrade head
   ```
4. **Scale Workers**: To handle intensive PyTorch CPU loads smoothly, spin up extra backend instances in your `docker-compose.yml`.

---

## 🔌 API Documentation

Detailed swagger documentation is automatically generated and accessible at `http://localhost/docs`.

### Key Endpoints
- **GET** `/api/v1/weather/forecast/{farm_id}`
  *Returns a localized 7-day weather prediction via LSTM optimization.*
- **POST** `/api/v1/market/predict`
  *Accepts current Supply/Demand and returns Future Crop Price and Best Selling Date.*
- **POST** `/api/v1/orchestrator/chat`
  *Streaming SSE endpoint connecting to the LangGraph AI loop. Accepts text, images, and voice.*
- **POST** `/api/v1/report/generate/{farm_id}`
  *Triggers WeasyPrint to aggregate data and return a professional PDF report.*

---

## 📖 User Manual

1. **Dashboard Overview**: Upon logging in, farmers are greeted with a personalized interface outlining the realtime status of their crops, local soil moisture, and weather alerts.
2. **Asking the AI**: Use the Chat window to type, or the Microphone button to speak in English, Hindi, or Telugu. Ask complex questions like: *"The tomato prices are dropping, what should I do?"*
3. **Disease Scanning**: Click the **Upload Leaf** button in the chat. The system will identify the disease, cross-reference government treatment schemes using RAG, and instantly output a confidence-scored remedy.
4. **PDF Reports**: Navigate to the "Reports" tab and click "Generate Weekly Summary" to instantly download a professionally formatted PDF encompassing all charts and predictions.

---

## 🛠️ Developer Guide

### Adding a new AI Agent to LangGraph
1. **Create the Specialist**: Navigate to `core/agents/` and create your logical node (e.g., `pest_agent.py`).
2. **Formulate Guidelines**: Ensure the node accepts the standard `AgentState` typed dict.
3. **Hook into Workflow**: In `core/agents/workflow.py`, add your new agent to the Directed Acyclic Graph (DAG) state machine. Add an edge from the `Supervisor` node so the LLM knows when to invoke your service.

### Formatting the UI
Frontend components are utilizing Vanilla CSS for tailored styling. Avoid generic Tailwind defaults. When modifying the Dashboard, refer to `frontend/src/styles/variables.css` for the dark-mode compatible primary palette.

---

## 🔮 Future Scope

- **Edge Deployment**: Shrink wrapping the disease models to run inference directly on iOS/Android devices without network reliance.
- **Drone Integration**: Ingesting Orthomosaic imagery for wide-scale automated farm surveying.
- **Automated IoT Control**: Linking the Irrigation Agent directly to farm smart-valves to autonomously water crops based on Weather LSTM forecasts.
- **Commodity Trading Link**: Implementing live execution trading hooks to automatically sell crops at the LSTM's perceived peak profitability date.
