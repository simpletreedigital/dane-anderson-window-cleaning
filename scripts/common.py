import re, os

DOMAIN = "https://daneandersonwindowcleaning.com"
PHONE_DISPLAY = "(831) 224-3387"
PHONE_TEL = "8312243387"
BIZ = "Dane Anderson Window Cleaning"

WAVE_TOP = '''<div class="wave-divider"><svg viewBox="0 0 1200 60" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg"><path d="M0,30 C200,70 400,0 600,25 C800,50 1000,10 1200,30 L1200,60 L0,60 Z" fill="{fill}"></path></svg></div>'''

def wave(fill):
    return WAVE_TOP.format(fill=fill)

HEAD_FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">'''

def breadcrumb(items):
    # items: list of (label, url or None for current)
    parts = []
    for i, (label, url) in enumerate(items):
        if url:
            parts.append(f'<a href="{url}">{label}</a>')
        else:
            parts.append(f'<span>{label}</span>')
        if i < len(items) - 1:
            parts.append('<span>/</span>')
    return '<div class="breadcrumb">' + ''.join(parts) + '</div>'

def breadcrumb_schema(items, urlbase=DOMAIN):
    els = []
    for i, (label, url) in enumerate(items):
        full = urlbase + url if url and url != '/' else (urlbase + '/' if url == '/' else urlbase)
        if url is None:
            full = None
        els.append({"@type": "ListItem", "position": i + 1, "name": label, **({"item": full} if full else {})})
    return els

def mobile_call_bar():
    return f'''<div class="mobile-call-bar active"><a href="tel:{PHONE_TEL}">&#128222; Call Now: {PHONE_DISPLAY}</a></div>'''

def faq_block(faqs, heading="Frequently Asked Questions", htag="h2"):
    items = []
    for q, a in faqs:
        items.append(f'<div class="faq-item"><button class="faq-q">{q} <span class="faq-icon">+</span></button><div class="faq-a">{a}</div></div>')
    return f'<{htag} style="margin:40px 0 18px">{heading}</{htag}>\n<div class="faq-list">' + ''.join(items) + '</div>'

def faq_schema(faqs):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in faqs
        ]
    }

def strip_tags(s):
    return re.sub('<[^<]+?>', '', s)

def case_study(title, situation, approach, outcome):
    return f'''<div class="case-study">
<span class="cs-label">Client Case Study</span>
<h3>{title}</h3>
<div class="cs-grid">
<div class="cs-col"><h4>The Situation</h4><p>{situation}</p></div>
<div class="cs-col"><h4>Our Approach</h4><p>{approach}</p></div>
<div class="cs-col"><h4>The Outcome</h4><p>{outcome}</p></div>
</div>
<p class="cs-disclaimer">Client name changed. Results vary based on individual circumstances. Prior results do not guarantee similar outcomes.</p>
</div>'''

FAQ_SCRIPT = '''<script>
document.querySelectorAll('.faq-q').forEach(btn=>{
 btn.addEventListener('click',()=>{
 const item=btn.closest('.faq-item');
 const wasOpen=item.classList.contains('open');
 document.querySelectorAll('.faq-item').forEach(i=>i.classList.remove('open'));
 if(!wasOpen)item.classList.add('open');
 });
});
</script>'''

def page_shell(title, description, canonical_path, schema_graph, body, extra_head="", body_class="", show_call_bar=False, og_type="website"):
    canonical = DOMAIN + canonical_path
    import json
    schema_json = json.dumps({"@context": "https://schema.org", "@graph": schema_graph}, separators=(',', ':'))
    call_bar = mobile_call_bar() if show_call_bar else ""
    bc = ' class="has-call-bar"' if show_call_bar else ""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/png" href="/images/favicon.png">
{HEAD_FONTS}
<meta name="robots" content="index, follow">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="{og_type}">
<script type="application/ld+json">{schema_json}</script>
{extra_head}
<script src="/includes/nav-footer-loader.js"></script>
</head>
<body{bc}>
<main>
{body}
</main>
{call_bar}
{FAQ_SCRIPT}
</body>
</html>
'''

def write_page(path, html):
    full = os.path.join("/Volumes/samsung/_WEB/ClaudeCode/clients/dane-anderson-window-cleaning/site", path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(html)
    wc = len(re.sub('<[^<]+?>', ' ', html).split())
    print(f"{path}  (~{wc} words incl markup-adjacent text)")

LOCAL_BUSINESS_BASE = {
    "@type": "LocalBusiness",
    "@id": DOMAIN + "/#business",
    "name": BIZ,
    "url": DOMAIN + "/",
    "telephone": PHONE_DISPLAY,
    "image": DOMAIN + "/images/hero/homepage-hero-coastal-home.jpg",
    "priceRange": "$$",
    "areaServed": [
        {"@type": "City", "name": "Santa Cruz, CA"},
        {"@type": "City", "name": "Capitola, CA"},
        {"@type": "City", "name": "Aptos, CA"},
        {"@type": "City", "name": "Watsonville, CA"},
        {"@type": "City", "name": "Monterey, CA"},
        {"@type": "City", "name": "Pacific Grove, CA"},
        {"@type": "City", "name": "Carmel-by-the-Sea, CA"}
    ],
}

SERVICES = [
    ("Residential Window Cleaning", "residential-window-cleaning", "primary"),
    ("Commercial Window Cleaning", "commercial-window-cleaning", "primary"),
    ("Screen Cleaning & Repair", "screen-cleaning-repair", "secondary"),
    ("Hard Water Stain Removal", "hard-water-stain-removal", "secondary"),
    ("Gutter Cleaning", "gutter-cleaning", "secondary"),
]

LOCATIONS = [
    ("Santa Cruz", "santa-cruz"),
    ("Capitola", "capitola"),
    ("Aptos", "aptos"),
    ("Watsonville", "watsonville"),
    ("Monterey", "monterey"),
    ("Pacific Grove", "pacific-grove"),
    ("Carmel-by-the-Sea", "carmel-by-the-sea"),
]
