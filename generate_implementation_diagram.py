import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def generate_implementation_diagram():
    fig, ax = plt.subplots(figsize=(13, 8.5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    plt.title("Figure 7.1: AgriGen AI Detailed Modular Implementation & Inter-Service Dataflow",
              fontsize=14, color='#0f172a', weight='bold', pad=20)

    modules = [
        {
            "name": "Module 1: Client UI & Audio Ingestion",
            "file": "frontend/src/App.jsx",
            "x": 0.04, "y": 0.68, "w": 0.42, "h": 0.22,
            "bg": "#eff6ff", "border": "#2563eb", "title_col": "#1e40af",
            "lines": [
                "• MediaRecorder API for 16 kHz audio capture",
                "• File API for leaf photo canvas compression",
                "• EventSource client for SSE token stream",
                "• Chart.js rendering for weather & market curves"
            ]
        },
        {
            "name": "Module 2: Gateway & Streaming Hub",
            "file": "backend/api/v1/orchestrator.py",
            "x": 0.54, "y": 0.68, "w": 0.42, "h": 0.22,
            "bg": "#f0fdf4", "border": "#16a34a", "title_col": "#166534",
            "lines": [
                "• FastAPI asynchronous route handlers",
                "• Pydantic schema validation & token chunking",
                "• OpenAI Whisper Speech-to-Text integration",
                "• gTTS multilingual voice synthesis engine"
            ]
        },
        {
            "name": "Module 3: LangGraph Agent DAG",
            "file": "backend/core/agents/workflow.py",
            "x": 0.04, "y": 0.38, "w": 0.42, "h": 0.24,
            "bg": "#faf5ff", "border": "#9333ea", "title_col": "#6b21a8",
            "lines": [
                "• TypedDict AgentState immutable dictionary",
                "• Meta-prompt Supervisor intent routing",
                "• Live Open-Meteo & SoilGrids telemetry fetch",
                "• Composite multi-turn response compiler"
            ]
        },
        {
            "name": "Module 4: Deep Vision Pathology",
            "file": "backend/services/vision_service.py",
            "x": 0.54, "y": 0.38, "w": 0.42, "h": 0.24,
            "bg": "#fef2f2", "border": "#dc2626", "title_col": "#991b1b",
            "lines": [
                "• PaddyDiseaseEnsembleService 2-stage pipeline",
                "• PyTorch EfficientNet-B0 fine-tuned weights",
                "• Multi-class blight, blast & spot classification",
                "• Lesion confidence score & severity calculation"
            ]
        },
        {
            "name": "Module 5: Spatial Geolocation & Mandis",
            "file": "backend/services/geo_service.py",
            "x": 0.04, "y": 0.06, "w": 0.42, "h": 0.24,
            "bg": "#fff7ed", "border": "#ea580c", "title_col": "#9a3412",
            "lines": [
                "• Haversine spherical distance calculation (km)",
                "• 25+ major national and regional mandi database",
                "• Reverse geocoding for district & mandal naming",
                "• Commodity modal price lookup & margin estimation"
            ]
        },
        {
            "name": "Module 6: Dense Vector RAG Pipeline",
            "file": "backend/core/ai/rag.py",
            "x": 0.54, "y": 0.06, "w": 0.42, "h": 0.24,
            "bg": "#fdf4ff", "border": "#c026d3", "title_col": "#86198f",
            "lines": [
                "• FAISS IndexFlatIP dense vector similarity",
                "• sentence-transformers/all-MiniLM-L6-v2 embeddings",
                "• Indexed ICAR & university agronomy publications",
                "• Zero-hallucination context injection into LLM"
            ]
        }
    ]

    for m in modules:
        rect = mpatches.FancyBboxPatch((m["x"], m["y"]), m["w"], m["h"],
                                      boxstyle="round,pad=0.015",
                                      facecolor=m["bg"], edgecolor=m["border"], linewidth=1.6)
        ax.add_patch(rect)
        ax.text(m["x"] + 0.015, m["y"] + m["h"] - 0.035, m["name"],
                ha='left', va='center', color=m["title_col"], fontsize=9.5, weight='bold')
        ax.text(m["x"] + 0.015, m["y"] + m["h"] - 0.07, f"File: {m['file']}",
                ha='left', va='center', color='#64748b', fontsize=7.8, style='italic')

        for idx, line in enumerate(m["lines"]):
            ax.text(m["x"] + 0.015, m["y"] + m["h"] - 0.115 - (idx * 0.033), line,
                    ha='left', va='center', color='#1e293b', fontsize=8.0)

    # Cross connections
    ax.annotate("", xy=(0.54, 0.79), xytext=(0.46, 0.79),
                arrowprops=dict(facecolor='#0284c7', edgecolor='#0284c7', arrowstyle="<->", lw=2))
    ax.annotate("", xy=(0.25, 0.62), xytext=(0.25, 0.68),
                arrowprops=dict(facecolor='#0284c7', edgecolor='#0284c7', arrowstyle="->", lw=2))
    ax.annotate("", xy=(0.75, 0.62), xytext=(0.75, 0.68),
                arrowprops=dict(facecolor='#0284c7', edgecolor='#0284c7', arrowstyle="->", lw=2))
    ax.annotate("", xy=(0.25, 0.30), xytext=(0.25, 0.38),
                arrowprops=dict(facecolor='#0284c7', edgecolor='#0284c7', arrowstyle="->", lw=2))
    ax.annotate("", xy=(0.75, 0.30), xytext=(0.75, 0.38),
                arrowprops=dict(facecolor='#0284c7', edgecolor='#0284c7', arrowstyle="->", lw=2))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 0.96)
    plt.axis('off')
    plt.tight_layout()

    out_file = os.path.join(os.getcwd(), "figure_7_1_implementation_module_interaction.png")
    plt.savefig(out_file, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Generated {out_file}")

if __name__ == '__main__':
    generate_implementation_diagram()
