# -*- coding: utf-8 -*-
"""
Asset and Data generator for Mohamed Mahmoud Dahab Showrooms website.
Generates:
1. High quality dual phone mockup SVGs for each model showing both colors.
2. Single color phone mockup SVGs for interactive color switching.
3. SVG illustrations for home & electrical appliances (TV, Refrigerator, Washing Machine, AC, Microwave, Cooker).
4. SVG illustrations for accessories (Powerbank, Earbuds, Smartwatch).
5. Comprehensive data.js file with all 23 phones, 5 accessories, and 10 electrical appliances.
"""

import os
import json

# Ensure directories
os.makedirs('assets/images/phones', exist_ok=True)
os.makedirs('assets/images/appliances', exist_ok=True)
os.makedirs('assets/images/accessories', exist_ok=True)
os.makedirs('assets/images/brand', exist_ok=True)

def generate_dual_phone_svg(c1_hex, c2_hex, model_label):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 360" width="100%" height="100%">
  <defs>
    <radialGradient id="glow_{abs(hash(model_label))}" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#d4af37" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#0b0f19" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="c1_{abs(hash(model_label))}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{c1_hex}"/>
      <stop offset="100%" stop-color="{c1_hex}" stop-opacity="0.8"/>
    </linearGradient>
    <linearGradient id="c2_{abs(hash(model_label))}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{c2_hex}"/>
      <stop offset="100%" stop-color="{c2_hex}" stop-opacity="0.8"/>
    </linearGradient>
    <filter id="shadow_{abs(hash(model_label))}" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="14" flood-color="#000000" flood-opacity="0.65"/>
    </filter>
    <linearGradient id="shine" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.4"/>
      <stop offset="35%" stop-color="#ffffff" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.25"/>
    </linearGradient>
    <linearGradient id="gold_border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffd700"/>
      <stop offset="50%" stop-color="#b8860b"/>
      <stop offset="100%" stop-color="#d4af37"/>
    </linearGradient>
  </defs>

  <!-- Ambient Glow -->
  <circle cx="170" cy="180" r="150" fill="url(#glow_{abs(hash(model_label))})"/>

  <!-- Phone 2 (Back / Color 2, angled right) -->
  <g transform="translate(145, 30) rotate(11 65 140)" filter="url(#shadow_{abs(hash(model_label))})">
    <rect x="0" y="0" width="135" height="275" rx="26" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
    <rect x="3" y="3" width="129" height="269" rx="23" fill="url(#c2_{abs(hash(model_label))})"/>
    <rect x="3" y="3" width="129" height="269" rx="23" fill="url(#shine)"/>
    
    <!-- Camera Island -->
    <rect x="12" y="14" width="48" height="74" rx="14" fill="#090d16" fill-opacity="0.8" stroke="#cbd5e1" stroke-width="1" stroke-opacity="0.4"/>
    <circle cx="36" cy="35" r="14" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
    <circle cx="36" cy="35" r="8" fill="#020617"/>
    <circle cx="34" cy="33" r="3" fill="#38bdf8" fill-opacity="0.85"/>
    <circle cx="36" cy="68" r="12" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
    <circle cx="36" cy="68" r="6" fill="#020617"/>
    <circle cx="34" cy="66" r="2" fill="#38bdf8" fill-opacity="0.85"/>
    <circle cx="21" cy="78" r="4" fill="#fef08a"/>
  </g>

  <!-- Phone 1 (Front / Color 1, angled left) -->
  <g transform="translate(45, 45) rotate(-6 65 140)" filter="url(#shadow_{abs(hash(model_label))})">
    <rect x="0" y="0" width="135" height="275" rx="26" fill="#1e293b" stroke="url(#gold_border)" stroke-width="1.5"/>
    <rect x="3" y="3" width="129" height="269" rx="23" fill="url(#c1_{abs(hash(model_label))})"/>
    <rect x="3" y="3" width="129" height="269" rx="23" fill="url(#shine)"/>
    
    <!-- Camera Island -->
    <rect x="12" y="14" width="48" height="76" rx="15" fill="#090d16" fill-opacity="0.8" stroke="#e2e8f0" stroke-width="1" stroke-opacity="0.5"/>
    <circle cx="36" cy="35" r="14" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
    <circle cx="36" cy="35" r="8" fill="#020617"/>
    <circle cx="34" cy="33" r="3" fill="#38bdf8" fill-opacity="0.85"/>
    <circle cx="36" cy="68" r="12" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
    <circle cx="36" cy="68" r="6" fill="#020617"/>
    <circle cx="34" cy="66" r="2" fill="#38bdf8" fill-opacity="0.85"/>
    <circle cx="21" cy="79" r="4" fill="#fef08a"/>

    <!-- Subtle Dahab Signature -->
    <text x="67" y="242" font-family="'Cairo', sans-serif" font-size="8.5" font-weight="700" fill="#ffffff" fill-opacity="0.75" text-anchor="middle" letter-spacing="1">DAHAB EDITION</text>
  </g>
