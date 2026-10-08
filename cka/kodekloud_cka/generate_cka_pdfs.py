#!/usr/bin/env python3
"""
Scrapes all 135 KodeKloud CKA documentation pages and renders high-quality
PDF study guides per module as well as one comprehensive consolidated PDF.
"""

import os
import re
import sys
import urllib.request
import urllib.parse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

import markdown
from weasyprint import HTML

BASE_DIR = Path(__file__).resolve().parent
MD_INDEX = BASE_DIR / "cka_complete_notes.md"
RAW_PAGES_DIR = BASE_DIR / "raw_pages"
PDF_OUT_DIR = BASE_DIR / "pdf_guides"

RAW_PAGES_DIR.mkdir(parents=True, exist_ok=True)
PDF_OUT_DIR.mkdir(parents=True, exist_ok=True)

CSS_STYLING = """
@page {
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
    @top-left {
        content: "KodeKloud CKA Notes";
        font-family: 'Inter', system-ui, sans-serif;
        font-size: 8pt;
        color: #64748b;
    }
    @top-right {
        content: string(heading);
        font-family: 'Inter', system-ui, sans-serif;
        font-size: 8pt;
        color: #64748b;
    }
    @bottom-center {
        content: "Page " counter(page) " of " counter(pages);
        font-family: 'Inter', system-ui, sans-serif;
        font-size: 8pt;
        color: #64748b;
    }
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.6;
    color: #1e293b;
    background-color: #ffffff;
}

h1 {
    font-size: 20pt;
    color: #0f172a;
    border-bottom: 2px solid #3b82f6;
    padding-bottom: 6px;
    margin-top: 0;
    margin-bottom: 16px;
    string-set: heading content();
    page-break-after: avoid;
}

h2 {
    font-size: 14pt;
    color: #1e3a8a;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 4px;
    margin-top: 24px;
    margin-bottom: 12px;
    page-break-after: avoid;
}

h3 {
    font-size: 11pt;
    color: #334155;
    margin-top: 18px;
    margin-bottom: 8px;
    page-break-after: avoid;
}

p {
    margin-top: 0;
    margin-bottom: 10px;
    text-align: justify;
}

ul, ol {
    margin-top: 0;
    margin-bottom: 12px;
    padding-left: 20px;
}

li {
    margin-bottom: 4px;
}

code {
    font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
    font-size: 8.5pt;
    background-color: #f1f5f9;
    color: #0f172a;
    padding: 2px 4px;
    border-radius: 4px;
    border: 1px solid #e2e8f0;
}

pre {
    background-color: #0f172a;
    color: #f8fafc;
    padding: 12px;
    border-radius: 6px;
    font-size: 8pt;
    line-height: 1.45;
    overflow-x: auto;
    page-break-inside: avoid;
    margin-bottom: 12px;
}

pre code {
    background-color: transparent;
    color: inherit;
    padding: 0;
    border: none;
}

blockquote {
    border-left: 4px solid #3b82f6;
    background-color: #eff6ff;
    margin: 12px 0;
    padding: 8px 14px;
    color: #1e3a8a;
    border-radius: 0 4px 4px 0;
    page-break-inside: avoid;
}

img {
    max-width: 100% !important;
    height: auto !important;
    display: block;
    margin: 14px auto;
    border-radius: 6px;
    border: 1px solid #e2e8f0;
    box-sizing: border-box;
    page-break-inside: avoid;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 14px;
    font-size: 9pt;
    page-break-inside: avoid;
}

th, td {
    border: 1px solid #cbd5e1;
    padding: 6px 10px;
    text-align: left;
}

th {
    background-color: #f8fafc;
    font-weight: 600;
    color: #0f172a;
}

tr:nth-child(even) {
    background-color: #f8fafc;
}

.module-header {
    text-align: center;
    padding: 30px 0 20px 0;
    margin-bottom: 30px;
    border-bottom: 3px solid #3b82f6;
}

.module-header h1 {
    border: none;
    font-size: 26pt;
    color: #1e3a8a;
    margin-bottom: 8px;
}

.module-header .subtitle {
    font-size: 12pt;
    color: #64748b;
    font-weight: 500;
}

.page-break {
    page-break-after: always;
}
"""

