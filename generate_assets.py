import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def create_architecture_diagram():
    fig, ax = plt.subplots(figsize=(12, 7), dpi=300)
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')

    # Title
    plt.title("AgriGen AI - Phase 1 High-Level Architecture", fontsize=16, color='#38bdf8', weight='bold', pad=20)

    # Boxes
    boxes = [
        # User & Frontend
        {"name": "React + Vite Frontend\n(Interactive Dashboard & Voice/Image UI)", "x": 0.05, "y": 0.65, "w": 0.25, "h": 0.25, "color": "#1e293b", "ec": "#38bdf8"},
        
        # FastAPI Hub
        {"name": "FastAPI Orchestrator Backend\n(REST API / SSE Streaming / Auth)", "x": 0.38, "y": 0.65, "w": 0.25, "h": 0.25, "color": "#1e293b", "ec": "#4ade80"},
        
        # LangGraph Supervisor
        {"name": "LangGraph Supervisor Node\n(Llama-3 Dynamic Multi-Agent Router)", "x": 0.70, "y": 0.65, "w": 0.25, "h": 0.25, "color": "#1e293b", "ec": "#a78bfa"},
        
        # Specialist Agents Block
        {"name": "Weather Agent\n(PyTorch LSTM)", "x": 0.55, "y": 0.25, "w": 0.18, "h": 0.18, "color": "#0f172a", "ec": "#facc15"},
        {"name": "Market Agent\n(Price Forecasting)", "x": 0.76, "y": 0.25, "w": 0.18, "h": 0.18, "color": "#0f172a", "ec": "#fb923c"},
        {"name": "Disease Agent\n(Vision Classifier)", "x": 0.55, "y": 0.02, "w": 0.18, "h": 0.18, "color": "#0f172a", "ec": "#f87171"},
        {"name": "RAG Knowledge Agent\n(FAISS Vector DB)", "x": 0.76, "y": 0.02, "w": 0.18, "h": 0.18, "color": "#0f172a", "ec": "#34d399"},

        # Data Layer
        {"name": "Database Layer\n(PostgreSQL / SQLite & Redis Cache)", "x": 0.12, "y": 0.15, "w": 0.30, "h": 0.30, "color": "#1e293b", "ec": "#f43f5e"},
    ]

    for b in boxes:
        rect = mpatches.FancyBboxPatch((b["x"], b["y"]), b["w"], b["h"],
                                      boxstyle="round,pad=0.03",
                                      facecolor=b["color"], edgecolor=b["ec"], linewidth=2)
        ax.add_patch(rect)
        ax.text(b["x"] + b["w"]/2, b["y"] + b["h"]/2, b["name"],
                ha='center', va='center', color='#f8fafc', fontsize=9, weight='bold', wrap=True)

    # Arrows
    arrows = [
        ((0.30, 0.77), (0.38, 0.77), "HTTP / SSE"),
        ((0.63, 0.77), (0.70, 0.77), "State Machine"),
        ((0.75, 0.65), (0.64, 0.43), "Delegate"),
        ((0.85, 0.65), (0.85, 0.43), "Delegate"),
        ((0.45, 0.65), (0.27, 0.45), "SQL / Cache"),
    ]

    for start, end, label in arrows:
        ax.annotate(label, xy=end, xytext=start,
                    arrowprops=dict(facecolor='#94a3b8', edgecolor='#94a3b8', arrowstyle="->", lw=1.5),
                    color='#cbd5e1', fontsize=8, weight='bold', ha='center')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.axis('off')
    plt.tight_layout()
    output_path = os.path.join(os.getcwd(), "system_architecture.png")
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Saved {output_path}")

def create_workflow_diagram():
    fig, ax = plt.subplots(figsize=(12, 5), dpi=300)
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')

    plt.title("AgriGen AI - Multi-Agent Processing Workflow", fontsize=16, color='#4ade80', weight='bold', pad=20)

    steps = [
        {"num": "Step 1", "title": "Farmer Query / Input", "desc": "Voice (Whisper) / Leaf Photo / Text", "x": 0.05},
        {"num": "Step 2", "title": "FastAPI Orchestrator", "desc": "Authenticates & Passes State to LangGraph", "x": 0.28},
        {"num": "Step 3", "title": "Supervisor Router", "desc": "Analyzes Intent & Directs to Expert Agent", "x": 0.51},
        {"num": "Step 4", "title": "Agent Execution", "desc": "LSTM Forecast / FAISS RAG / Disease Vision", "x": 0.74},
    ]

    for s in steps:
        rect = mpatches.FancyBboxPatch((s["x"], 0.3), 0.20, 0.45,
                                      boxstyle="round,pad=0.03",
                                      facecolor='#1e293b', edgecolor='#38bdf8', linewidth=2)
        ax.add_patch(rect)
        ax.text(s["x"] + 0.10, 0.63, s["num"], ha='center', va='center', color='#facc15', fontsize=11, weight='bold')
        ax.text(s["x"] + 0.10, 0.50, s["title"], ha='center', va='center', color='#ffffff', fontsize=10, weight='bold')
        ax.text(s["x"] + 0.10, 0.38, s["desc"], ha='center', va='center', color='#94a3b8', fontsize=8, wrap=True)

    for x in [0.25, 0.48, 0.71]:
        ax.annotate("", xy=(x + 0.03, 0.52), xytext=(x, 0.52),
                    arrowprops=dict(facecolor='#4ade80', edgecolor='#4ade80', arrowstyle="->", lw=2))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.axis('off')
    plt.tight_layout()
    output_path = os.path.join(os.getcwd(), "agent_workflow.png")
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Saved {output_path}")

if __name__ == "__main__":
    create_architecture_diagram()
    create_workflow_diagram()
