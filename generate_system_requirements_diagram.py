import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def generate_requirements_diagram():
    fig, ax = plt.subplots(figsize=(13, 8.5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    plt.title("Figure 4.1: AgriGen AI Multi-Tier Hardware and Software Requirements Architecture",
              fontsize=14, color='#0f172a', weight='bold', pad=20)

    layers = [
        {
            "tier": "TIER 1: CLIENT HARDWARE & INTERFACE REQUIREMENTS",
            "bg": "#f8fafc", "border": "#64748b", "y": 0.81, "h": 0.14,
            "items": [
                ("Farmer End Device", "Any Android / iOS Smartphone or PC\nMin 2 GB RAM, Quad-Core CPU", "#e2e8f0"),
                ("Peripheral Sensors", "Camera Sensor (≥ 5 MP resolution)\nIntegrated Microphone / Headset", "#e2e8f0"),
                ("Network Connectivity", "3G / 4G / 5G / Broadband (≥ 512 Kbps)\nGPS Geolocation Module", "#e2e8f0")
            ]
        },
        {
            "tier": "TIER 2: FRONTEND PRESENTATION RUNTIME",
            "bg": "#eff6ff", "border": "#3b82f6", "y": 0.62, "h": 0.15,
            "items": [
                ("Core Framework", "React.js v19 (Component-driven UI)\nVite v8 (High-speed build tool)", "#dbeafe"),
                ("Visualization & Audio", "Chart.js (Interactive time-series)\nHTML5 MediaRecorder & Audio API", "#dbeafe"),
                ("Protocols & Formats", "Server-Sent Events (SSE) streaming\nRESTful JSON & Multipart Form-Data", "#dbeafe")
            ]
        },
        {
            "tier": "TIER 3: BACKEND API & COMPUTATION SERVER",
            "bg": "#f0fdf4", "border": "#22c55e", "y": 0.43, "h": 0.15,
            "items": [
                ("Web Framework", "FastAPI (Asynchronous Python 3.10+)\nUvicorn (High-performance ASGI server)", "#dcfce7"),
                ("Data Validation", "Pydantic v2 (Strict Schema Validation)\nSQLAlchemy ORM + Alembic migrations", "#dcfce7"),
                ("Reporting Engine", "WeasyPrint (Automated PDF generation)\nJWT & Passlib (Secure authentication)", "#dcfce7")
            ]
        },
        {
            "tier": "TIER 4: MACHINE LEARNING & AGENTIC AI CORE",
            "bg": "#faf5ff", "border": "#a855f7", "y": 0.24, "h": 0.15,
            "items": [
                ("Multi-Agent Supervisor", "LangGraph (State Machine DAG)\nLangChain (Prompt & Context piping)", "#f3e8ff"),
                ("Time-Series & Vision", "PyTorch (LSTM Weather & Market Models)\nTorchvision (Leaf Pathology CNN)", "#f3e8ff"),
                ("Retrieval & Speech", "FAISS-CPU (Dense Vector DB RAG)\nOpenAI Whisper (Multilingual STT) + gTTS", "#f3e8ff")
            ]
        },
        {
            "tier": "TIER 5: PERSISTENCE, CACHING & DEVOPS INFRASTRUCTURE",
            "bg": "#fff1f2", "border": "#f43f5e", "y": 0.05, "h": 0.15,
            "items": [
                ("Relational Database", "PostgreSQL 15 (Alpine) / SQLite 3\nACID-compliant storage for users/metrics", "#ffe4e6"),
                ("In-Memory State Cache", "Redis 7 (Alpine)\nSession memory & high-speed token caching", "#ffe4e6"),
                ("DevOps & Orchestration", "Docker & Docker Compose v3.8\nMulti-container microservices architecture", "#ffe4e6")
            ]
        }
    ]

    for layer in layers:
        # Layer container
        rect = mpatches.FancyBboxPatch((0.03, layer["y"]), 0.94, layer["h"],
                                      boxstyle="round,pad=0.01",
                                      facecolor=layer["bg"], edgecolor=layer["border"], linewidth=1.5)
        ax.add_patch(rect)
        ax.text(0.05, layer["y"] + layer["h"] - 0.03, layer["tier"],
                ha='left', va='center', color=layer["border"], fontsize=9.5, weight='bold')

        # Inner cards
        x_positions = [0.05, 0.36, 0.67]
        for idx, (title, desc, card_bg) in enumerate(layer["items"]):
            card = mpatches.FancyBboxPatch((x_positions[idx], layer["y"] + 0.015), 0.29, layer["h"] - 0.05,
                                          boxstyle="round,pad=0.01",
                                          facecolor=card_bg, edgecolor=layer["border"], linewidth=0.8)
            ax.add_patch(card)
            ax.text(x_positions[idx] + 0.145, layer["y"] + layer["h"] - 0.045, title,
                    ha='center', va='center', color='#0f172a', fontsize=8.5, weight='bold')
            ax.text(x_positions[idx] + 0.145, layer["y"] + 0.04, desc,
                    ha='center', va='center', color='#334155', fontsize=7.5, linespacing=1.25)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.axis('off')
    plt.tight_layout()

    out_file = os.path.join(os.getcwd(), "figure_4_1_tech_stack_requirements.png")
    plt.savefig(out_file, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Generated {out_file} successfully.")

if __name__ == '__main__':
    generate_requirements_diagram()