</svg>'''
    return svg

def generate_single_phone_svg(c_hex, model_label):
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 360" width="100%" height="100%">
  <defs>
    <radialGradient id="sglow_{abs(hash(c_hex + model_label))}" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="{c_hex}" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#0b0f19" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="sc_{abs(hash(c_hex + model_label))}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{c_hex}"/>
      <stop offset="100%" stop-color="{c_hex}" stop-opacity="0.82"/>
    </linearGradient>
    <filter id="sshadow_{abs(hash(c_hex + model_label))}" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="12" stdDeviation="15" flood-color="#000000" flood-opacity="0.65"/>
    </filter>
    <linearGradient id="sshine" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.42"/>
      <stop offset="35%" stop-color="#ffffff" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#000000" stop-opacity="0.25"/>
    </linearGradient>
  </defs>

  <circle cx="150" cy="180" r="140" fill="url(#sglow_{abs(hash(c_hex + model_label))})"/>

  <g transform="translate(80, 35)" filter="url(#sshadow_{abs(hash(c_hex + model_label))})">
    <rect x="0" y="0" width="140" height="285" rx="28" fill="#1e293b" stroke="#d4af37" stroke-width="1.5"/>
    <rect x="3" y="3" width="134" height="279" rx="25" fill="url(#sc_{abs(hash(c_hex + model_label))})"/>
    <rect x="3" y="3" width="134" height="279" rx="25" fill="url(#sshine)"/>
    
    <!-- Camera Island -->
    <rect x="14" y="15" width="52" height="82" rx="16" fill="#090d16" fill-opacity="0.85" stroke="#cbd5e1" stroke-width="1" stroke-opacity="0.4"/>
    <circle cx="40" cy="38" r="15" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
    <circle cx="40" cy="38" r="8" fill="#020617"/>
    <circle cx="38" cy="36" r="3" fill="#38bdf8" fill-opacity="0.9"/>
    <circle cx="40" cy="72" r="13" fill="#1e293b" stroke="#94a3b8" stroke-width="1.5"/>
    <circle cx="40" cy="72" r="7" fill="#020617"/>
    <circle cx="38" cy="70" r="2.5" fill="#38bdf8" fill-opacity="0.9"/>
    <circle cx="23" cy="85" r="4" fill="#fef08a"/>

    <text x="70" y="248" font-family="'Cairo', sans-serif" font-size="9" font-weight="700" fill="#ffffff" fill-opacity="0.8" text-anchor="middle" letter-spacing="1">DAHAB 2026</text>
  </g>
</svg>'''
    return svg

