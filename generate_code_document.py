import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    """Sets background shading of a table cell in docx."""
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    """Sets inner margins for a table cell."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for margin_name, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{margin_name}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def create_code_document():
    doc = docx.Document()

    # Page Margins (0.75 inch for more code width)
    sections = doc.sections
    for s in sections:
        s.top_margin = Inches(0.75)
        s.bottom_margin = Inches(0.75)
        s.left_margin = Inches(0.75)
        s.right_margin = Inches(0.75)

    # Base Normal Style
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(10)
    normal_style.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)

    # Document Header / Title
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_title = title.add_run("AgriGen AI — Complete Source Code Documentation\n")
    run_title.font.name = 'Calibri'
    run_title.font.size = Pt(22)
    run_title.font.bold = True
    run_title.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    sub = doc.add_paragraph()
    sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run_sub = sub.add_run("Intelligent Multi-Agent Smart Farming Ecosystem\nAcademic Review & Complete Technical Implementation Reference")
    run_sub.font.size = Pt(12)
    run_sub.font.italic = True
    run_sub.font.color.rgb = RGBColor(0x02, 0x84, 0xC7)

    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_meta = p_meta.add_run("Architecture: React 19 • FastAPI • LangGraph • PyTorch • FAISS RAG • Whisper Speech\nDate: Academic Review 2026 | Total Scope: End-to-End Production Modules")
    r_meta.font.size = Pt(9.5)
    r_meta.font.color.rgb = RGBColor(0x64, 0x74, 0x8B)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # Table of Contents
    p_toc_head = doc.add_paragraph()
    r_toc = p_toc_head.add_run("Table of Source Code Modules Included")
    r_toc.font.size = Pt(14)
    r_toc.font.bold = True
    r_toc.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)

    code_files = [
        ("Section 1: Application Entrypoint & Lifecycle", "backend/main.py", "FastAPI App, Middleware, Static Mounts, Lifespan Handler"),
        ("Section 2: System Configuration & Security", "backend/config/settings.py", "Pydantic BaseSettings, API Key Validation, Environment Variables"),
        ("Section 3: Database Engine & Relational Models", "backend/database/database.py", "SQLAlchemy Engine, SessionLocal, Declarative Base"),
        ("Section 4: Relational Entity ORM Schemas", "backend/database/models.py", "User, Farm, DiagnosticRecord, Telemetry Models"),
        ("Section 5: API Gateway & Streaming Hub", "backend/api/v1/orchestrator.py", "REST Routes, SSE Token Streaming, Whisper Transcription, gTTS"),
        ("Section 6: Farm Telemetry & System Monitoring", "backend/api/v1/telemetry.py", "System Health, Environmental Telemetry, Sensor Feeds"),
        ("Section 7: LangGraph Multi-Agent Supervisor DAG", "backend/core/agents/workflow.py", "AgentState Schema, Supervisor Router, Open-Meteo & Soil Tools"),
        ("Section 8: Deep Vision Pathology Diagnostic Service", "backend/services/vision_service.py", "PyTorch EfficientNet-B0 Paddy Disease Ensemble Classifier"),
        ("Section 9: Geolocation & Mandi Indexing Engine", "backend/services/geo_service.py", "Haversine Distance, Mandi DB, Soil Texture, Crop Calendar"),
        ("Section 10: Deep Learning Training Pipeline", "backend/ml/train_disease_classifier.py", "PyTorch Training Loop, Adam Optimizer, CrossEntropyLoss"),
        ("Section 11: Dataset Augmentation & Preprocessing", "backend/ml/dataset_pipeline.py", "Torchvision Transforms, Balance Sampling, Train/Val Split"),
        ("Section 12: Client Presentation Dashboard", "frontend/src/App.jsx", "React 19 UI, Voice Audio Capture, Chart.js Visualizations"),
        ("Section 13: Responsive Styling & Design System", "frontend/src/App.css", "Modern Dark-Theme CSS Tokens, Glassmorphism, Micro-animations")
    ]

    table = doc.add_table(rows=1, cols=3)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = "Module / Section"
    hdr_cells[1].text = "File Path in Project"
    hdr_cells[2].text = "Key Functional Responsibility"
    for c in hdr_cells:
        set_cell_background(c, "1E293B")
        for p in c.paragraphs:
            for r in p.runs:
                r.font.name = 'Calibri'
                r.font.size = Pt(9.5)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    for sec_name, file_rel, desc in code_files:
        row_cells = table.add_row().cells
        row_cells[0].text = sec_name
        row_cells[1].text = file_rel
        row_cells[2].text = desc
        for idx, c in enumerate(row_cells):
            set_cell_background(c, "F8FAFC" if idx % 2 == 0 else "FFFFFF")
            for p in c.paragraphs:
                for r in p.runs:
                    r.font.name = 'Calibri'
                    r.font.size = Pt(8.5)

    doc.add_page_break()

    # Now add each source file in full detail
    base_dir = os.path.dirname(os.path.abspath(__file__))

    for idx, (sec_name, file_rel, desc) in enumerate(code_files, start=1):
        file_path = os.path.join(base_dir, file_rel.replace('/', os.sep))
        
        # Section Header
        h1 = doc.add_paragraph()
        r_h1 = h1.add_run(f"{sec_name}\n")
        r_h1.font.name = 'Calibri'
        r_h1.font.size = Pt(15)
        r_h1.font.bold = True
        r_h1.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

        meta_p = doc.add_paragraph()
        r_path = meta_p.add_run(f"Source File: {file_rel}\n")
        r_path.font.size = Pt(10)
        r_path.font.bold = True
        r_path.font.color.rgb = RGBColor(0x02, 0x84, 0xC7)

        r_desc = meta_p.add_run(f"Description: {desc}")
        r_desc.font.size = Pt(9.5)
        r_desc.font.italic = True
        r_desc.font.color.rgb = RGBColor(0x47, 0x55, 0x69)

        if not os.path.exists(file_path):
            doc.add_paragraph(f"[Notice: File {file_rel} not found in workspace]")
            doc.add_page_break()
            continue

        try:
            with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                lines = f.readlines()
        except Exception as e:
            lines = [f"Error reading file: {e}"]

        total_lines = len(lines)
        meta_p.add_run(f" | Total Lines: {total_lines}")

        # Code block inside a shaded 1-cell table for neat Word rendering
        code_table = doc.add_table(rows=1, cols=1)
        code_table.alignment = WD_TABLE_ALIGNMENT.CENTER
        code_cell = code_table.rows[0].cells[0]
        set_cell_background(code_cell, "F8FAFC")
        set_cell_margins(code_cell, top=120, bottom=120, left=150, right=150)

        # Populate lines with line numbers
        p_code = code_cell.paragraphs[0]
        p_code.paragraph_format.line_spacing = Pt(11)
        p_code.paragraph_format.space_before = Pt(0)
        p_code.paragraph_format.space_after = Pt(0)

        # For large files (like App.jsx or App.css which are 1700+ lines),
        # include the most critical 350-450 lines so the document is perfectly 25-30 pages.
        limit_lines = lines
        is_truncated = False
        if total_lines > 450:
            limit_lines = lines[:450]
            is_truncated = True

        code_text_chunks = []
        for l_idx, line in enumerate(limit_lines, start=1):
            code_text_chunks.append(f"{l_idx:04d}:  {line.rstrip()}")

        if is_truncated:
            code_text_chunks.append(f"\n... [Remaining {total_lines - 450} lines preserved in repository at {file_rel}] ...")

        full_code_str = "\n".join(code_text_chunks)
        r_code = p_code.add_run(full_code_str)
        r_code.font.name = 'Consolas'
        r_code.font.size = Pt(8.0)
        r_code.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

        doc.add_paragraph().paragraph_format.space_after = Pt(12)
        doc.add_page_break()

    out_docx = os.path.join(base_dir, "AgriGen_AI_Complete_Source_Code_Documentation.docx")
    doc.save(out_docx)
    print(f"Generated {out_docx} successfully! Total modules: {len(code_files)}")

if __name__ == '__main__':
    create_code_document()
