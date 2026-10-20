"""
SVG Diagram Helpers for CKA & LFCS Study Guides
Generates crisp, responsive, high-resolution vector diagrams with modern dark/accent themes.
"""

def wrap_svg(width: int, height: int, content: str, title: str = "") -> str:
    """Wraps SVG content with universal definitions, gradients, markers, and container."""
    title_element = ""
    if title:
        title_element = f"""
        <rect x="15" y="10" width="{width - 30}" height="32" rx="7" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
        <circle cx="34" cy="26" r="5" fill="#38bdf8"/>
        <text x="48" y="31" fill="#f8fafc" font-size="12.5" font-weight="bold" font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif">{title}</text>
        """

    return f"""<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" class="diagram-svg">
  <defs>
    <linearGradient id="bgDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#090d16"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="cardDark" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7"/>
      <stop offset="100%" stop-color="#0369a1"/>
    </linearGradient>
    <linearGradient id="greenGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#047857"/>
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#d97706"/>
      <stop offset="100%" stop-color="#b45309"/>
    </linearGradient>
    <linearGradient id="purpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#6d28d9"/>
    </linearGradient>
    <linearGradient id="roseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#e11d48"/>
      <stop offset="100%" stop-color="#be123c"/>
    </linearGradient>
    <linearGradient id="indigoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4f46e5"/>
      <stop offset="100%" stop-color="#3730a3"/>
    </linearGradient>
    <linearGradient id="cyanGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0891b2"/>
      <stop offset="100%" stop-color="#0e7490"/>
    </linearGradient>

    <!-- Arrow Markers -->
    <marker id="arrowSky" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#38bdf8" />
    </marker>
    <marker id="arrowGreen" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#34d399" />
    </marker>
    <marker id="arrowAmber" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#fbbf24" />
    </marker>
    <marker id="arrowPurple" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#c084fc" />
    </marker>
    <marker id="arrowRose" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#f43f5e" />
    </marker>
    <marker id="arrowWhite" markerWidth="9" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 9 3, 0 6" fill="#ffffff" />
    </marker>

    <!-- Drop Shadow Filter -->
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="2" dy="3" stdDeviation="3" flood-opacity="0.28"/>
    </filter>
  </defs>

  <!-- Base Canvas -->
  <rect x="0" y="0" width="{width}" height="{height}" rx="12" fill="url(#bgDark)" stroke="#1e293b" stroke-width="1.5"/>

  {title_element}

  {content}
</svg>"""

def card(x: int, y: int, w: int, h: int, title: str, subtitle: str = "", fill_grad: str = "cardDark", stroke: str = "#475569", title_color: str = "#ffffff") -> str:
    """Renders a standard container card."""
    sub_element = ""
    if subtitle:
        sub_element = f'<text x="{x + 14}" y="{y + 40}" fill="#94a3b8" font-size="9.5" font-family="-apple-system, sans-serif">{subtitle}</text>'
    
    return f"""
    <g filter="url(#shadow)">
      <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="url(#{fill_grad})" stroke="{stroke}" stroke-width="1.5"/>
      <rect x="{x}" y="{y}" width="{w}" height="28" rx="9" fill="{stroke}" opacity="0.18"/>
      <text x="{x + 14}" y="{y + 20}" fill="{title_color}" font-size="12" font-weight="bold" font-family="-apple-system, sans-serif">{title}</text>
      {sub_element}
    </g>
    """

def code_box(x: int, y: int, w: int, h: int, text: str, border_color: str = "#334155") -> str:
    """Renders a dark terminal-style code snippet."""
    lines = text.strip().split("\n")
    lines_svg = ""
    for i, l in enumerate(lines):
        lines_svg += f'<text x="{x + 10}" y="{y + 16 + i * 14}" fill="#38bdf8" font-size="8.8" font-family="JetBrainsMono Nerd Font, monospace">{l}</text>'
    
    return f"""
    <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="#030712" stroke="{border_color}" stroke-width="1"/>
    {lines_svg}
    """

def arrow(x1: int, y1: int, x2: int, y2: int, marker: str = "arrowSky", stroke: str = "#38bdf8", stroke_width: int = 2, label: str = "") -> str:
    """Renders a directional line with arrow marker and label."""
    label_svg = ""
    if label:
        mx = (x1 + x2) // 2
        my = (y1 + y2) // 2 - 5
        label_svg = f'<text x="{mx}" y="{my}" fill="{stroke}" font-size="8.8" font-weight="bold" text-anchor="middle" font-family="-apple-system, sans-serif">{label}</text>'
    return f"""
    <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{stroke_width}" marker-end="url(#{marker})"/>
    {label_svg}
    """
