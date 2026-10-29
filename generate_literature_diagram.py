import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def generate_literature_framework():
    # Academic publication style (white background, clean borders, professional palette)
    fig, ax = plt.subplots(figsize=(13, 8), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    # Main Title
    plt.title("Figure 2.1: Theoretical Framework & Algorithmic Foundations of AgriGen AI",
              fontsize=15, color='#1e293b', weight='bold', pad=22)

    # Sub-framework 1: Multi-Agent State Machine
    box_mas = mpatches.FancyBboxPatch((0.04, 0.54), 0.43, 0.38,
                                      boxstyle="round,pad=0.02",
                                      facecolor='#eff6ff', edgecolor='#2563eb', linewidth=1.8)
    ax.add_patch(box_mas)
    ax.text(0.255, 0.88, "1. Multi-Agent Orchestration Theory",
            ha='center', va='center', color='#1e3a8a', fontsize=11, weight='bold')
    ax.text(0.255, 0.72,
            "• Supervisor DAG: M = <S, A, T, O>\n"
            "• Dynamic Routing via LLM Meta-Prompting\n"
            "• Context Isolation to prevent Hallucination\n"
            "• Eliminates single-agent prompt dilution\n"
            "• References: Wu et al. (2023), LangGraph",
            ha='center', va='center', color='#334155', fontsize=9.5, linespacing=1.6)

    # Sub-framework 2: LSTM Recurrent Networks
    box_lstm = mpatches.FancyBboxPatch((0.53, 0.54), 0.43, 0.38,
                                       boxstyle="round,pad=0.02",
                                       facecolor='#f0fdf4', edgecolor='#16a34a', linewidth=1.8)
    ax.add_patch(box_lstm)
    ax.text(0.745, 0.88, "2. Time-Series Deep Learning (LSTM)",
            ha='center', va='center', color='#14532d', fontsize=11, weight='bold')
    ax.text(0.745, 0.72,
            "• Gated Memory: Forget (f_t), Input (i_t), Output (o_t)\n"
            "• Cell State Update: C_t = f_t * C_{t-1} + i_t * C~_t\n"
            "• Solves Vanishing Gradients over long sequences\n"
            "• Dual deployment: Weather & Mandi Crop Prices\n"
            "• References: Hochreiter (1997), Su et al. (2020)",
            ha='center', va='center', color='#334155', fontsize=9.5, linespacing=1.6)

    # Sub-framework 3: Computer Vision & Pathology
    box_cv = mpatches.FancyBboxPatch((0.04, 0.08), 0.43, 0.38,
                                     boxstyle="round,pad=0.02",
                                     facecolor='#fef2f2', edgecolor='#dc2626', linewidth=1.8)
    ax.add_patch(box_cv)
    ax.text(0.255, 0.42, "3. Deep Residual Computer Vision",
            ha='center', va='center', color='#991b1b', fontsize=11, weight='bold')
    ax.text(0.255, 0.26,
            "• Spatial Feature Extraction: z_{l+1} = F(z_l, W) + z_l\n"
            "• Multi-class leaf pathology classification\n"
            "• Lesion texture and fungal chlorosis recognition\n"
            "• Overcomes laboratory bias on field imagery\n"
            "• References: Mohanty et al. (2016), Ferentinos (2018)",
            ha='center', va='center', color='#334155', fontsize=9.5, linespacing=1.6)

    # Sub-framework 4: RAG & Dense Vector Retrieval
    box_rag = mpatches.FancyBboxPatch((0.53, 0.08), 0.43, 0.38,
                                      boxstyle="round,pad=0.02",
                                      facecolor='#faf5ff', edgecolor='#9333ea', linewidth=1.8)
    ax.add_patch(box_rag)
    ax.text(0.745, 0.42, "4. Dense Retrieval RAG & Acoustic Modeling",
            ha='center', va='center', color='#581c87', fontsize=11, weight='bold')
    ax.text(0.745, 0.26,
            "• FAISS Vector Similarity: Cosine(v_q, v_i)\n"
            "• Agronomy Research Corpus Indexing (ICAR/FAO)\n"
            "• Whisper Seq2Seq Multilingual Audio Encoder\n"
            "• Voice interface in Hindi, Telugu, and English\n"
            "• References: Lewis et al. (2020), Radford et al. (2022)",
            ha='center', va='center', color='#334155', fontsize=9.5, linespacing=1.6)

    # Connecting central convergence node
    central_badge = mpatches.FancyBboxPatch((0.40, 0.46), 0.20, 0.08,
                                           boxstyle="round,pad=0.01",
                                           facecolor='#0f172a', edgecolor='#38bdf8', linewidth=1.5)
    ax.add_patch(central_badge)
    ax.text(0.50, 0.50, "AgriGen AI\nCore Synthesis",
            ha='center', va='center', color='#ffffff', fontsize=9, weight='bold')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.axis('off')
    plt.tight_layout()

    out_file = os.path.join(os.getcwd(), "figure_2_1_theoretical_framework.png")
    plt.savefig(out_file, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Generated {out_file} successfully.")

if __name__ == '__main__':
    generate_literature_framework()