# Appliances SVGs
appliances_svgs = {
    "tv_samsung_55": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 280" width="100%" height="100%">
  <defs>
    <radialGradient id="tvglow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#0b0f19" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="tvscreen" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="50%" stop-color="#1e1b4b"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
  </defs>
  <circle cx="170" cy="140" r="130" fill="url(#tvglow)"/>
  <!-- Stand -->
  <path d="M130 240 L210 240 L190 220 L150 220 Z" fill="#475569"/>
  <!-- Bezel -->
  <rect x="25" y="30" width="290" height="190" rx="6" fill="#0f172a" stroke="#d4af37" stroke-width="2"/>
  <!-- Screen with vibrant 4K visual -->
  <rect x="30" y="35" width="280" height="180" rx="4" fill="url(#tvscreen)"/>
  <!-- Dynamic landscape glow -->
  <circle cx="240" cy="80" r="35" fill="#f59e0b" fill-opacity="0.85"/>
  <path d="M30 190 Q90 120 160 170 T310 160 L310 215 L30 215 Z" fill="#312e81" fill-opacity="0.85"/>
  <path d="M30 195 Q110 150 200 185 T310 180 L310 215 L30 215 Z" fill="#0369a1" fill-opacity="0.75"/>
  <text x="170" y="115" font-family="'Cairo', sans-serif" font-size="18" font-weight="900" fill="#ffffff" text-anchor="middle" letter-spacing="2">CRYSTAL 4K UHD</text>
  <text x="170" y="135" font-family="'Cairo', sans-serif" font-size="11" font-weight="bold" fill="#fde047" text-anchor="middle">SAMSUNG SMART 55"</text>
</svg>''',

    "tv_lg_oled_65": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 280" width="100%" height="100%">
  <defs>
    <radialGradient id="lgglow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#a855f7" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#0b0f19" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="oledscreen" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#000000"/>
      <stop offset="40%" stop-color="#180026"/>
      <stop offset="100%" stop-color="#4c0519"/>
    </linearGradient>
  </defs>
  <circle cx="170" cy="140" r="130" fill="url(#lgglow)"/>
  <!-- Stand -->
  <rect x="110" y="235" width="120" height="8" rx="4" fill="#94a3b8"/>
  <rect x="162" y="215" width="16" height="20" fill="#475569"/>
  <!-- Bezel -->
  <rect x="20" y="25" width="300" height="190" rx="4" fill="#0a0a0a" stroke="#a855f7" stroke-width="1.5"/>
  <rect x="23" y="28" width="294" height="184" rx="2" fill="url(#oledscreen)"/>
  <!-- Vivid OLED colors -->
  <circle cx="100" cy="100" r="45" fill="#ec4899" fill-opacity="0.7" filter="blur(8px)"/>
  <circle cx="210" cy="110" r="50" fill="#8b5cf6" fill-opacity="0.7" filter="blur(8px)"/>
  <text x="170" y="115" font-family="'Cairo', sans-serif" font-size="20" font-weight="900" fill="#ffffff" text-anchor="middle" letter-spacing="3">OLED CINEMA</text>
  <text x="170" y="138" font-family="'Cairo', sans-serif" font-size="11" font-weight="bold" fill="#f472b6" text-anchor="middle">LG 65" 4K SELF-LIT PIXELS</text>
</svg>''',

    "fridge_sharp": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 340" width="100%" height="100%">
  <defs>
    <radialGradient id="fridgeglow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#0b0f19" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="inox" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#94a3b8"/>
      <stop offset="50%" stop-color="#cbd5e1"/>
      <stop offset="100%" stop-color="#64748b"/>
    </linearGradient>
  </defs>
  <circle cx="140" cy="170" r="130" fill="url(#fridgeglow)"/>
  <g transform="translate(60, 20)">
    <!-- Main Body -->
    <rect x="0" y="0" width="160" height="295" rx="14" fill="url(#inox)" stroke="#475569" stroke-width="2"/>
    <!-- Top Door (Freezer) -->
    <rect x="4" y="4" width="152" height="95" rx="10" fill="url(#inox)"/>
    <line x1="4" y1="102" x2="156" y2="102" stroke="#334155" stroke-width="3"/>
    <!-- Bottom Door (Fridge) -->
    <rect x="4" y="105" width="152" height="182" rx="10" fill="url(#inox)"/>
    <!-- Digital Display -->
    <rect x="60" y="45" width="40" height="18" rx="4" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
    <text x="80" y="58" font-family="monospace" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">-18°C</text>
    <!-- Handles (Recessed) -->
    <rect x="14" y="60" width="6" height="30" rx="3" fill="#1e293b"/>
    <rect x="14" y="120" width="6" height="60" rx="3" fill="#1e293b"/>
    <!-- Inverter & Plasmacluster Logo -->
    <circle cx="130" cy="24" r="8" fill="#0284c7"/>
    <text x="130" y="27" font-family="'Cairo', sans-serif" font-size="6" font-weight="bold" fill="#ffffff" text-anchor="middle">J-TECH</text>
    <text x="80" y="270" font-family="'Cairo', sans-serif" font-size="9" font-weight="900" fill="#1e293b" text-anchor="middle">SHARP INVERTER</text>
  </g>
</svg>''',

    "fridge_lg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 340" width="100%" height="100%">
  <defs>
    <radialGradient id="lgfglow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#d4af37" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#0b0f19" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="blacksteel" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="50%" stop-color="#334155"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>
  <circle cx="140" cy="170" r="130" fill="url(#lgfglow)"/>
  <g transform="translate(60, 20)">
    <rect x="0" y="0" width="160" height="295" rx="14" fill="url(#blacksteel)" stroke="#d4af37" stroke-width="1.5"/>
    <!-- InstaView Glass Window Door -->
    <rect x="85" y="12" width="65" height="135" rx="8" fill="#0f172a" stroke="#d4af37" stroke-width="1"/>
    <rect x="90" y="17" width="55" height="125" rx="6" fill="#1e1b4b" fill-opacity="0.8"/>
    <!-- Water Dispenser -->
    <rect x="14" y="50" width="40" height="60" rx="6" fill="#0f172a" stroke="#64748b" stroke-width="1"/>
    <path d="M28 85 Q34 70 40 85" stroke="#38bdf8" stroke-width="2" fill="none"/>
    <circle cx="34" cy="95" r="4" fill="#38bdf8"/>
    <!-- Bottom Freezer Section -->
    <line x1="4" y1="165" x2="156" y2="165" stroke="#475569" stroke-width="2"/>
    <rect x="35" y="175" width="90" height="10" rx="3" fill="#64748b"/>
    <rect x="35" y="230" width="90" height="10" rx="3" fill="#64748b"/>
    <text x="80" y="280" font-family="'Cairo', sans-serif" font-size="9" font-weight="900" fill="#d4af37" text-anchor="middle">LG INSTAVIEW 506L</text>
  </g>
</svg>''',

    "washer_lg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 320" width="100%" height="100%">
  <defs>
    <radialGradient id="washglow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#0b0f19" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="drumshine" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0284c7" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#1e1b4b" stop-opacity="0.9"/>
    </linearGradient>
  </defs>
  <circle cx="140" cy="160" r="130" fill="url(#washglow)"/>
  <g transform="translate(50, 20)">
    <!-- Washing machine body -->
    <rect x="0" y="0" width="180" height="270" rx="14" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
    <!-- Control Panel -->
    <rect x="8" y="8" width="164" height="45" rx="8" fill="#0f172a"/>
    <!-- Detergent drawer -->
    <rect x="16" y="16" width="45" height="28" rx="4" fill="#334155"/>
    <!-- Knob -->
    <circle cx="90" cy="30" r="14" fill="#475569" stroke="#d4af37" stroke-width="2"/>
    <!-- Digital display -->
    <rect x="116" y="16" width="48" height="28" rx="4" fill="#020617"/>
    <text x="140" y="34" font-family="monospace" font-size="11" font-weight="bold" fill="#38bdf8" text-anchor="middle">0:59</text>
    <!-- Big Glass Door -->
    <circle cx="90" cy="155" r="70" fill="#0f172a" stroke="#d4af37" stroke-width="3"/>
    <circle cx="90" cy="155" r="54" fill="url(#drumshine)"/>
    <!-- Chrome Drum Ring -->
    <circle cx="90" cy="155" r="38" fill="#0f172a" fill-opacity="0.6" stroke="#94a3b8" stroke-width="2" stroke-dasharray="8 6"/>
    <circle cx="90" cy="155" r="16" fill="#38bdf8" fill-opacity="0.4"/>
    <text x="90" y="250" font-family="'Cairo', sans-serif" font-size="9" font-weight="bold" fill="#e2e8f0" text-anchor="middle">LG STEAM 9KG INVERTER</text>
  </g>
</svg>''',

    "dishwasher_beko": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 280 320" width="100%" height="100%">
  <defs>
    <radialGradient id="dishglow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#10b981" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#0b0f19" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="140" cy="160" r="130" fill="url(#dishglow)"/>
  <g transform="translate(50, 20)">
    <rect x="0" y="0" width="180" height="270" rx="12" fill="#cbd5e1" stroke="#475569" stroke-width="2"/>
    <rect x="8" y="8" width="164" height="40" rx="6" fill="#1e293b"/>
    <!-- LED Indicators -->
    <circle cx="25" cy="28" r="4" fill="#10b981"/>
    <circle cx="38" cy="28" r="4" fill="#38bdf8"/>
    <circle cx="51" cy="28" r="4" fill="#fbbf24"/>
    <!-- Small Display -->
    <rect x="110" y="16" width="50" height="24" rx="4" fill="#020617"/>
    <text x="135" y="32" font-family="monospace" font-size="10" font-weight="bold" fill="#10b981" text-anchor="middle">ECO P1</text>
    <!-- Handle -->
    <rect x="30" y="60" width="120" height="12" rx="4" fill="#475569"/>
    <!-- Front Panel -->
    <rect x="10" y="80" width="160" height="175" rx="8" fill="#94a3b8" stroke="#64748b" stroke-width="1.5"/>
    <text x="90" y="240" font-family="'Cairo', sans-serif" font-size="9" font-weight="900" fill="#0f172a" text-anchor="middle">BEKO 14 PERSONS INOX</text>
  </g>
</svg>''',

    "ac_sharp_15": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 260" width="100%" height="100%">
  <defs>
    <radialGradient id="acglow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#0b0f19" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="acwhite" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="50%" stop-color="#f1f5f9"/>
      <stop offset="100%" stop-color="#e2e8f0"/>
    </linearGradient>
  </defs>
  <circle cx="170" cy="130" r="120" fill="url(#acglow)"/>
  <g transform="translate(30, 60)">
    <!-- AC Indoor Unit -->
    <rect x="0" y="0" width="280" height="95" rx="14" fill="url(#acwhite)" stroke="#cbd5e1" stroke-width="2"/>
    <!-- Air vent flap -->
    <rect x="15" y="70" width="250" height="18" rx="6" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1"/>
    <!-- Digital Hidden Display -->
    <circle cx="230" cy="38" r="16" fill="#0f172a"/>
    <text x="230" y="44" font-family="monospace" font-size="14" font-weight="bold" fill="#38bdf8" text-anchor="middle">22°</text>
    <!-- Cold Air Breeze Effect -->
    <path d="M40 98 Q80 135 140 120 T240 145" stroke="#38bdf8" stroke-width="3" stroke-linecap="round" fill="none" opacity="0.8"/>
    <path d="M60 110 Q110 150 180 135 T270 160" stroke="#7dd3fc" stroke-width="2" stroke-linecap="round" fill="none" opacity="0.6"/>
    <!-- Sharp Logo & Plasmacluster -->
    <circle cx="50" cy="38" r="12" fill="#0284c7"/>
    <text x="50" y="42" font-family="'Cairo', sans-serif" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">PCI</text>
    <text x="140" y="42" font-family="'Cairo', sans-serif" font-size="11" font-weight="900" fill="#1e293b" text-anchor="middle">SHARP INVERTER 1.5 HP</text>
  </g>
</svg>''',

    "ac_carrier_225": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 340 260" width="100%" height="100%">
  <defs>
    <radialGradient id="carrierglow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#d4af37" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#0b0f19" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="170" cy="130" r="120" fill="url(#carrierglow)"/>
  <g transform="translate(30, 60)">
    <rect x="0" y="0" width="280" height="98" rx="14" fill="#f8fafc" stroke="#d4af37" stroke-width="1.5"/>
    <!-- Gold Trim -->
    <line x1="0" y1="20" x2="280" y2="20" stroke="#d4af37" stroke-width="2"/>
    <rect x="15" y="72" width="250" height="18" rx="6" fill="#e2e8f0"/>
    <circle cx="235" cy="48" r="16" fill="#0f172a"/>
    <text x="235" y="54" font-family="monospace" font-size="14" font-weight="bold" fill="#eab308" text-anchor="middle">20°</text>
    <!-- Air stream -->
    <path d="M40 100 Q100 140 170 125 T250 150" stroke="#38bdf8" stroke-width="2.5" fill="none" opacity="0.8"/>
    <text x="135" y="48" font-family="'Cairo', sans-serif" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">CARRIER OPTIMAX 2.25 HP</text>
  </g>
</svg>''',

    "cooker_fresh_90": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300" width="100%" height="100%">
  <defs>
    <radialGradient id="cookerglow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#f97316" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#0b0f19" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="150" cy="150" r="130" fill="url(#cookerglow)"/>
  <g transform="translate(45, 25)">
    <!-- Stove Body -->
    <rect x="0" y="0" width="210" height="245" rx="12" fill="#334155" stroke="#cbd5e1" stroke-width="2"/>
    <!-- Burner Surface (Cast Iron) -->
    <rect x="6" y="6" width="198" height="45" rx="6" fill="#0f172a"/>
    <!-- 5 Burners -->
    <circle cx="35" cy="22" r="10" fill="#1e293b" stroke="#f97316" stroke-width="1.5"/>
    <circle cx="85" cy="22" r="10" fill="#1e293b" stroke="#f97316" stroke-width="1.5"/>
    <circle cx="105" cy="30" r="12" fill="#1e293b" stroke="#ea580c" stroke-width="2"/>
    <circle cx="130" cy="22" r="10" fill="#1e293b" stroke="#f97316" stroke-width="1.5"/>
    <circle cx="175" cy="22" r="10" fill="#1e293b" stroke="#f97316" stroke-width="1.5"/>
    <!-- Knob Row -->
    <rect x="6" y="56" width="198" height="28" rx="4" fill="#1e293b"/>
    <circle cx="30" cy="70" r="7" fill="#64748b"/>
    <circle cx="60" cy="70" r="7" fill="#64748b"/>
    <circle cx="90" cy="70" r="7" fill="#64748b"/>
    <circle cx="120" cy="70" r="7" fill="#64748b"/>
    <circle cx="150" cy="70" r="7" fill="#64748b"/>
    <circle cx="180" cy="70" r="7" fill="#64748b"/>
    <!-- Oven Mirror Door -->
    <rect x="12" y="90" width="186" height="142" rx="8" fill="#0f172a" stroke="#d4af37" stroke-width="1.5"/>
    <rect x="30" y="105" width="150" height="85" rx="6" fill="#451a03" fill-opacity="0.6"/>
    <!-- Oven Handle -->
    <rect x="40" y="98" width="130" height="8" rx="3" fill="#cbd5e1"/>
    <text x="105" y="150" font-family="'Cairo', sans-serif" font-size="10" font-weight="900" fill="#fdba74" text-anchor="middle">FRESH JUMBO 90x60</text>
  </g>
</svg>''',

    "microwave_tornado": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 260" width="100%" height="100%">
  <defs>
    <radialGradient id="microglow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.25"/>
      <stop offset="100%" stop-color="#0b0f19" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="160" cy="130" r="120" fill="url(#microglow)"/>
  <g transform="translate(30, 40)">
    <rect x="0" y="0" width="260" height="170" rx="14" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
    <!-- Glass Door -->
    <rect x="12" y="14" width="165" height="142" rx="8" fill="#090d16" stroke="#64748b" stroke-width="1.5"/>
    <rect x="22" y="24" width="145" height="122" rx="6" fill="#1e1b4b" fill-opacity="0.7"/>
    <!-- Turntable Plate reflection -->
    <ellipse cx="94" cy="115" rx="55" ry="16" fill="#38bdf8" fill-opacity="0.4"/>
    <!-- Control Panel -->
    <rect x="186" y="14" width="62" height="142" rx="6" fill="#0f172a"/>
    <!-- LED Clock -->
    <rect x="194" y="22" width="46" height="24" rx="4" fill="#020617"/>
    <text x="217" y="38" font-family="monospace" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">12:30</text>
    <!-- Buttons -->
    <circle cx="206" cy="62" r="5" fill="#475569"/>
    <circle cx="228" cy="62" r="5" fill="#475569"/>
    <circle cx="206" cy="78" r="5" fill="#475569"/>
    <circle cx="228" cy="78" r="5" fill="#475569"/>
    <!-- Dial -->
    <circle cx="217" cy="110" r="14" fill="#64748b" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="130" y="195" font-family="'Cairo', sans-serif" font-size="9" font-weight="900" fill="#e2e8f0" text-anchor="middle">TORNADO 36L GRILL DIGITAL</text>
  </g>
</svg>'''
}

