#!/usr/bin/env python3
"""
Generate publication-quality SVG figures for Xcelerate FC documentation.
Follows academic engineering style: off-white background, dark navy text,
restrained blue (#2563EB / #3B82F6) and amber (#D97706 / #F59E0B) accents,
Inter typography and IBM Plex Mono for numbers.
"""

from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent.parent / "assets" / "figures"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def generate_model_evolution_svg():
    """Figure 1: Chronological bar chart showing model progression."""
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 460" width="100%" height="100%" style="background-color: #F8FAFC;">
  <defs>
    <style>
      .title { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 700; font-size: 20px; fill: #0F172A; }
      .subtitle { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 13px; fill: #475569; }
      .axis-label { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 12px; fill: #64748B; font-weight: 500; }
      .tick-text { font-family: 'IBM Plex Mono', 'SF Mono', Menlo, Consolas, monospace; font-size: 11px; fill: #64748B; }
      .bar-val { font-family: 'IBM Plex Mono', 'SF Mono', Menlo, Consolas, monospace; font-size: 14px; font-weight: 600; fill: #0F172A; text-anchor: middle; }
      .bar-title { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 13px; font-weight: 600; fill: #1E293B; text-anchor: middle; }
      .bar-desc { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11px; fill: #64748B; text-anchor: middle; }
      .badge-text { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 10px; font-weight: 700; fill: #FFFFFF; text-anchor: middle; }
      .grid { stroke: #E2E8F0; stroke-width: 1; stroke-dasharray: 4,4; }
      .axis-line { stroke: #CBD5E1; stroke-width: 1.5; }
    </style>
    <linearGradient id="barGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#3B82F6"/>
      <stop offset="100%" stop-color="#2563EB"/>
    </linearGradient>
    <linearGradient id="selectedGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#2563EB"/>
      <stop offset="100%" stop-color="#1D4ED8"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="3" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Title & Subtitle -->
  <text x="50" y="45" class="title">Evolution of Possession Inference Models</text>
  <text x="50" y="68" class="subtitle">Mean external SkillCorner H/A proxy spellF1 across five development matches (higher is better)</text>

  <!-- Y-Axis Grid Lines & Ticks (Scale: 0.30 to 0.52 -> Y range: 360 to 110 => 250px for 0.22 range) -->
  <!-- Formula: y = 360 - ((val - 0.30) / 0.22) * 250 -->
  <line x1="80" y1="360" x2="740" y2="360" class="axis-line" />
  <text x="70" y="364" class="tick-text" text-anchor="end">0.30</text>

  <line x1="80" y1="303" x2="740" y2="303" class="grid" />
  <text x="70" y="307" class="tick-text" text-anchor="end">0.35</text>

  <line x1="80" y1="246" x2="740" y2="246" class="grid" />
  <text x="70" y="250" class="tick-text" text-anchor="end">0.40</text>

  <line x1="80" y1="189" x2="740" y2="189" class="grid" />
  <text x="70" y="193" class="tick-text" text-anchor="end">0.45</text>

  <line x1="80" y1="132" x2="740" y2="132" class="grid" />
  <text x="70" y="136" class="tick-text" text-anchor="end">0.50</text>

  <!-- Y-axis Label -->
  <text x="-240" y="28" class="axis-label" transform="rotate(-90)" text-anchor="middle">External SkillCorner H/A proxy spellF1</text>

  <!-- BARS -->
  <!-- Bar 1: Baseline HMM = 0.4004 -> y = 360 - ((0.4004 - 0.30)/0.22)*250 = 360 - 114.1 = 245.9; height = 114.1 -->
  <g filter="url(#shadow)">
    <rect x="110" y="246" width="120" height="114" rx="6" fill="#93C5FD" />
  </g>
  <text x="170" y="235" class="bar-val">0.4004</text>
  <text x="170" y="385" class="bar-title">M1 · Baseline</text>
  <text x="170" y="403" class="bar-desc">Proximity + HMM</text>

  <!-- Bar 2: switch_strong = 0.4501 -> y = 360 - ((0.4501 - 0.30)/0.22)*250 = 360 - 170.6 = 189.4; height = 170.6 -->
  <g filter="url(#shadow)">
    <rect x="270" y="189" width="120" height="171" rx="6" fill="#60A5FA" />
  </g>
  <text x="330" y="178" class="bar-val">0.4501</text>
  <text x="330" y="385" class="bar-title">M2 · Persistence</text>
  <text x="330" y="403" class="bar-desc">switch_strong</text>
  <!-- Delta badge -->
  <rect x="298" y="198" width="64" height="18" rx="9" fill="#1E293B" opacity="0.85" />
  <text x="330" y="211" class="badge-text">+12.4%</text>

  <!-- Bar 3: control_strong = 0.4815 -> y = 360 - ((0.4815 - 0.30)/0.22)*250 = 360 - 206.2 = 153.8; height = 206.2 -->
  <g filter="url(#shadow)">
    <rect x="430" y="154" width="120" height="206" rx="6" fill="url(#barGrad)" />
  </g>
  <text x="490" y="143" class="bar-val">0.4815</text>
  <text x="490" y="385" class="bar-title">M3 · Ball Control</text>
  <text x="490" y="403" class="bar-desc">control_strong</text>
  <!-- Delta badge -->
  <rect x="458" y="163" width="64" height="18" rx="9" fill="#1E293B" opacity="0.85" />
  <text x="490" y="176" class="badge-text">+20.3%</text>

  <!-- Bar 4: fusion_control_multiscale = 0.4823 -> y = 360 - ((0.4823 - 0.30)/0.22)*250 = 360 - 207.2 = 152.8; height = 207.2 -->
  <g filter="url(#shadow)">
    <rect x="590" y="153" width="120" height="207" rx="6" fill="url(#selectedGrad)" stroke="#1D4ED8" stroke-width="2" />
  </g>
  <text x="650" y="141" class="bar-val" style="fill: #1D4ED8;">0.4823</text>
  <text x="650" y="385" class="bar-title" style="fill: #1D4ED8;">M4 · Selected</text>
  <text x="650" y="403" class="bar-desc">fusion_multiscale</text>
  <!-- Selected Winner Tag -->
  <rect x="605" y="112" width="90" height="20" rx="4" fill="#D97706" />
  <text x="650" y="126" class="badge-text">FINAL MODEL</text>

  <!-- Bottom boundary annotation -->
  <line x1="80" y1="425" x2="740" y2="425" stroke="#E2E8F0" stroke-width="1" />
  <text x="410" y="445" class="axis-label" text-anchor="middle">Experimental progression evaluated on SkillCorner Open Data (Matches 1886347, 1899585, 1925299, 1996435, 2006229)</text>
</svg>
"""
    (OUT_DIR / "model_evolution.svg").write_text(svg, encoding="utf-8")
    print("Created model_evolution.svg")


def generate_external_validation_svg():
    """Figure 2: Match-by-match comparison with reserved holdout."""
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 480" width="100%" height="100%" style="background-color: #F8FAFC;">
  <defs>
    <style>
      .title { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 700; font-size: 20px; fill: #0F172A; }
      .subtitle { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 13px; fill: #475569; }
      .axis-label { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 12px; fill: #64748B; font-weight: 500; }
      .tick-text { font-family: 'IBM Plex Mono', 'SF Mono', Menlo, Consolas, monospace; font-size: 11px; fill: #64748B; }
      .match-id { font-family: 'IBM Plex Mono', 'SF Mono', Menlo, Consolas, monospace; font-size: 12px; font-weight: 600; fill: #1E293B; text-anchor: middle; }
      .val-label { font-family: 'IBM Plex Mono', 'SF Mono', Menlo, Consolas, monospace; font-size: 11px; font-weight: 600; text-anchor: middle; }
      .legend-text { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 12px; font-weight: 600; fill: #1E293B; }
      .holdout-box { fill: #FEF3C7; stroke: #F59E0B; stroke-width: 1.5; stroke-dasharray: 4,4; rx: 8px; }
      .holdout-title { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11px; font-weight: 700; fill: #B45309; text-anchor: middle; }
      .grid { stroke: #E2E8F0; stroke-width: 1; stroke-dasharray: 4,4; }
      .axis-line { stroke: #CBD5E1; stroke-width: 1.5; }
    </style>
    <filter id="dotShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="2" stdDeviation="2" flood-opacity="0.15"/>
    </filter>
  </defs>

  <!-- Title & Subtitle -->
  <text x="50" y="42" class="title">Generalization Across Independent External Matches</text>
  <text x="50" y="65" class="subtitle">SkillCorner H/A proxy spellF1 on five development matches and one reserved external holdout</text>

  <!-- Legend -->
  <g transform="translate(480, 48)">
    <line x1="0" y1="0" x2="24" y2="0" stroke="#3B82F6" stroke-width="2.5" />
    <circle cx="12" cy="0" r="4.5" fill="#3B82F6" />
    <text x="32" y="4" class="legend-text">switch_strong (Mean: 0.4501)</text>

    <line x1="0" y1="20" x2="24" y2="20" stroke="#059669" stroke-width="2.5" />
    <circle cx="12" cy="20" r="4.5" fill="#059669" />
    <text x="32" y="24" class="legend-text">fusion_control_multiscale (Mean: 0.4823)</text>
  </g>

  <!-- Plot Area: X from 90 to 810; Y from 110 (0.55) to 370 (0.38) -->
  <!-- Y scale: 0.38 to 0.55 -> delta = 0.17; height = 260px; y = 370 - ((val - 0.38) / 0.17) * 260 -->
  <!-- 0.38 -> 370; 0.40 -> 339.4; 0.45 -> 262.9; 0.50 -> 186.5; 0.55 -> 110.0 -->

  <!-- Y-Axis Grid & Ticks -->
  <line x1="80" y1="370" x2="810" y2="370" class="axis-line" />
  <text x="70" y="374" class="tick-text" text-anchor="end">0.38</text>

  <line x1="80" y1="339" x2="810" y2="339" class="grid" />
  <text x="70" y="343" class="tick-text" text-anchor="end">0.40</text>

  <line x1="80" y1="293" x2="810" y2="293" class="grid" />
  <text x="70" y="297" class="tick-text" text-anchor="end">0.43</text>

  <line x1="80" y1="247" x2="810" y2="247" class="grid" />
  <text x="70" y="251" class="tick-text" text-anchor="end">0.46</text>

  <line x1="80" y1="202" x2="810" y2="202" class="grid" />
  <text x="70" y="206" class="tick-text" text-anchor="end">0.49</text>

  <line x1="80" y1="156" x2="810" y2="156" class="grid" />
  <text x="70" y="160" class="tick-text" text-anchor="end">0.52</text>

  <line x1="80" y1="110" x2="810" y2="110" class="grid" />
  <text x="70" y="114" class="tick-text" text-anchor="end">0.55</text>

  <!-- Y-axis Label -->
  <text x="-240" y="25" class="axis-label" transform="rotate(-90)" text-anchor="middle">SkillCorner H/A proxy spellF1</text>

  <!-- Reserved Holdout Shading Box -->
  <rect x="670" y="95" width="130" height="295" class="holdout-box" />
  <text x="735" y="120" class="holdout-title">RESERVED HOLDOUT</text>

  <!-- X-coordinates:
       Match 1 (1886347): x = 140
       Match 2 (1899585): x = 250
       Match 3 (1925299): x = 360
       Match 4 (1996435): x = 470
       Match 5 (2006229): x = 580
       Holdout (2017461): x = 735
  -->

  <!-- Separation line between Dev and Holdout -->
  <line x1="645" y1="95" x2="645" y2="390" stroke="#94A3B8" stroke-width="1.5" stroke-dasharray="6,6" />
  <text x="360" y="440" class="axis-label" text-anchor="middle">Five Development Matches (Leave-One-Out Cross-Validation)</text>
  <text x="735" y="440" class="axis-label" text-anchor="middle" style="fill: #B45309; font-weight: 600;">Unseen Test Match</text>

  <!-- switch_strong points:
       1886347: 0.447 -> y = 370 - ((0.447-0.38)/0.17)*260 = 267.5
       1899585: 0.479 -> y = 370 - ((0.479-0.38)/0.17)*260 = 218.6
       1925299: 0.443 -> y = 370 - ((0.443-0.38)/0.17)*260 = 273.6
       1996435: 0.436 -> y = 370 - ((0.436-0.38)/0.17)*260 = 284.4
       2006229: 0.445 -> y = 370 - ((0.445-0.38)/0.17)*260 = 270.6
  -->
  <polyline points="140,268 250,219 360,274 470,284 580,271" fill="none" stroke="#93C5FD" stroke-width="2.5" />

  <!-- fusion_control_multiscale points:
       1886347: 0.509 -> y = 370 - ((0.509-0.38)/0.17)*260 = 172.8
       1899585: 0.489 -> y = 370 - ((0.489-0.38)/0.17)*260 = 203.3
       1925299: 0.476 -> y = 370 - ((0.476-0.38)/0.17)*260 = 223.2
       1996435: 0.474 -> y = 370 - ((0.474-0.38)/0.17)*260 = 226.2
       2006229: 0.463 -> y = 370 - ((0.463-0.38)/0.17)*260 = 243.1
  -->
  <polyline points="140,173 250,203 360,223 470,226 580,243" fill="none" stroke="#059669" stroke-width="3" />

  <!-- Data Points switch_strong -->
  <g fill="#3B82F6">
    <circle cx="140" cy="268" r="5" filter="url(#dotShadow)"/>
    <text x="140" y="285" class="val-label" fill="#2563EB">0.447</text>

    <circle cx="250" cy="219" r="5" filter="url(#dotShadow)"/>
    <text x="250" y="236" class="val-label" fill="#2563EB">0.479</text>

    <circle cx="360" cy="274" r="5" filter="url(#dotShadow)"/>
    <text x="360" y="291" class="val-label" fill="#2563EB">0.443</text>

    <circle cx="470" cy="284" r="5" filter="url(#dotShadow)"/>
    <text x="470" y="301" class="val-label" fill="#2563EB">0.436</text>

    <circle cx="580" cy="271" r="5" filter="url(#dotShadow)"/>
    <text x="580" y="288" class="val-label" fill="#2563EB">0.445</text>
  </g>

  <!-- Data Points fusion_control_multiscale -->
  <g fill="#059669">
    <circle cx="140" cy="173" r="6" filter="url(#dotShadow)"/>
    <text x="140" y="160" class="val-label" fill="#047857">0.509</text>

    <circle cx="250" cy="203" r="6" filter="url(#dotShadow)"/>
    <text x="250" y="190" class="val-label" fill="#047857">0.489</text>

    <circle cx="360" cy="223" r="6" filter="url(#dotShadow)"/>
    <text x="360" y="210" class="val-label" fill="#047857">0.476</text>

    <circle cx="470" cy="226" r="6" filter="url(#dotShadow)"/>
    <text x="470" y="213" class="val-label" fill="#047857">0.474</text>

    <circle cx="580" cy="243" r="6" filter="url(#dotShadow)"/>
    <text x="580" y="230" class="val-label" fill="#047857">0.463</text>
  </g>

  <!-- Holdout Data Point 2017461 = 0.4078 -> y = 370 - ((0.4078-0.38)/0.17)*260 = 327.5 -->
  <g>
    <circle cx="735" cy="328" r="8" fill="#D97706" stroke="#FFFFFF" stroke-width="2.5" filter="url(#dotShadow)"/>
    <text x="735" y="315" class="val-label" fill="#B45309" style="font-size: 13px; font-weight: 700;">0.4078</text>
    <rect x="680" y="345" width="110" height="24" rx="4" fill="#B45309" />
    <text x="735" y="361" class="val-label" fill="#FFFFFF">Reserved Test</text>
  </g>

  <!-- Match ID X-Labels -->
  <text x="140" y="405" class="match-id">1886347</text>
  <text x="250" y="405" class="match-id">1899585</text>
  <text x="360" y="405" class="match-id">1925299</text>
  <text x="470" y="405" class="match-id">1996435</text>
  <text x="580" y="405" class="match-id">2006229</text>
  <text x="735" y="405" class="match-id" style="fill: #B45309;">2017461</text>
</svg>
"""
    (OUT_DIR / "external_validation.svg").write_text(svg, encoding="utf-8")
    print("Created external_validation.svg")


def generate_football_possession_schematic_svg():
    """Figure 3: Conceptual football schematic showing why nearest != controller."""
    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 480" width="100%" height="100%" style="background-color: #F8FAFC;">
  <defs>
    <style>
      .title { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 700; font-size: 20px; fill: #0F172A; }
      .subtitle { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 13px; fill: #475569; }
      .pitch-line { stroke: #D9EAE3; stroke-width: 1.5; fill: none; }
      .pitch-line-faint { stroke: #7EA39B; stroke-opacity: 0.25; stroke-width: 1; fill: none; }
      .label-box-title { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 700; font-size: 13px; }
      .label-box-desc { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 11px; fill: #475569; }
      .player-text { font-family: 'IBM Plex Mono', 'SF Mono', monospace; font-weight: 700; font-size: 11px; text-anchor: middle; }
      .field-text { font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-size: 12px; font-weight: 600; fill: #FFFFFF; }
      .mono-metric { font-family: 'IBM Plex Mono', 'SF Mono', monospace; font-size: 11px; font-weight: 600; }
    </style>
    <filter id="cardShadow" x="-2%" y="-2%" width="104%" height="106%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-opacity="0.08"/>
    </filter>
  </defs>

  <!-- Title & Subtitle -->
  <text x="40" y="38" class="title">Football-Aware Possession Modeling: Control vs Proximity</text>
  <text x="40" y="60" class="subtitle">Why nearest-player geometry fails during passes, and how last-controller memory preserves possession</text>

  <!-- Pitch Container -->
  <g transform="translate(40, 80)" filter="url(#cardShadow)">
    <!-- Pitch Turf -->
    <rect x="0" y="0" width="780" height="250" rx="12" fill="#143B33" stroke="#0F2922" stroke-width="2"/>

    <!-- Subtle field zones -->
    <line x1="156" y1="5" x2="156" y2="245" class="pitch-line-faint" />
    <line x1="312" y1="5" x2="312" y2="245" class="pitch-line-faint" />
    <line x1="468" y1="5" x2="468" y2="245" class="pitch-line-faint" />
    <line x1="624" y1="5" x2="624" y2="245" class="pitch-line-faint" />

    <!-- Outer boundary & Halfway line -->
    <rect x="20" y="15" width="740" height="220" rx="3" class="pitch-line" />
    <line x1="390" y1="15" x2="390" y2="235" class="pitch-line" />
    <circle cx="390" cy="125" r="45" class="pitch-line" />
    <circle cx="390" cy="125" r="3" fill="#D9EAE3" />

    <!-- Penalty Area left & right -->
    <rect x="20" y="65" width="85" height="120" class="pitch-line" />
    <rect x="675" y="65" width="85" height="120" class="pitch-line" />

    <!-- Pass Trajectory arc from H1 to H2 -->
    <path d="M 170 140 Q 340 40 480 120" fill="none" stroke="#38BDF8" stroke-width="3" stroke-dasharray="6,6" />
    <!-- Trajectory Direction Arrow -->
    <polygon points="485,124 472,112 476,128" fill="#38BDF8" />

    <!-- Control radius around H1 (passer) -->
    <circle cx="170" cy="140" r="36" fill="#38BDF8" fill-opacity="0.12" stroke="#38BDF8" stroke-width="1.2" stroke-dasharray="3,3" />
    <text x="170" y="190" class="field-text" text-anchor="middle" style="font-size: 10px; fill: #7DD3FC;">Control Radius (1.8m)</text>

    <!-- Proximity threshold circle around ball -->
    <circle cx="410" cy="98" r="48" fill="#FFFFFF" fill-opacity="0.06" stroke="#CBD5E1" stroke-width="1.2" stroke-dasharray="2,2"/>
    <line x1="410" y1="98" x2="445" y2="82" stroke="#F59E0B" stroke-width="2" stroke-dasharray="3,3"/>
    <text x="440" y="74" class="field-text" style="font-size: 10px; fill: #FCD34D;">d = 1.1m (closest)</text>

    <!-- Ball in Flight -->
    <circle cx="410" cy="98" r="8" fill="#FFFFFF" stroke="#0F172A" stroke-width="2" />
    <circle cx="410" cy="98" r="3" fill="#0F172A" />

    <!-- Team H Players (Home - Blue) -->
    <!-- Player H1: Passer (Origin) -->
    <circle cx="170" cy="140" r="14" fill="#2563EB" stroke="#FFFFFF" stroke-width="2.5" />
    <text x="170" y="144" class="player-text" fill="#FFFFFF">H1</text>
    <text x="170" y="116" class="field-text" text-anchor="middle">Passer (Last Controller)</text>

    <!-- Player H2: Intended Receiver -->
    <circle cx="560" cy="160" r="14" fill="#2563EB" stroke="#FFFFFF" stroke-width="2.5" />
    <text x="560" y="164" class="player-text" fill="#FFFFFF">H2</text>
    <text x="560" y="190" class="field-text" text-anchor="middle">Intended Receiver</text>

    <!-- Another teammate H3 -->
    <circle cx="280" cy="65" r="14" fill="#2563EB" stroke="#FFFFFF" stroke-width="2.5" />
    <text x="280" y="69" class="player-text" fill="#FFFFFF">H3</text>

    <!-- Team A Players (Away - Amber/Orange) -->
    <!-- Defender A1: Physically nearest to ball during pass, but NOT in control -->
    <circle cx="445" cy="82" r="14" fill="#D97706" stroke="#FFFFFF" stroke-width="2.5" />
    <text x="445" y="86" class="player-text" fill="#FFFFFF">A1</text>
    <text x="450" y="52" class="field-text" text-anchor="middle" style="fill: #FDE68A;">Defender A1</text>
    <text x="450" y="64" class="field-text" text-anchor="middle" style="font-size: 9px; fill: #FDE68A;">(Nearest to ball in flight)</text>

    <!-- Other defenders A2, A3 -->
    <circle cx="520" cy="75" r="14" fill="#D97706" stroke="#FFFFFF" stroke-width="2.5" />
    <text x="520" y="79" class="player-text" fill="#FFFFFF">A2</text>

    <circle cx="620" cy="115" r="14" fill="#D97706" stroke="#FFFFFF" stroke-width="2.5" />
    <text x="620" y="119" class="player-text" fill="#FFFFFF">A3</text>

    <!-- In-pitch status banners -->
    <rect x="30" y="25" width="230" height="24" rx="4" fill="#0F172A" opacity="0.85" />
    <text x="40" y="41" class="field-text" style="font-size: 11px;">PASS IN PROGRESS · Team H → Team H</text>
  </g>

  <!-- Explanatory Comparison Cards (Bottom) -->
  <!-- Card 1: Naive Geometric Approach -->
  <g transform="translate(40, 345)" filter="url(#cardShadow)">
    <rect x="0" y="0" width="375" height="115" rx="8" fill="#FFFFFF" stroke="#EF4444" stroke-width="1.5" />
    <rect x="15" y="12" width="22" height="22" rx="11" fill="#FEE2E2" />
    <text x="26" y="27" font-family="'Inter', sans-serif" font-weight="700" font-size="13" fill="#DC2626" text-anchor="middle">✕</text>
    <text x="46" y="28" class="label-box-title" fill="#991B1B">Naive Proximity Model (Nearest Player)</text>

    <text x="15" y="56" class="label-box-desc">Decision: <tspan class="mono-metric" fill="#DC2626">Possession = A (Turnover)</tspan></text>
    <text x="15" y="76" class="label-box-desc">Because Defender A1 happens to be 1.1m from the ball while</text>
    <text x="15" y="94" class="label-box-desc">it travels in the air, a spurious turnover is flagged every pass.</text>
  </g>

  <!-- Card 2: Football-Aware Approach (Our Model) -->
  <g transform="translate(445, 345)" filter="url(#cardShadow)">
    <rect x="0" y="0" width="375" height="115" rx="8" fill="#FFFFFF" stroke="#10B981" stroke-width="1.5" />
    <rect x="15" y="12" width="22" height="22" rx="11" fill="#D1FAE5" />
    <text x="26" y="27" font-family="'Inter', sans-serif" font-weight="700" font-size="13" fill="#059669" text-anchor="middle">✓</text>
    <text x="46" y="28" class="label-box-title" fill="#065F46">Our Football-Aware Model (Last-Controller Memory)</text>

    <text x="15" y="56" class="label-box-desc">Decision: <tspan class="mono-metric" fill="#059669">Possession = H (Continuous)</tspan></text>
    <text x="15" y="76" class="label-box-desc">Maintains H1 memory (1.8m radius, 10s expiry) across flight.</text>
    <text x="15" y="94" class="label-box-desc">Requires sustained control evidence before granting a turnover.</text>
  </g>
</svg>
"""
    (OUT_DIR / "football_possession_schematic.svg").write_text(svg, encoding="utf-8")
    print("Created football_possession_schematic.svg")


if __name__ == "__main__":
    generate_model_evolution_svg()
    generate_external_validation_svg()
    generate_football_possession_schematic_svg()
    print("All 3 SVG figures generated successfully in", OUT_DIR)