def parse_index():
    sections = {}
    current_section = "General"
    
    with open(MD_INDEX, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("### "):
                current_section = line.replace("### ", "").strip()
                if current_section not in sections:
                    sections[current_section] = []
            elif line.startswith("- ["):
                m = re.match(r"- \[(.*?)\]\((.*?)\)(?:: (.*))?", line)
                if m:
                    title = m.group(1)
                    url = m.group(2)
                    desc = m.group(3) or ""
                    sections[current_section].append({
                        "title": title,
                        "url": url,
                        "desc": desc,
                        "section": current_section
                    })
    return sections

def download_page(item):
    url = item["url"]
    sec = re.sub(r'[^a-zA-Z0-9_-]', '_', item["section"])
    t = re.sub(r'[^a-zA-Z0-9_-]', '_', item["title"])
    filename = f"{sec}__{t}.md"
    filepath = RAW_PAGES_DIR / filename
    
    if filepath.exists() and filepath.stat().st_size > 50:
        item["local_md"] = filepath
        return item

    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read().decode('utf-8', errors='ignore')
            with open(filepath, "w", encoding="utf-8") as out:
                out.write(content)
            item["local_md"] = filepath
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        item["local_md"] = None
    return item

def clean_markdown(md_text, title):
    # Remove frontmatter if present
    if md_text.startswith("---"):
        parts = md_text.split("---", 2)
        if len(parts) >= 3:
            md_text = parts[2]
            
    # Clean doc link badges or noise
    md_text = re.sub(r'\[Skip to main content\].*?\n', '', md_text)
    md_text = re.sub(r'Was this page helpful\?.*', '', md_text, flags=re.DOTALL)
    
    # Ensure top header is title
    if not re.search(r'^#\s+', md_text, flags=re.MULTILINE):
        md_text = f"# {title}\n\n" + md_text
        
    return md_text

def build_module_pdf(section_name, items):
    sec_slug = re.sub(r'[^a-zA-Z0-9_-]', '_', section_name).lower()
    pdf_path = PDF_OUT_DIR / f"CKA_{sec_slug}.pdf"
    
    full_html_body = f"""
    <div class="module-header">
        <h1>CKA: {section_name}</h1>
        <div class="subtitle">KodeKloud Complete Study Notes — Certified Kubernetes Administrator</div>
    </div>
    """
    
    for i, item in enumerate(items):
        if not item.get("local_md") or not item["local_md"].exists():
            continue
        with open(item["local_md"], "r", encoding="utf-8") as f:
            raw = f.read()
        cleaned = clean_markdown(raw, item["title"])
        rendered_html = markdown.markdown(cleaned, extensions=['extra', 'tables', 'fenced_code', 'codehilite'])
        
        full_html_body += f"<div class='lesson-content'>{rendered_html}</div>"
        if i < len(items) - 1:
            full_html_body += "<div class='page-break'></div>"

    doc = f"""<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>{CSS_STYLING}</style>
    </head>
    <body>
        {full_html_body}
    </body>
    </html>
    """
    
    HTML(string=doc).write_pdf(target=str(pdf_path))
    print(f"Generated: {pdf_path}")
    return pdf_path

def build_consolidated_pdf(sections):
    pdf_path = PDF_OUT_DIR / "CKA_Complete_KodeKloud_Notes.pdf"
    full_html_body = f"""
    <div class="module-header" style="padding-top: 150px;">
        <h1 style="font-size: 32pt;">Certified Kubernetes Administrator (CKA)</h1>
        <div class="subtitle" style="font-size: 16pt; margin-top: 15px;">Complete Official KodeKloud Documentation & Study Guide</div>
        <p style="margin-top: 40px; color: #64748b; font-size: 11pt;">Compiled for Mickey (Hailemichael Tehka Meresa)</p>
    </div>
    <div class="page-break"></div>
    """
    
    for section_name, items in sections.items():
        full_html_body += f"""
        <div class="module-header">
            <h1>Section: {section_name}</h1>
        </div>
        """
        for i, item in enumerate(items):
            if not item.get("local_md") or not item["local_md"].exists():
                continue
            with open(item["local_md"], "r", encoding="utf-8") as f:
                raw = f.read()
            cleaned = clean_markdown(raw, item["title"])
            rendered_html = markdown.markdown(cleaned, extensions=['extra', 'tables', 'fenced_code', 'codehilite'])
            full_html_body += f"<div class='lesson-content'>{rendered_html}</div><div class='page-break'></div>"

    doc = f"""<!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>{CSS_STYLING}</style>
    </head>
    <body>
        {full_html_body}
    </body>
    </html>
    """
    
    print("Generating Consolidated Complete CKA PDF...")
    HTML(string=doc).write_pdf(target=str(pdf_path))
    print(f"Generated Consolidated PDF: {pdf_path}")
    return pdf_path

def main():
    print("Parsing index...")
    sections = parse_index()
    all_items = []
    for s_items in sections.values():
        all_items.extend(s_items)
        
    print(f"Found {len(all_items)} documentation pages across {len(sections)} sections.")
    print("Downloading markdown files concurrently...")
    with ThreadPoolExecutor(max_workers=10) as executor:
        list(executor.map(download_page, all_items))
        
    print("Generating Section PDFs...")
    for section_name, items in sections.items():
        build_module_pdf(section_name, items)
        
    build_consolidated_pdf(sections)
    print("Done! All PDFs generated successfully.")

if __name__ == "__main__":
    main()
