import re, glob, os

# Map filename -> descriptive alt text (varied, natural, no keyword stuffing)
ALT_MAP = {
    "homepage-hero-coastal-home.jpg": "Coastal California home exterior with clean windows along the Monterey Bay shoreline",
    "santa-cruz-coastline.jpg": "Santa Cruz, California coastline and boardwalk viewed from the bluffs",
    "capitola-village-beach.jpg": "Capitola Village beachfront and colorful waterfront buildings",
    "aptos-california-coast.jpg": "Aptos coastline near Seacliff State Beach",
    "watsonville-agricultural-valley.jpg": "Pajaro Valley farmland surrounding Watsonville, California",
    "monterey-bay-coastline.jpg": "Monterey Bay coastline with rocky shore and open water",
    "pacific-grove-coast.jpg": "Pacific Grove rocky coastline along Ocean View Boulevard",
    "carmel-by-the-sea.jpg": "Carmel-by-the-Sea coastline with cypress trees along the shore",
    "about-hero-santa-cruz-wharf.jpg": "Santa Cruz wharf at sunset over Monterey Bay",
    "window-cleaner-squeegee-closeup.jpg": "Close-up of a squeegee cleaning a glass window pane",
    "residential-window-cleaning-progress.jpg": "Professional cleaning exterior residential windows",
    "commercial-window-cleaning-storefront.jpg": "Commercial storefront glass being cleaned",
    "gutter-cleaning-ladder.jpg": "Gutter cleaning from a ladder on a residential roofline",
    "hard-water-spots-glass.jpg": "Mineral water spots and droplets visible on a glass pane",
    "window-screen-repair.jpg": "Close-up of window screen mesh and frame",
}

for f in sorted(glob.glob('/Volumes/samsung/_WEB/ClaudeCode/clients/dane-anderson-window-cleaning/site/**/index.html', recursive=True)):
    html = open(f).read()

    def repl(m):
        block = m.group(0)
        src_m = re.search(r'src="([^"]+)"', block)
        if not src_m:
            return block
        fname = os.path.basename(src_m.group(1))
        alt = ALT_MAP.get(fname)
        if not alt:
            return block
        new_block = re.sub(r'alt="[^"]*"\s*role="presentation"', f'alt="{alt}"', block, count=1)
        return new_block

    new_html = re.sub(r'<div class="hero-bg">\s*<img[^>]*>', repl, html)
    if new_html != html:
        open(f, 'w').write(new_html)
        print("fixed hero alt:", f)
