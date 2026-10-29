import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def generate_sequence_diagram():
    fig, ax = plt.subplots(figsize=(13, 8.5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    plt.title("Figure 6.4: UML Sequence Diagram for Multimodal Advisory Request Execution",
              fontsize=14, color='#0f172a', weight='bold', pad=20)

    lifelines = [
        ("Farmer\n(Client UI)", 0.08),
        ("FastAPI\nGateway", 0.26),
        ("Whisper\nEngine", 0.44),
        ("LangGraph\nSupervisor", 0.62),
        ("Specialist\nAgents", 0.80),
        ("FAISS RAG\n& DB", 0.94)
    ]

    # Draw lifelines
    for name, x in lifelines:
        box = mpatches.FancyBboxPatch((x - 0.06, 0.86), 0.12, 0.07, boxstyle="round,pad=0.01",
                                      facecolor='#e2e8f0', edgecolor='#0f172a', linewidth=1.2)
        ax.add_patch(box)
        ax.text(x, 0.895, name, ha='center', va='center', color='#0f172a', fontsize=8.5, weight='bold')
        ax.plot([x, x], [0.86, 0.05], color='#94a3b8', linestyle='--', lw=1.2)

    messages = [
        (0.08, 0.26, 0.80, "1. Voice Audio / Leaf Photo Upload (POST)", "#0284c7"),
        (0.26, 0.44, 0.73, "2. Stream raw PCM audio buffer", "#0284c7"),
        (0.44, 0.26, 0.66, "3. Transcribed vernacular text (Hindi/Telugu)", "#16a34a"),
        (0.26, 0.62, 0.59, "4. Initialize State & invoke Supervisor DAG", "#0284c7"),
        (0.62, 0.80, 0.52, "5. Dispatch parallel tasks (Weather/Vision/Price)", "#0284c7"),
        (0.80, 0.94, 0.45, "6. Query FAISS index for agronomy papers", "#0284c7"),
        (0.94, 0.80, 0.38, "7. Return verified ICAR treatment context", "#16a34a"),
        (0.80, 0.62, 0.31, "8. Return specialist predictions & diagnostic results", "#16a34a"),
        (0.62, 0.26, 0.24, "9. Aggregate multi-agent response & synthesize", "#16a34a"),
        (0.26, 0.08, 0.17, "10. SSE Token Stream + Audio TTS + Chart Data", "#16a34a"),
        (0.08, 0.08, 0.10, "11. Render Dashboard Cards & Play Audio Response", "#475569")
    ]

    for x1, x2, y, text, col in messages:
        if x1 != x2:
            linestyle = '-' if col == "#0284c7" else '--'
            ax.annotate("", xy=(x2, y), xytext=(x1, y),
                        arrowprops=dict(facecolor=col, edgecolor=col, arrowstyle="->", lw=1.5, linestyle=linestyle))
            mid_x = (x1 + x2) / 2
            ax.text(mid_x, y + 0.018, text, ha='center', va='bottom', color='#0f172a', fontsize=7.8, weight='bold')
        else:
            # Self-call
            arc = mpatches.Arc((x1 + 0.03, y), 0.06, 0.04, angle=0, theta1=270, theta2=90, color=col, lw=1.5)
            ax.add_patch(arc)
            ax.text(x1 + 0.065, y, text, ha='left', va='center', color='#0f172a', fontsize=7.8, weight='bold')

    ax.set_xlim(0, 1.02)
    ax.set_ylim(0, 0.96)
    plt.axis('off')
    plt.tight_layout()

    out_file = os.path.join(os.getcwd(), "figure_6_4_uml_sequence_diagram.png")
    plt.savefig(out_file, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Generated {out_file}")

if __name__ == '__main__':
    generate_sequence_diagram()
