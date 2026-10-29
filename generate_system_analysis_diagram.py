import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def generate_system_analysis_diagram():
    fig, ax = plt.subplots(figsize=(13, 8), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    plt.title("Figure 3.1: Architectural Comparison — Existing Fragmented Approach vs. Proposed AgriGen AI Ecosystem",
              fontsize=14, color='#0f172a', weight='bold', pad=20)

    # Left Column: Existing System (Fragmented, High Friction, Error-Prone)
    ex_box = mpatches.FancyBboxPatch((0.03, 0.05), 0.44, 0.86,
                                     boxstyle="round,pad=0.02",
                                     facecolor='#fef2f2', edgecolor='#ef4444', linewidth=2)
    ax.add_patch(ex_box)
    ax.text(0.25, 0.87, "EXISTING SYSTEM (Fragmented & Siloed)",
            ha='center', va='center', color='#991b1b', fontsize=12, weight='bold')

    ex_steps = [
        {"title": "1. Field Observation", "desc": "Farmer notices leaf spot, yellowing, or abnormal crop growth", "y": 0.74, "col": "#fee2e2"},
        {"title": "2. Fragmented Information Search", "desc": "Visits separate weather app, checks news for mandi rates,\ncalls local pesticide shop or extension officer", "y": 0.58, "col": "#fee2e2"},
        {"title": "3. High Literacy & Language Barrier", "desc": "English-dominated menus, technical charts, 50-page PDFs\nlead to confusion and abandonment", "y": 0.42, "col": "#fee2e2"},
        {"title": "4. Delayed & Guesswork Action", "desc": "Unverified chemical cocktails sprayed; delayed harvest;\nselling to middlemen at distress rates", "y": 0.26, "col": "#fee2e2"},
        {"title": "Outcome: Severe Vulnerability", "desc": "High input costs, toxic chemical overuse, 30-40% yield loss,\nand chronic debt cycles", "y": 0.12, "col": "#fecaca"}
    ]

    for s in ex_steps:
        box = mpatches.FancyBboxPatch((0.06, s["y"] - 0.05), 0.38, 0.10,
                                     boxstyle="round,pad=0.01",
                                     facecolor=s["col"], edgecolor='#dc2626', linewidth=1.2)
        ax.add_patch(box)
        ax.text(0.25, s["y"] + 0.02, s["title"], ha='center', va='center', color='#7f1d1d', fontsize=9.5, weight='bold')
        ax.text(0.25, s["y"] - 0.02, s["desc"], ha='center', va='center', color='#374151', fontsize=8, linespacing=1.3)

    # Right Column: Proposed System (AgriGen AI Multi-Agent Ecosystem)
    prop_box = mpatches.FancyBboxPatch((0.53, 0.05), 0.44, 0.86,
                                       boxstyle="round,pad=0.02",
                                       facecolor='#f0fdf4', edgecolor='#16a34a', linewidth=2)
    ax.add_patch(prop_box)
    ax.text(0.75, 0.87, "PROPOSED SYSTEM: AgriGen AI",
            ha='center', va='center', color='#14532d', fontsize=12, weight='bold')

    prop_steps = [
        {"title": "1. Natural Voice / Photo Capture", "desc": "Farmer takes leaf photo or speaks question in mother tongue\n(Hindi, Telugu, or English) via mobile UI", "y": 0.74, "col": "#dcfce7"},
        {"title": "2. LangGraph Supervisor DAG", "desc": "Intelligent orchestrator routes intent across specialized\nautonomous neural agents concurrently", "y": 0.58, "col": "#dcfce7"},
        {"title": "3. Specialist Co-Execution", "desc": "• Weather Agent: LSTM micro-climate risk\n• Market Agent: Mandi price trend forecast\n• Disease Agent: Deep vision pathology\n• Knowledge Agent: FAISS RAG scientific remedies", "y": 0.40, "col": "#dcfce7"},
        {"title": "4. Multimodal Synthesis", "desc": "Instant, conversational spoken advisory + visual charts +\ndownloadable PDF advisory with safe chemical dosage", "y": 0.23, "col": "#dcfce7"},
        {"title": "Outcome: Proactive Precision Farming", "desc": "Protected yields, 25-35% lower input costs, verified science,\nand maximized harvest profitability", "y": 0.10, "col": "#bbf7d0"}
    ]

    for s in prop_steps:
        box = mpatches.FancyBboxPatch((0.56, s["y"] - 0.055), 0.38, 0.11,
                                     boxstyle="round,pad=0.01",
                                     facecolor=s["col"], edgecolor='#15803d', linewidth=1.2)
        ax.add_patch(box)
        ax.text(0.75, s["y"] + 0.025, s["title"], ha='center', va='center', color='#064e3b', fontsize=9.5, weight='bold')
        ax.text(0.75, s["y"] - 0.022, s["desc"], ha='center', va='center', color='#1f2937', fontsize=8, linespacing=1.3)

    # Dividing arrow in middle
    ax.annotate("TRANSFORMATION", xy=(0.53, 0.50), xytext=(0.47, 0.50),
                arrowprops=dict(facecolor='#2563eb', edgecolor='#2563eb', arrowstyle="->", lw=2.5),
                ha='center', va='center', color='#1d4ed8', fontsize=8.5, weight='bold', rotation=90)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.axis('off')
    plt.tight_layout()

    out_file = os.path.join(os.getcwd(), "figure_3_1_system_analysis_comparison.png")
    plt.savefig(out_file, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Generated {out_file} successfully.")

if __name__ == '__main__':
    generate_system_analysis_diagram()
