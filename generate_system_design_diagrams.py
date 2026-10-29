import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def generate_system_architecture():
    fig, ax = plt.subplots(figsize=(13, 8.5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    plt.title("Figure 6.1: AgriGen AI Detailed Multi-Tier System Architecture",
              fontsize=14, color='#0f172a', weight='bold', pad=20)

    # Tier 1: Client Layer
    box_client = mpatches.FancyBboxPatch((0.05, 0.72), 0.90, 0.18, boxstyle="round,pad=0.015",
                                         facecolor='#eff6ff', edgecolor='#2563eb', linewidth=1.8)
    ax.add_patch(box_client)
    ax.text(0.50, 0.86, "TIER 1: PRESENTATION & CLIENT INTERFACE (React 19 + Vite)",
            ha='center', va='center', color='#1e40af', fontsize=11, weight='bold')
    
    client_sub = [
        ("Voice Capture UI", "HTML5 MediaRecorder\n16 kHz PCM Streaming", 0.18),
        ("Leaf Scanner UI", "Optical Camera Upload\nCanvas Compression", 0.50),
        ("Interactive Dashboard", "Chart.js Forecasts\nSSE Live Stream View", 0.82)
    ]
    for title, desc, cx in client_sub:
        cbox = mpatches.FancyBboxPatch((cx - 0.13, 0.74), 0.26, 0.09, boxstyle="round,pad=0.01",
                                       facecolor='#ffffff', edgecolor='#3b82f6', linewidth=1)
        ax.add_patch(cbox)
        ax.text(cx, 0.80, title, ha='center', va='center', color='#1e3a8a', fontsize=9, weight='bold')
        ax.text(cx, 0.76, desc, ha='center', va='center', color='#475569', fontsize=7.5)

    # Tier 2: Backend API & Gateway
    box_backend = mpatches.FancyBboxPatch((0.05, 0.44), 0.90, 0.20, boxstyle="round,pad=0.015",
                                          facecolor='#f0fdf4', edgecolor='#16a34a', linewidth=1.8)
    ax.add_patch(box_backend)
    ax.text(0.50, 0.60, "TIER 2: API GATEWAY & ORCHESTRATION HUB (FastAPI + Uvicorn)",
            ha='center', va='center', color='#166534', fontsize=11, weight='bold')
    
    backend_sub = [
        ("Whisper ASR Engine", "Speech-to-Text Conversion\n(Hindi, Telugu, English)", 0.18),
        ("LangGraph Supervisor", "DAG State Machine\nDynamic Intent Router", 0.50),
        ("Report & SSE Hub", "WeasyPrint PDF Engine\nSSE Streaming Server", 0.82)
    ]
    for title, desc, bx in backend_sub:
        bbox = mpatches.FancyBboxPatch((bx - 0.13, 0.46), 0.26, 0.10, boxstyle="round,pad=0.01",
                                       facecolor='#ffffff', edgecolor='#22c55e', linewidth=1)
        ax.add_patch(bbox)
        ax.text(bx, 0.525, title, ha='center', va='center', color='#14532d', fontsize=9, weight='bold')
        ax.text(bx, 0.485, desc, ha='center', va='center', color='#475569', fontsize=7.5)

    # Tier 3: Autonomous Specialist AI Agents
    box_agents = mpatches.FancyBboxPatch((0.05, 0.20), 0.90, 0.18, boxstyle="round,pad=0.015",
                                         facecolor='#faf5ff', edgecolor='#9333ea', linewidth=1.8)
    ax.add_patch(box_agents)
    ax.text(0.50, 0.34, "TIER 3: AUTONOMOUS SPECIALIST AI AGENTS (PyTorch & Vector RAG)",
            ha='center', va='center', color='#6b21a8', fontsize=11, weight='bold')

    agent_sub = [
        ("Weather Agent", "PyTorch LSTM\nMicro-climate Forecast", 0.15),
        ("Market Agent", "LSTM Price Model\nMandi Trend Predictor", 0.38),
        ("Disease Vision Agent", "Deep Residual CNN\nPathology Diagnostics", 0.62),
        ("Knowledge Agent", "FAISS Vector DB\nRAG Agronomy Corpus", 0.85)
    ]
    for title, desc, ax_pos in agent_sub:
        abox = mpatches.FancyBboxPatch((ax_pos - 0.10, 0.22), 0.20, 0.09, boxstyle="round,pad=0.01",
                                       facecolor='#ffffff', edgecolor='#a855f7', linewidth=1)
        ax.add_patch(abox)
        ax.text(ax_pos, 0.28, title, ha='center', va='center', color='#581c87', fontsize=8.5, weight='bold')
        ax.text(ax_pos, 0.24, desc, ha='center', va='center', color='#475569', fontsize=7.2)

    # Tier 4: Data & Persistence Infrastructure
    box_data = mpatches.FancyBboxPatch((0.05, 0.03), 0.90, 0.12, boxstyle="round,pad=0.015",
                                       facecolor='#fff1f2', edgecolor='#f43f5e', linewidth=1.8)
    ax.add_patch(box_data)
    ax.text(0.50, 0.115, "TIER 4: PERSISTENCE, CACHING & DEVOPS INFRASTRUCTURE",
            ha='center', va='center', color='#9f1239', fontsize=10.5, weight='bold')
    
    data_sub = [
        ("PostgreSQL 15 / SQLite", "Relational User & Audit Storage", 0.25),
        ("Redis 7 Cache", "Session Memory & Telemetry Cache", 0.50),
        ("Docker Container Hub", "Microservice Sandboxing", 0.75)
    ]
    for title, desc, dx in data_sub:
        dbox = mpatches.FancyBboxPatch((dx - 0.11, 0.045), 0.22, 0.055, boxstyle="round,pad=0.01",
                                       facecolor='#ffffff', edgecolor='#fb7185', linewidth=0.8)
        ax.add_patch(dbox)
        ax.text(dx, 0.08, title, ha='center', va='center', color='#881337', fontsize=8, weight='bold')
        ax.text(dx, 0.06, desc, ha='center', va='center', color='#475569', fontsize=7)

    # Connecting Arrows
    arrows = [
        ((0.50, 0.72), (0.50, 0.64)),
        ((0.50, 0.44), (0.50, 0.38)),
        ((0.50, 0.20), (0.50, 0.15))
    ]
    for start, end in arrows:
        ax.annotate("", xy=end, xytext=start,
                    arrowprops=dict(facecolor='#0284c7', edgecolor='#0284c7', arrowstyle="<->", lw=2.5))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 0.95)
    plt.axis('off')
    plt.tight_layout()

    out_file = os.path.join(os.getcwd(), "figure_6_1_system_architecture_detailed.png")
    plt.savefig(out_file, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Generated {out_file}")

def generate_use_case_diagram():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    plt.title("Figure 6.2: UML Use Case Diagram for AgriGen AI Platform",
              fontsize=14, color='#0f172a', weight='bold', pad=20)

    # System Boundary Box
    sys_box = mpatches.FancyBboxPatch((0.26, 0.04), 0.68, 0.88, boxstyle="round,pad=0.02",
                                      facecolor='#f8fafc', edgecolor='#0284c7', linewidth=2)
    ax.add_patch(sys_box)
    ax.text(0.60, 0.88, "AgriGen AI System Boundary", ha='center', va='center',
            color='#0369a1', fontsize=11, weight='bold')

    # Primary Actor: Farmer / User
    ax.plot([0.10, 0.10], [0.60, 0.48], color='#0f172a', lw=2.5) # body
    circle = plt.Circle((0.10, 0.65), 0.04, color='#0f172a', ec='#0f172a', lw=2) # head
    ax.add_patch(circle)
    ax.plot([0.05, 0.15], [0.55, 0.55], color='#0f172a', lw=2.5) # arms
    ax.plot([0.10, 0.06], [0.48, 0.38], color='#0f172a', lw=2.5) # left leg
    ax.plot([0.10, 0.14], [0.48, 0.38], color='#0f172a', lw=2.5) # right leg
    ax.text(0.10, 0.32, "Farmer / User\n(Client Actor)", ha='center', va='top',
            color='#0f172a', fontsize=9.5, weight='bold')

    # Use Cases (Ellipses)
    use_cases = [
        ("UC-1: Record & Submit Multilingual Voice Query", 0.78),
        ("UC-2: Upload Crop Leaf Photo for Optical Diagnosis", 0.64),
        ("UC-3: View Hyper-Local Weather & Spray Window Alerts", 0.50),
        ("UC-4: Forecast Commodity Market Prices & Mandi Trends", 0.36),
        ("UC-5: Retrieve Verified RAG Agronomy Treatment Guide", 0.22),
        ("UC-6: Download Comprehensive PDF Advisory Report", 0.08)
    ]

    for uc_text, uy in use_cases:
        ellipse = mpatches.FancyBboxPatch((0.32, uy - 0.04), 0.56, 0.08, boxstyle="round,pad=0.02",
                                          facecolor='#eff6ff', edgecolor='#2563eb', linewidth=1.5)
        ax.add_patch(ellipse)
        ax.text(0.60, uy, uc_text, ha='center', va='center', color='#1e3a8a', fontsize=8.8, weight='bold')
        # Line from Actor to Use Case
        ax.plot([0.15, 0.32], [0.55, uy], color='#64748b', lw=1.3, linestyle='--')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 0.96)
    plt.axis('off')
    plt.tight_layout()

    out_file = os.path.join(os.getcwd(), "figure_6_2_uml_use_case_diagram.png")
    plt.savefig(out_file, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Generated {out_file}")

def generate_class_diagram():
    fig, ax = plt.subplots(figsize=(13, 8.5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    plt.title("Figure 6.3: UML Class Diagram for AgriGen AI Core Architecture",
              fontsize=14, color='#0f172a', weight='bold', pad=20)

    classes = [
        {
            "name": "UserSession",
            "x": 0.05, "y": 0.56, "w": 0.26, "h": 0.35,
            "attrs": ["- session_id: UUID", "- user_id: String", "- language: String", "- gps_coords: Tuple[float, float]"],
            "methods": ["+ initialize_state(): Dict", "+ update_location(lat, lon)", "+ persist_history()"]
        },
        {
            "name": "AgentSupervisor",
            "x": 0.37, "y": 0.56, "w": 0.28, "h": 0.35,
            "attrs": ["- state_graph: StateGraph", "- active_agents: List[Agent]", "- router_llm: Llama3"],
            "methods": ["+ parse_intent(query): Intent", "+ route_execution(state): Node", "+ aggregate_responses(): Advisory"]
        },
        {
            "name": "WhisperService",
            "x": 0.70, "y": 0.56, "w": 0.26, "h": 0.35,
            "attrs": ["- model_size: String", "- sample_rate: int = 16000", "- supported_langs: List[str]"],
            "methods": ["+ load_model()", "+ transcribe_audio(pcm_blob): str", "+ detect_language(audio): str"]
        },
        {
            "name": "WeatherAgent",
            "x": 0.05, "y": 0.08, "w": 0.20, "h": 0.38,
            "attrs": ["- lstm_model: PyTorch", "- api_key: str", "- seq_length: int = 7"],
            "methods": ["+ fetch_telemetry(coords)", "+ predict_rainfall(): Tensor", "+ evaluate_spray_risk()"]
        },
        {
            "name": "MarketAgent",
            "x": 0.28, "y": 0.08, "w": 0.20, "h": 0.38,
            "attrs": ["- lstm_price_model: PyTorch", "- mandi_dataset: DataFrame", "- horizon: int = 7"],
            "methods": ["+ load_mandi_rates(mandi)", "+ forecast_prices(): List", "+ calculate_profit_margin()"]
        },
        {
            "name": "DiseaseVisionAgent",
            "x": 0.51, "y": 0.08, "w": 0.21, "h": 0.38,
            "attrs": ["- cnn_backbone: ResNet", "- num_classes: int = 38", "- confidence_threshold: float"],
            "methods": ["+ preprocess_image(blob)", "+ classify_pathology(): Result", "+ generate_heatmap()"]
        },
        {
            "name": "KnowledgeRAGAgent",
            "x": 0.75, "y": 0.08, "w": 0.21, "h": 0.38,
            "attrs": ["- faiss_index: IndexFlatIP", "- embedding_model: MiniLM", "- top_k: int = 3"],
            "methods": ["+ embed_query(query): Vector", "+ query_faiss(vector): Docs", "+ synthesize_guidance(): str"]
        }
    ]

    for c in classes:
        # Class container
        box = mpatches.FancyBboxPatch((c["x"], c["y"]), c["w"], c["h"], boxstyle="round,pad=0.01",
                                      facecolor='#ffffff', edgecolor='#0f172a', linewidth=1.5)
        ax.add_patch(box)
        # Title bar
        title_box = mpatches.FancyBboxPatch((c["x"], c["y"] + c["h"] - 0.07), c["w"], 0.07, boxstyle="round,pad=0.01",
                                            facecolor='#e2e8f0', edgecolor='#0f172a', linewidth=1.5)
        ax.add_patch(title_box)
        ax.text(c["x"] + c["w"]/2, c["y"] + c["h"] - 0.035, c["name"],
                ha='center', va='center', color='#0f172a', fontsize=9, weight='bold')

        # Attributes
        attr_text = "\n".join(c["attrs"])
        ax.text(c["x"] + 0.01, c["y"] + c["h"] - 0.16, attr_text,
                ha='left', va='center', color='#334155', fontsize=7.2, linespacing=1.3)
        # Separator line
        ax.plot([c["x"], c["x"] + c["w"]], [c["y"] + c["h"] - 0.22, c["y"] + c["h"] - 0.22], color='#94a3b8', lw=1)
        # Methods
        meth_text = "\n".join(c["methods"])
        ax.text(c["x"] + 0.01, c["y"] + 0.07, meth_text,
                ha='left', va='center', color='#1e3a8a', fontsize=7.2, linespacing=1.3)

    # Association lines
    ax.annotate("", xy=(0.37, 0.73), xytext=(0.31, 0.73),
                arrowprops=dict(facecolor='#0f172a', edgecolor='#0f172a', arrowstyle="->", lw=1.5))
    ax.annotate("", xy=(0.70, 0.73), xytext=(0.65, 0.73),
                arrowprops=dict(facecolor='#0f172a', edgecolor='#0f172a', arrowstyle="->", lw=1.5))

    # Supervisor down to agents
    ax.annotate("", xy=(0.50, 0.46), xytext=(0.50, 0.56),
                arrowprops=dict(facecolor='#0f172a', edgecolor='#0f172a', arrowstyle="->", lw=1.5))
    ax.plot([0.15, 0.85], [0.46, 0.46], color='#0f172a', lw=1.5)
    for agent_x in [0.15, 0.38, 0.61, 0.85]:
        ax.plot([agent_x, agent_x], [0.46, 0.44], color='#0f172a', lw=1.5)

    ax.set_xlim(0, 1.01)
    ax.set_ylim(0, 0.96)
    plt.axis('off')
    plt.tight_layout()

    out_file = os.path.join(os.getcwd(), "figure_6_3_uml_class_diagram.png")
    plt.savefig(out_file, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Generated {out_file}")

if __name__ == '__main__':
    generate_system_architecture()
    generate_use_case_diagram()
    generate_class_diagram()
