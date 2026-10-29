import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Enable Nirmala UI and Segoe UI Emoji for flawless Telugu/Hindi and UI rendering
plt.rcParams['font.family'] = 'Nirmala UI'

def generate_screen_1():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')

    # Top Navbar
    nav = mpatches.FancyBboxPatch((0.02, 0.88), 0.96, 0.09, boxstyle="round,pad=0.01",
                                  facecolor='#1e293b', edgecolor='#334155', lw=1.2)
    ax.add_patch(nav)
    ax.text(0.05, 0.925, "AgriGen AI | Intelligent Smart Farming Platform",
            ha='left', va='center', color='#38bdf8', fontsize=12, weight='bold')
    ax.text(0.70, 0.925, "Location: Razam, AP (18.45°N, 83.66°E) | Lang: [ Telugu / Hindi / EN ]",
            ha='left', va='center', color='#94a3b8', fontsize=8.5)

    # Widget 1: Weather & Spray Risk Card
    w1 = mpatches.FancyBboxPatch((0.02, 0.48), 0.46, 0.37, boxstyle="round,pad=0.015",
                                 facecolor='#1e293b', edgecolor='#38bdf8', lw=1.5)
    ax.add_patch(w1)
    ax.text(0.05, 0.81, "Hyper-Local Weather & Spray Risk Advisory", color='#38bdf8', fontsize=11, weight='bold')
    ax.text(0.05, 0.74, "Temperature: 31.5°C | Relative Humidity: 68%\nSoil Moisture: 24.2% | Wind: 8.5 km/h ENE",
            color='#f8fafc', fontsize=9, linespacing=1.4)
    # Spray alert badge
    badge = mpatches.FancyBboxPatch((0.05, 0.52), 0.40, 0.16, boxstyle="round,pad=0.01",
                                    facecolor='#450a0a', edgecolor='#ef4444', lw=1.2)
    ax.add_patch(badge)
    ax.text(0.25, 0.63, "SPRAY ALERT: Heavy Rain Predicted in 18 Hours",
            ha='center', va='center', color='#fca5a5', fontsize=9, weight='bold')
    ax.text(0.25, 0.56, "Do not apply chemical pesticides today.\nHigh precipitation probability (85%).",
            ha='center', va='center', color='#fee2e2', fontsize=7.8, linespacing=1.2)

    # Widget 2: Market Intelligence Card
    w2 = mpatches.FancyBboxPatch((0.52, 0.48), 0.46, 0.37, boxstyle="round,pad=0.015",
                                 facecolor='#1e293b', edgecolor='#4ade80', lw=1.5)
    ax.add_patch(w2)
    ax.text(0.55, 0.81, "Commodity Market Rates & Projections", color='#4ade80', fontsize=11, weight='bold')
    ax.text(0.55, 0.74, "Crop: Paddy (Basmati / Medium) | Nearest: Warangal Mandi\nModal Price: Rs 7,450 / Quintal (+3.2% trend)",
            color='#f8fafc', fontsize=9, linespacing=1.4)
    badge2 = mpatches.FancyBboxPatch((0.55, 0.52), 0.40, 0.16, boxstyle="round,pad=0.01",
                                     facecolor='#064e3b', edgecolor='#10b981', lw=1.2)
    ax.add_patch(badge2)
    ax.text(0.75, 0.63, "MARKET ADVICE: Hold Harvest for 3 Days",
            ha='center', va='center', color='#86efac', fontsize=9, weight='bold')
    ax.text(0.75, 0.56, "LSTM Model projects price peak at Rs 7,620\non Thursday due to regional supply constraint.",
            ha='center', va='center', color='#dcfce7', fontsize=7.8, linespacing=1.2)

    # Bottom Area: Quick Action Hub & Soil Summary
    w3 = mpatches.FancyBboxPatch((0.02, 0.06), 0.96, 0.38, boxstyle="round,pad=0.015",
                                 facecolor='#1e293b', edgecolor='#64748b', lw=1.2)
    ax.add_patch(w3)
    ax.text(0.05, 0.39, "SoilGrids Telemetry & Quick Diagnostic Launchpad", color='#f8fafc', fontsize=11, weight='bold')
    ax.text(0.05, 0.30, "Soil Texture: Clay Loam | Soil pH: 6.4 (Slightly Acidic) | Organic Carbon: 0.72% (Medium)",
            color='#94a3b8', fontsize=8.8)

    btns = [
        ("Voice Advisory Console", 0.05, "#0284c7"),
        ("Scan Crop Leaf Photo", 0.37, "#16a34a"),
        ("Download PDF Dossier", 0.69, "#9333ea")
    ]
    for text, bx, col in btns:
        btn_box = mpatches.FancyBboxPatch((bx, 0.12), 0.26, 0.12, boxstyle="round,pad=0.015",
                                          facecolor=col, edgecolor='#ffffff', lw=1)
        ax.add_patch(btn_box)
        ax.text(bx + 0.13, 0.18, text, ha='center', va='center', color='#ffffff', fontsize=9.5, weight='bold')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.axis('off')
    plt.tight_layout()

    out = os.path.join(os.getcwd(), "output_screen_1_home_dashboard.png")
    plt.savefig(out, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    print(f"Generated {out}")

def generate_screen_2():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')

    # Header
    nav = mpatches.FancyBboxPatch((0.02, 0.88), 0.96, 0.09, boxstyle="round,pad=0.01",
                                  facecolor='#1e293b', edgecolor='#334155', lw=1.2)
    ax.add_patch(nav)
    ax.text(0.05, 0.925, "AgriGen AI Multilingual Conversational Advisory Console",
            ha='left', va='center', color='#38bdf8', fontsize=12, weight='bold')
    ax.text(0.72, 0.925, "Whisper Engine: ACTIVE (Telugu / Hindi / EN)",
            ha='left', va='center', color='#4ade80', fontsize=8.5)

    # Chat Log Container
    chat_box = mpatches.FancyBboxPatch((0.02, 0.22), 0.96, 0.63, boxstyle="round,pad=0.015",
                                      facecolor='#1e293b', edgecolor='#334155', lw=1)
    ax.add_patch(chat_box)

    # Farmer Message 1 (Telugu Voice Query)
    msg1 = mpatches.FancyBboxPatch((0.35, 0.70), 0.60, 0.12, boxstyle="round,pad=0.01",
                                  facecolor='#0369a1', edgecolor='#38bdf8', lw=1)
    ax.add_patch(msg1)
    ax.text(0.37, 0.77, "Farmer (Voice Input - Transcribed Telugu):", color='#e0f2fe', fontsize=8.5, weight='bold')
    ax.text(0.37, 0.73, '"వరి ఆకుపై ఎర్రటి మచ్చలు వచ్చాయి, రేపు మందు పిచికారీ చేయవచ్చా?"',
            color='#ffffff', fontsize=9.2, style='italic')

    # Agent Response 1 (Multimodal Synthesized Advice)
    msg2 = mpatches.FancyBboxPatch((0.05, 0.26), 0.88, 0.40, boxstyle="round,pad=0.01",
                                  facecolor='#0f172a', edgecolor='#10b981', lw=1.5)
    ax.add_patch(msg2)
    ax.text(0.07, 0.62, "AgriGen Multi-Agent Response (Supervisor + Vision + Weather):",
            color='#4ade80', fontsize=9.5, weight='bold')
    
    body = (
        "1. వ్యాధి నిర్ధారణ (Diagnosis): Brown Spot (బిపోలారిస్ ఒరైజే) తెగులుగా గుర్తించబడింది.\n"
        "2. వాతావరణ హెచ్చరిక (Weather Alert): రాగల 18 గంటల్లో మీ ప్రాంతంలో వర్షం (85%) కురిసే అవకాశం ఉంది.\n"
        "3. సూచన (Recommendation): ఈ రోజు ఎలాంటి రసాయన మందు పిచికారీ చేయవద్దు. వర్షం తగ్గిన తర్వాత\n"
        "   గురువారం ఉదయం హెక్సాకోనాజోల్ 5% EC (Hexaconazole) 2 మి.లీ లీటరు నీటికి కలిపి పిచికారీ చేయండి.\n"
        "4. శాస్త్రీయ ఆధారము: ICAR-NRRI ప్యాడీ ప్రొటెక్షన్ ప్రొటోకాల్ 2024 నుండి సరిచూడబడింది."
    )
    ax.text(0.07, 0.46, body, color='#f8fafc', fontsize=8.8, linespacing=1.4)
    ax.text(0.07, 0.29, "[Playing Spoken Audio Advisory in Telugu via gTTS...]",
            color='#38bdf8', fontsize=8.2, weight='bold')

    # Input Bar at bottom
    inp = mpatches.FancyBboxPatch((0.02, 0.05), 0.96, 0.13, boxstyle="round,pad=0.01",
                                  facecolor='#1e293b', edgecolor='#64748b', lw=1)
    ax.add_patch(inp)
    mic_btn = mpatches.FancyBboxPatch((0.04, 0.07), 0.22, 0.09, boxstyle="round,pad=0.01",
                                      facecolor='#dc2626', edgecolor='#ffffff', lw=1)
    ax.add_patch(mic_btn)
    ax.text(0.15, 0.115, "0:04 Recording...", ha='center', va='center', color='#ffffff', fontsize=8.5, weight='bold')

    ax.text(0.29, 0.115, "Type a question or speak in your native dialect (Telugu / Hindi / EN)...", color='#64748b', fontsize=8.8)
    
    send_btn = mpatches.FancyBboxPatch((0.85, 0.07), 0.11, 0.09, boxstyle="round,pad=0.01",
                                       facecolor='#2563eb', edgecolor='#ffffff', lw=1)
    ax.add_patch(send_btn)
    ax.text(0.905, 0.115, "Send", ha='center', va='center', color='#ffffff', fontsize=8.5, weight='bold')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.axis('off')
    plt.tight_layout()

    out = os.path.join(os.getcwd(), "output_screen_2_voice_chat.png")
    plt.savefig(out, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    print(f"Generated {out}")

def generate_screen_3():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')

    # Header
    nav = mpatches.FancyBboxPatch((0.02, 0.88), 0.96, 0.09, boxstyle="round,pad=0.01",
                                  facecolor='#1e293b', edgecolor='#334155', lw=1.2)
    ax.add_patch(nav)
    ax.text(0.05, 0.925, "Leaf Pathology Optical Scanner & Vision Diagnostic Screen",
            ha='left', va='center', color='#38bdf8', fontsize=12, weight='bold')

    # Left Container: Uploaded Image Preview & Lesion Bounding Boxes
    img_box = mpatches.FancyBboxPatch((0.02, 0.06), 0.44, 0.79, boxstyle="round,pad=0.015",
                                      facecolor='#1e293b', edgecolor='#f43f5e', lw=1.5)
    ax.add_patch(img_box)
    ax.text(0.24, 0.80, "Uploaded Foliage Sample", ha='center', va='center', color='#f43f5e', fontsize=10.5, weight='bold')
    
    leaf_canvas = mpatches.FancyBboxPatch((0.06, 0.14), 0.36, 0.60, boxstyle="round,pad=0.01",
                                          facecolor='#064e3b', edgecolor='#10b981', lw=2)
    ax.add_patch(leaf_canvas)
    ax.text(0.24, 0.45, "Leaf Specimen\n(Solanum lycopersicum)", ha='center', va='center', color='#86efac', fontsize=10, weight='bold')
    
    # Bounding boxes representing YOLO/Vision lesion localization
    bbox1 = mpatches.Rectangle((0.12, 0.48), 0.11, 0.12, fill=False, edgecolor='#ef4444', lw=2, linestyle='--')
    ax.add_patch(bbox1)
    ax.text(0.12, 0.62, "Lesion 1: 96.4%", color='#fca5a5', fontsize=7.5, weight='bold')

    bbox2 = mpatches.Rectangle((0.24, 0.25), 0.12, 0.10, fill=False, edgecolor='#ef4444', lw=2, linestyle='--')
    ax.add_patch(bbox2)
    ax.text(0.24, 0.37, "Lesion 2: 94.1%", color='#fca5a5', fontsize=7.5, weight='bold')

    # Right Container: Deep Learning Diagnostic Results
    res_box = mpatches.FancyBboxPatch((0.48, 0.06), 0.50, 0.79, boxstyle="round,pad=0.015",
                                      facecolor='#1e293b', edgecolor='#38bdf8', lw=1.5)
    ax.add_patch(res_box)
    ax.text(0.51, 0.80, "Deep Learning Diagnostic Report", color='#38bdf8', fontsize=11, weight='bold')
    
    diag_lines = [
        ("Identified Pathogen:", "Tomato Early Blight (Alternaria solani)", "#f87171"),
        ("Model Confidence:", "96.4% (Softmax Calibrated)", "#4ade80"),
        ("Infection Severity:", "Moderate (Grade II - Active Sporulation)", "#facc15"),
        ("Affected Organ:", "Lower Foliage (Foliar Necrosis)", "#cbd5e1")
    ]
    for idx, (label, val, val_col) in enumerate(diag_lines):
        y_pos = 0.72 - (idx * 0.07)
        ax.text(0.51, y_pos, label, color='#94a3b8', fontsize=8.8)
        ax.text(0.70, y_pos, val, color=val_col, fontsize=8.8, weight='bold')

    # Scientific Treatment from RAG
    rag_box = mpatches.FancyBboxPatch((0.50, 0.10), 0.46, 0.32, boxstyle="round,pad=0.01",
                                      facecolor='#0f172a', edgecolor='#10b981', lw=1.2)
    ax.add_patch(rag_box)
    ax.text(0.52, 0.38, "Verified ICAR Treatment Protocol:", color='#10b981', fontsize=9.2, weight='bold')
    rag_text = (
        "- Chemical Treatment: Mancozeb 75% WP @ 2.5 g/L\n"
        "  or Chlorothalonil 75% WP @ 2.0 g/L water.\n"
        "- Organic Option: 5% Neem Seed Kernel Extract (NSKE).\n"
        "- Application Warning: Avoid application during peak midday heat.\n"
        "  Pre-harvest Interval (PHI): Maintain 7 days before plucking."
    )
    ax.text(0.52, 0.23, rag_text, color='#f8fafc', fontsize=8.0, linespacing=1.35)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.axis('off')
    plt.tight_layout()

    out = os.path.join(os.getcwd(), "output_screen_3_disease_scanner.png")
    plt.savefig(out, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    print(f"Generated {out}")

def generate_screen_4():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=300)
    fig.patch.set_facecolor('#0f172a')
    ax.set_facecolor('#0f172a')

    # Header
    nav = mpatches.FancyBboxPatch((0.02, 0.88), 0.96, 0.09, boxstyle="round,pad=0.01",
                                  facecolor='#1e293b', edgecolor='#334155', lw=1.2)
    ax.add_patch(nav)
    ax.text(0.05, 0.925, "Commodity Market Intelligence & Mandi Price Forecasting",
            ha='left', va='center', color='#4ade80', fontsize=12, weight='bold')

    # Top Mandi Comparison Table
    t_box = mpatches.FancyBboxPatch((0.02, 0.50), 0.96, 0.35, boxstyle="round,pad=0.015",
                                   facecolor='#1e293b', edgecolor='#334155', lw=1)
    ax.add_patch(t_box)
    ax.text(0.05, 0.80, "Wholesale Market Rates across Nearest Mandis (Haversine Sorted)", color='#f8fafc', fontsize=10.5, weight='bold')

    headers = ["Mandi Name", "Distance (km)", "Current Modal Price", "7-Day Predicted Peak", "Action"]
    x_pos = [0.05, 0.26, 0.45, 0.68, 0.88]
    for h, x in zip(headers, x_pos):
        ax.text(x, 0.73, h, color='#38bdf8', fontsize=8.5, weight='bold')

    rows = [
        ("Warangal Central Mandi", "42.5 km", "Rs 7,450 / Qtl", "Rs 7,620 (Thursday)", "Best Net Profit"),
        ("Guntur Spice & Cotton", "88.2 km", "Rs 7,620 / Qtl", "Rs 7,650 (Wednesday)", "High Transport Cost"),
        ("Khammam Regional Mandi", "64.1 km", "Rs 7,380 / Qtl", "Rs 7,420 (Friday)", "Moderate Volume")
    ]
    for idx, row in enumerate(rows):
        y_val = 0.65 - (idx * 0.06)
        col = '#4ade80' if idx == 0 else '#e2e8f0'
        for cell, x in zip(row, x_pos):
            ax.text(x, y_val, cell, color=col, fontsize=8.2)

    # Bottom Forecast Graph Area
    g_box = mpatches.FancyBboxPatch((0.02, 0.06), 0.96, 0.41, boxstyle="round,pad=0.015",
                                   facecolor='#1e293b', edgecolor='#4ade80', lw=1.2)
    ax.add_patch(g_box)
    ax.text(0.05, 0.42, "PyTorch LSTM 7-Day Forward Price Prediction vs. Historical Modal (Cotton)", color='#4ade80', fontsize=10, weight='bold')

    days = ["Mon", "Tue", "Wed", "Thu (Peak)", "Fri", "Sat", "Sun"]
    prices = [7450, 7480, 7550, 7620, 7580, 7510, 7470]
    
    for idx in range(len(days) - 1):
        x1 = 0.10 + (idx * 0.13)
        x2 = 0.10 + ((idx + 1) * 0.13)
        y1 = 0.15 + (prices[idx] - 7400) / 750.0 * 0.20
        y2 = 0.15 + (prices[idx+1] - 7400) / 750.0 * 0.20
        ax.plot([x1, x2], [y1, y2], 'o-', color='#38bdf8', lw=2.5, markersize=5)
        ax.text(x1, y1 + 0.03, f"Rs {prices[idx]}", ha='center', color='#f8fafc', fontsize=7.8, weight='bold')
        ax.text(x1, 0.10, days[idx], ha='center', color='#94a3b8', fontsize=7.8)

    ax.text(0.10 + (6 * 0.13), 0.15 + (prices[6] - 7400) / 750.0 * 0.20 + 0.03, f"Rs {prices[6]}",
            ha='center', color='#f8fafc', fontsize=7.8, weight='bold')
    ax.text(0.10 + (6 * 0.13), 0.10, days[6], ha='center', color='#94a3b8', fontsize=7.8)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.axis('off')
    plt.tight_layout()

    out = os.path.join(os.getcwd(), "output_screen_4_market_forecast.png")
    plt.savefig(out, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    print(f"Generated {out}")

def generate_screen_5():
    fig, ax = plt.subplots(figsize=(10, 13), dpi=300)
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#ffffff')

    # Border Dossier
    dossier = mpatches.FancyBboxPatch((0.04, 0.03), 0.92, 0.94, boxstyle="square,pad=0.01",
                                      facecolor='#ffffff', edgecolor='#0f172a', lw=2)
    ax.add_patch(dossier)

    # Dossier Header
    hdr = mpatches.Rectangle((0.04, 0.88), 0.92, 0.09, facecolor='#0f172a')
    ax.add_patch(hdr)
    ax.text(0.50, 0.935, "AGRIGEN AI - OFFICIAL AGRONOMIC ADVISORY DOSSIER",
            ha='center', va='center', color='#ffffff', fontsize=11, weight='bold')
    ax.text(0.50, 0.90, "Generated via WeasyPrint Automated Compilation Engine | Verification ID: AGRI-2026-8841",
            ha='center', va='center', color='#94a3b8', fontsize=7.5)

    # Farmer & Field Meta Box
    meta_box = mpatches.Rectangle((0.07, 0.77), 0.86, 0.09, facecolor='#f8fafc', edgecolor='#cbd5e1', lw=1)
    ax.add_patch(meta_box)
    ax.text(0.09, 0.83, "Grower Name: Venkata Ramana", color='#0f172a', fontsize=8.5, weight='bold')
    ax.text(0.09, 0.79, "Location: Razam, Srikakulam, AP", color='#475569', fontsize=8)
    ax.text(0.55, 0.83, "Crop Specimen: Tomato (Foliage Stage)", color='#0f172a', fontsize=8.5, weight='bold')
    ax.text(0.55, 0.79, "Field Coordinates: 18.4500°N, 83.6500°E", color='#475569', fontsize=8)

    # Section 1: Vision Diagnostic
    ax.text(0.07, 0.73, "1. OPTICAL PHYTOSANITARY DIAGNOSTIC SUMMARY", color='#0f172a', fontsize=9.5, weight='bold')
    sec1 = mpatches.Rectangle((0.07, 0.58), 0.86, 0.13, facecolor='#fef2f2', edgecolor='#ef4444', lw=1)
    ax.add_patch(sec1)
    ax.text(0.09, 0.67, "Pathogen Identified: Early Blight (Alternaria solani) | Confidence: 96.4%",
            color='#991b1b', fontsize=8.5, weight='bold')
    ax.text(0.09, 0.61,
            "- Symptom Profile: Concentric dark necrotic rings with surrounding chlorotic halo.\n"
            "- Severity Classification: Grade II (Immediate intervention required to prevent defoliation).",
            color='#374151', fontsize=8, linespacing=1.4)

    # Section 2: Meteorological & Spraying Forecast
    ax.text(0.07, 0.54, "2. METEOROLOGICAL TELEMETRY & SPRAYING SAFETY", color='#0f172a', fontsize=9.5, weight='bold')
    sec2 = mpatches.Rectangle((0.07, 0.40), 0.86, 0.12, facecolor='#eff6ff', edgecolor='#3b82f6', lw=1)
    ax.add_patch(sec2)
    ax.text(0.09, 0.48, "Micro-Climate Alert: Heavy Precipitation Forecasted within 18 Hours (85% Probability)",
            color='#1e40af', fontsize=8.5, weight='bold')
    ax.text(0.09, 0.43,
            "- DO NOT spray today. Rainfall wash-off will neutralize fungicide efficacy and cause chemical runoff.\n"
            "- Recommended Spray Window: Thursday 06:30 AM to 09:30 AM (Wind < 6 km/h, Rain Prob < 15%).",
            color='#374151', fontsize=8, linespacing=1.3)

    # Section 3: Vetted Chemical & Organic Prescription
    ax.text(0.07, 0.36, "3. VETTED CHEMICAL & BIOLOGICAL PRESCRIPTION (ICAR-GROUNDED)", color='#0f172a', fontsize=9.5, weight='bold')
    sec3 = mpatches.Rectangle((0.07, 0.19), 0.86, 0.15, facecolor='#f0fdf4', edgecolor='#16a34a', lw=1)
    ax.add_patch(sec3)
    ax.text(0.09, 0.30, "Prescribed Active Compound: Mancozeb 75% WP or Chlorothalonil 75% WP",
            color='#166534', fontsize=8.5, weight='bold')
    ax.text(0.09, 0.22,
            "- Dilution Rate: 2.0 to 2.5 grams per 1 Liter of water (approx. 500g per acre in 200L water).\n"
            "- Adjuvant Recommendation: Add non-ionic wetting sticker (0.5 ml/L) for superior rainfastness.\n"
            "- Safety Margin (PHI): 7 Days before harvest. Wear protective nitrile gloves during mixing.",
            color='#374151', fontsize=8, linespacing=1.3)

    # Signature & QR
    ax.text(0.07, 0.10, "Digital Signature: Automated AI Agronomy Supervisor Node\nAuthorized via ICAR-FAISS Grounded Vector Pipeline",
            color='#64748b', fontsize=7.5)
    ax.text(0.70, 0.10, "Verified & Issued By:\nAgriGen AI Cloud Gateway",
            color='#0f172a', fontsize=7.5, weight='bold')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    plt.axis('off')
    plt.tight_layout()

    out = os.path.join(os.getcwd(), "output_screen_5_pdf_report.png")
    plt.savefig(out, dpi=300, facecolor=fig.get_facecolor(), bbox_inches='tight')
    plt.close()
    print(f"Generated {out}")

if __name__ == '__main__':
    generate_screen_1()
    generate_screen_2()
    generate_screen_3()
    generate_screen_4()
    generate_screen_5()
