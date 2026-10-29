import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def generate_lstm_diagram():
    fig, ax = plt.subplots(figsize=(12, 6.5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    plt.title("Figure 2.2: Internal Architecture and Gating Mechanisms of the LSTM Recurrent Cell",
              fontsize=14, color='#1e293b', weight='bold', pad=18)

    # Main LSTM Cell boundary
    cell_box = mpatches.FancyBboxPatch((0.15, 0.12), 0.70, 0.76,
                                      boxstyle="round,pad=0.03",
                                      facecolor='#f8fafc', edgecolor='#0284c7', linewidth=2.5)
    ax.add_patch(cell_box)
    ax.text(0.50, 0.84, "LSTM Cell at Time Step t",
            ha='center', va='center', color='#0369a1', fontsize=12, weight='bold')

    # Gates
    gates = [
        {"name": "Forget Gate (f_t)\n[σ]\nf_t = σ(W_f · [h_{t-1}, x_t] + b_f)", "x": 0.22, "y": 0.40, "w": 0.15, "h": 0.28, "color": "#fee2e2", "ec": "#ef4444"},
        {"name": "Input Gate (i_t)\n[σ]\ni_t = σ(W_i · [h_{t-1}, x_t] + b_i)", "x": 0.40, "y": 0.40, "w": 0.15, "h": 0.28, "color": "#fef3c7", "ec": "#f59e0b"},
        {"name": "Candidate Cell (~C_t)\n[tanh]\n~C_t = tanh(W_c · [h_{t-1}, x_t] + b_c)", "x": 0.58, "y": 0.40, "w": 0.16, "h": 0.28, "color": "#dcfce7", "ec": "#10b981"},
        {"name": "Output Gate (o_t)\n[σ]\no_t = σ(W_o · [h_{t-1}, x_t] + b_o)", "x": 0.77, "y": 0.40, "w": 0.15, "h": 0.28, "color": "#e0e7ff", "ec": "#6366f1"}
    ]

    for g in gates:
        rect = mpatches.FancyBboxPatch((g["x"] - g["w"]/2, g["y"] - g["h"]/2), g["w"], g["h"],
                                      boxstyle="round,pad=0.02",
                                      facecolor=g["color"], edgecolor=g["ec"], linewidth=1.5)
        ax.add_patch(rect)
        ax.text(g["x"], g["y"], g["name"],
                ha='center', va='center', color='#0f172a', fontsize=8, weight='bold')

    # Cell State Line across top
    ax.annotate("", xy=(0.95, 0.72), xytext=(0.05, 0.72),
                arrowprops=dict(facecolor='#0284c7', edgecolor='#0284c7', arrowstyle="->", lw=3))
    ax.text(0.04, 0.75, "C_{t-1}\n(Previous Cell State)", ha='right', va='center', fontsize=9, color='#0284c7', weight='bold')
    ax.text(0.96, 0.75, "C_t\n(New Cell State)", ha='left', va='center', fontsize=9, color='#0284c7', weight='bold')

    # Cell state update annotation
    ax.text(0.50, 0.75, "C_t = f_t ⊙ C_{t-1} + i_t ⊙ ~C_t",
            ha='center', va='bottom', fontsize=9.5, color='#0369a1', weight='bold',
            bbox=dict(boxstyle="square,pad=0.2", facecolor='#e0f2fe', edgecolor='#0284c7', lw=1))

    # Inputs at bottom
    ax.annotate("", xy=(0.50, 0.22), xytext=(0.50, 0.02),
                arrowprops=dict(facecolor='#475569', edgecolor='#475569', arrowstyle="->", lw=2.5))
    ax.text(0.50, 0.00, "Inputs: Current Step x_t + Previous Hidden State h_{t-1}",
            ha='center', va='top', fontsize=9.5, color='#334155', weight='bold')

    # Hidden State Output
    ax.annotate("", xy=(0.88, 0.25), xytext=(0.80, 0.25),
                arrowprops=dict(facecolor='#6366f1', edgecolor='#6366f1', arrowstyle="->", lw=2.5))
    ax.text(0.96, 0.25, "h_t = o_t ⊙ tanh(C_t)\n(Output Hidden State)",
            ha='left', va='center', fontsize=9, color='#4338ca', weight='bold')

    ax.set_xlim(0, 1.15)
    ax.set_ylim(-0.06, 0.95)
    plt.axis('off')
    plt.tight_layout()

    out_file = os.path.join(os.getcwd(), "figure_2_2_lstm_cell_mechanics.png")
    plt.savefig(out_file, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Generated {out_file} successfully.")

if __name__ == '__main__':
    generate_lstm_diagram()