# Accessories SVGs
accessories_svgs = {
    "powerbank_realme": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 280" width="100%" height="100%">
  <defs>
    <radialGradient id="pbglow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#eab308" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#0b0f19" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="130" cy="140" r="110" fill="url(#pbglow)"/>
  <g transform="translate(65, 30)">
    <!-- Powerbank body -->
    <rect x="0" y="0" width="130" height="210" rx="20" fill="#18181b" stroke="#eab308" stroke-width="2"/>
    <!-- Ports top -->
    <rect x="30" y="8" width="22" height="6" rx="2" fill="#09090b"/>
    <rect x="65" y="7" width="35" height="8" rx="2" fill="#09090b" stroke="#eab308" stroke-width="0.8"/>
    <!-- Battery Level Indicator LEDs -->
    <circle cx="45" cy="50" r="3" fill="#eab308"/>
    <circle cx="58" cy="50" r="3" fill="#eab308"/>
    <circle cx="71" cy="50" r="3" fill="#eab308"/>
    <circle cx="84" cy="50" r="3" fill="#71717a"/>
    <!-- Texture ridges -->
    <path d="M15 80 L115 80 M15 100 L115 100 M15 120 L115 120" stroke="#27272a" stroke-width="2"/>
    <text x="65" y="165" font-family="'Cairo', sans-serif" font-size="16" font-weight="900" fill="#eab308" text-anchor="middle">realme</text>
    <text x="65" y="185" font-family="'Cairo', sans-serif" font-size="9" font-weight="bold" fill="#a1a1aa" text-anchor="middle">20000mAh DART</text>
  </g>
</svg>''',

    "buds_realme": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 280" width="100%" height="100%">
  <defs>
    <radialGradient id="budsglow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#0b0f19" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="130" cy="140" r="110" fill="url(#budsglow)"/>
  <g transform="translate(55, 45)">
    <!-- Case -->
    <ellipse cx="75" cy="85" rx="65" ry="50" fill="#09090b" stroke="#38bdf8" stroke-width="2"/>
    <!-- Lid Cut line -->
    <path d="M12 85 Q75 60 138 85" stroke="#38bdf8" stroke-width="1.5" fill="none"/>
    <!-- LED Dot -->
    <circle cx="75" cy="105" r="3.5" fill="#38bdf8"/>
    <!-- Logo -->
    <text x="75" y="55" font-family="'Cairo', sans-serif" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">realme</text>
    <text x="75" y="165" font-family="'Cairo', sans-serif" font-size="10" font-weight="bold" fill="#38bdf8" text-anchor="middle">BUDS WIRELESS ANC</text>
  </g>
</svg>''',

    "watch_realme": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 280" width="100%" height="100%">
  <defs>
    <radialGradient id="watchglow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#d4af37" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#0b0f19" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <circle cx="130" cy="140" r="110" fill="url(#watchglow)"/>
  <g transform="translate(60, 20)">
    <!-- Strap top -->
    <rect x="42" y="0" width="56" height="55" rx="8" fill="#27272a"/>
    <!-- Strap bottom -->
    <rect x="42" y="175" width="56" height="55" rx="8" fill="#27272a"/>
    <!-- Watch Case -->
    <rect x="18" y="45" width="104" height="135" rx="28" fill="#18181b" stroke="#d4af37" stroke-width="2.5"/>
    <!-- Crown Button -->
    <rect x="122" y="80" width="6" height="25" rx="3" fill="#d4af37"/>
    <!-- AMOLED Screen -->
    <rect x="25" y="52" width="90" height="121" rx="22" fill="#000000"/>
    <!-- Dial UI -->
    <circle cx="70" cy="100" r="35" stroke="#38bdf8" stroke-width="3" stroke-dasharray="160 50" fill="none"/>
    <text x="70" y="98" font-family="'Cairo', sans-serif" font-size="18" font-weight="900" fill="#ffffff" text-anchor="middle">10:45</text>
    <text x="70" y="115" font-family="'Cairo', sans-serif" font-size="9" font-weight="bold" fill="#fde047" text-anchor="middle">138 BPM • 5K STEPS</text>
    <text x="70" y="142" font-family="'Cairo', sans-serif" font-size="8" font-weight="bold" fill="#38bdf8" text-anchor="middle">REALME WATCH 5</text>
  </g>
</svg>'''
}

# Write appliances SVGs
for k, svg in appliances_svgs.items():
    with open(f'assets/images/appliances/{k}.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

# Write accessories SVGs
for k, svg in accessories_svgs.items():
    with open(f'assets/images/accessories/{k}.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

print('Appliances and accessories SVGs written.')
