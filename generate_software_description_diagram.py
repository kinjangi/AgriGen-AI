import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def generate_software_diagram():
    fig, ax = plt.subplots(figsize=(13, 8.5), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    plt.title("Figure 5.1: AgriGen AI Software Architecture & Technology Interaction Flow",
              fontsize=14, color='#0f172a', weight='bold', pad=20)

    # 4 Main Vertical Columns representing the Software Components in Chapter 5
    cols = [
        {
            "title": "FRONTEND & UI\n(5.1 - 5.6)",
            "x": 0.03, "w": 0.21, "bg": "#eff6ff", "border": "#2563eb", "title_col": "#1e40af",
            "items": [
                ("HTML5 Semantic APIs", "Canvas, MediaRecorder, Geolocation, Audio Stream"),
                ("CSS3 Responsive Design", "Flexbox, CSS Grid, Dark Mode, Micro-animations"),
                ("JavaScript (ES6+)", "Async/Await, Fetch API, Blob/Multipart streams"),
                ("React.js 19", "Virtual DOM, Hooks (useState, useEffect, useRef)"),
                ("Chart.js", "Time-series line & bar visualization for price/weather"),
                ("Web Storage", "localStorage for user sessions & local offline cache")
            ]
        },
        {
            "title": "BACKEND SERVICES\n(5.7, 5.12)",
            "x": 0.27, "w": 0.21, "bg": "#f0fdf4", "border": "#16a34a", "title_col": "#166534",
            "items": [
                ("Python 3.10+", "Asynchronous runtime, dynamic typing, tensor support"),
                ("FastAPI Framework", "Async routes, OpenAPI docs, SSE streaming endpoints"),
                ("Uvicorn ASGI", "Asynchronous Server Gateway Interface for high QPS"),
                ("Pydantic v2", "Strict schema validation and data serialization"),
                ("SQLAlchemy ORM", "Declarative object mapping & connection pooling"),
                ("PostgreSQL / Redis", "Relational persistence & in-memory session cache")
            ]
        },
        {
            "title": "AI & MULTI-AGENT\n(5.8 - 5.10)",
            "x": 0.51, "w": 0.21, "bg": "#faf5ff", "border": "#9333ea", "title_col": "#6b21a8",
            "items": [
                ("LangGraph", "Cyclic Directed Acyclic Graph (DAG) state machine"),
                ("LangChain Core", "Context chaining, prompt assembly, and output parsers"),
                ("PyTorch v2.x", "LSTM neural networks for price & weather regression"),
                ("Torchvision", "Convolutional neural network for leaf pathology"),
                ("FAISS Vector DB", "Dense cosine similarity search over ICAR literature"),
                ("Sentence-Transformers", "Embedding generation (all-MiniLM-L6-v2)")
            ]
        },
        {
            "title": "VOICE & UTILITIES\n(5.11, WeasyPrint)",
            "x": 0.75, "w": 0.21, "bg": "#fff7ed", "border": "#ea580c", "title_col": "#9a3412",
            "items": [
                ("OpenAI Whisper", "Seq2Seq Transformer for multilingual speech-to-text"),
                ("gTTS / Web Speech", "Text-to-Speech synthesis in Hindi, Telugu, English"),
                ("WeasyPrint Engine", "Compiles HTML/CSS into downloadable PDF reports"),
                ("Docker & Compose", "Containerized microservice sandboxing & isolation"),
                ("NGINX Gateway", "Reverse proxy, rate limiting, and SSL termination"),
                ("Cross-Platform", "Responsive execution on mobile, tablet, and desktop")
            ]
        }
    ]

    for col in cols:
        # Column card
        rect = mpatches.FancyBboxPatch((col["x"], 0.05), col["w"], 0.86,
                                      boxstyle="round,pad=0.015",
                                      facecolor=col["bg"], edgecolor=col["border"], linewidth=1.8)
        ax.add_patch(rect)
        ax.text(col["x"] + col["w"]/2, 0.86, col["title"],
                ha='center', va='center', color=col["title_col"], fontsize=10.5, weight='bold')

        # Items inside column
        y_starts = [0.73, 0.60, 0.47, 0.34, 0.21, 0.08]
        for idx, (head, body) in enumerate(col["items"]):
            item_box = mpatches.FancyBboxPatch((col["x"] + 0.01, y_starts[idx] - 0.045), col["w"] - 0.02, 0.10,
                                               boxstyle="round,pad=0.01",
                                               facecolor="#ffffff", edgecolor=col["border"], linewidth=0.8)
            ax.add_patch(item_box)
            ax.text(col["x"] + col["w"]/2, y_starts[idx] + 0.025, head,
                    ha='center', va='center', color='#0f172a', fontsize=8.5, weight='bold')
            ax.text(col["x"] + col["w"]/2, y_starts[idx] - 0.018, body,
                    ha='center', va='center', color='#475569', fontsize=7.2, linespacing=1.2)

    # Inter-column connection arrows
    arrows = [
        ((0.24, 0.50), (0.27, 0.50)),
        ((0.48, 0.50), (0.51, 0.50)),
        ((0.72, 0.50), (0.75, 0.50)),
    ]
    for start, end in arrows:
        ax.annotate("", xy=end, xytext=start,
                    arrowprops=dict(facecolor='#0284c7', edgecolor='#0284c7', arrowstyle="->", lw=2.5))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 0.95)
    plt.axis('off')
    plt.tight_layout()

    out_file = os.path.join(os.getcwd(), "figure_5_1_software_architecture_stack.png")
    plt.savefig(out_file, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
    plt.close()
    print(f"Generated {out_file} successfully.")

if __name__ == '__main__':
    generate_software_diagram()
