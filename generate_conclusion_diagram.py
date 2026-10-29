import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def generate_roadmap_diagram():
    fig, ax = plt.subplots(figsize=(13, 8), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    plt.title("Figure 10.1: AgriGen AI Strategic Technology Evolution & Future Roadmap",
              fontsize=14, color='#0f172a', weight='bold', pad=20)

    phases = [
        {
            "phase": "PHASE 1: CURRENT DELIVERED BASELINE",
            "subtitle": "Multi-Agent Advisory & Multimodal AI Core",
            "x": 0.04, "w": 0.28, "bg": "#eff6ff", "border": "#2563eb", "title_col": "#1e40af",
            "milestones": [
                ("LangGraph Multi-Agent Core", "Supervisor DAG routing across specialist neural agents"),
                ("Deep Vision Pathology", "96.0% F1-score classification of 6 major foliage diseases"),
                ("Time-Series LSTM Models", "7-day weather risk & mandi price forecasting (MAPE 2.1%)"),
                ("FAISS RAG Knowledge", "Verified ICAR agronomic research literature integration"),
                ("Multilingual Voice Engine", "OpenAI Whisper STT + TTS in Hindi, Telugu, and English"),
                ("Production Cloud Stack", "FastAPI, React 19, Docker, PostgreSQL 15, and Redis 7")
            ]
        },
        {
            "phase": "PHASE 2: NEAR-TERM HORIZON (6-12 MONTHS)",
            "subtitle": "Edge-AI, IoT Sensor Mesh & Drone Multispectral",
            "x": 0.36, "w": 0.28, "bg": "#f0fdf4", "border": "#16a34a", "title_col": "#166534",
            "milestones": [
                ("Edge-AI / TinyML Models", "ONNX quantized vision models running 100% offline on mobile"),
                ("IoT In-Field Sensor Mesh", "LoRaWAN soil NPK, moisture & canopy sensor telemetry"),
                ("Drone Multispectral Feeds", "UAV aerial imaging for NDVI canopy vigor & flood mapping"),
                ("Expanded Vernaculars", "Acoustic support for Tamil, Kannada, Marathi & Bengali"),
                ("Automated Crop Calibrator", "Dynamic GDD (Growing Degree Day) stage-based scheduling"),
                ("Predictive Pest Swarm Alerts", "Regional epidemiological pest outbreak early warning")
            ]
        },
        {
            "phase": "PHASE 3: LONG-TERM VISION (1-3 YEARS)",
            "subtitle": "Decentralized FPO Commerce & Carbon Credits",
            "x": 0.68, "w": 0.28, "bg": "#faf5ff", "border": "#9333ea", "title_col": "#6b21a8",
            "milestones": [
                ("Direct-to-Buyer Commerce", "Disintermediating middlemen via smart-contract contracts"),
                ("FPO Aggregation Logistics", "Bulk transport route optimization for Farmer Collectives"),
                ("Carbon Credit Monetization", "Satellite-verified regenerative agriculture carbon ledger"),
                ("Institutional Credit AI", "Alternative credit scoring based on verified farm health logs"),
                ("Govt Scheme Automator", "Direct discovery & one-click application for subsidies"),
                ("Autonomous Robotic Fleets", "API control for autonomous weeding & targeted spot-sprayers")
            ]
        }
    ]

    for p in phases:
        rect = mpatches.FancyBboxPatch((p["x"], 0.06), p["w"], 0.86,
                                      boxstyle="round,pad=0.015",
                                      facecolor=p["bg"], edgecolor=p["border"], linewidth=1.8)
        ax.add_patch(rect)
        ax.text(p["x"] + p["w"]/2, 0.88, p["phase"],
                ha='center', va='center', color=p["title_col"], fontsize=9.5, weight='bold')
        ax.text(p["x"] + p["w"]/2, 0.84, p["subtitle"],
                ha='center', va='center', color='#64748b', fontsize=7.8, style='italic')

        y_positions = [0.72, 0.59, 0.46, 0.33, 0.20, 0.07]
        for idx, (title, desc) in enumerate(p["milestones"]):
            item_box = mpatches.FancyBboxPatch((p["x"] + 0.01, y_positions[idx] - 0.035), p["w"] - 0.02, 0.095,
                                               boxstyle="round,pad=0.01",
                                               facecolor="#ffffff", edgecolor=p["border"], linewidth=0.8)
            ax.add_patch(item_box)
            ax.text(p["x"] + 0.02, y_positions[idx] + 0.025, f"✔ {title}",
                    ha='left', va='center', color='#0f172a', fontsize=8.2, weight='bold')
            ax.text(p["x"] + 0.02, y_positions[idx] - 0.018, desc,
                    ha='left', va='center', color='#475569', fontsize=7.0, linespacing=1.2)

    # Connecting evolution arrows
    ax.annotate("", xy=(0.36, 0.50), xytext=(0.32, 0.50),
                arrowprops=dict(facecolor='#0284c7', edgecolor='#0284c7', arrowstyle="->", lw=2.5))
    ax.annotate("", xy=(0.68, 0.50), xytext=(0.64, 0.50),
                arrowprops=dict(facecolor='#0284c7', edgecolor='#0284c7', arrowstyle="->", lw=2.5))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 0.96)
    plt.axis('off')
    plt.tight_layout()

    out_file = os.path.join(os.getcwd(), "figure_10_1_future_roadmap_milestones.png")
    plt.savefig(out_file, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Generated {out_file} successfully.")

if __name__ == '__main__':
    generate_roadmap_diagram()
