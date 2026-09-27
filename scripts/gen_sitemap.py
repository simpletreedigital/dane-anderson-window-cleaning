import sys
sys.path.insert(0, "/Volumes/samsung/_WEB/ClaudeCode/clients/dane-anderson-window-cleaning/site/scripts")
from common import *
from datetime import date

PAGES = [
    ("/", "Home"),
    ("/about/", "About"),
    ("/services/", "All Services"),
    ("/services/residential-window-cleaning/", "Residential Window Cleaning"),
    ("/services/commercial-window-cleaning/", "Commercial Window Cleaning"),
    ("/services/screen-cleaning-repair/", "Screen Cleaning & Repair"),
    ("/services/hard-water-stain-removal/", "Hard Water Stain Removal"),
    ("/services/gutter-cleaning/", "Gutter Cleaning"),
    ("/locations/", "All Service Areas"),
    ("/locations/santa-cruz/", "Santa Cruz"),
    ("/locations/capitola/", "Capitola"),
    ("/locations/aptos/", "Aptos"),
    ("/locations/watsonville/", "Watsonville"),
    ("/locations/monterey/", "Monterey"),
    ("/locations/pacific-grove/", "Pacific Grove"),
    ("/locations/carmel-by-the-sea/", "Carmel-by-the-Sea"),
    ("/blog/", "Blog"),
    ("/blog/how-often-clean-windows-coastal-climate/", "How Often to Clean Windows in a Coastal Climate"),
    ("/blog/salt-air-marine-layer-glass-santa-cruz-monterey/", "Salt Air & Marine Layer and Glass"),
    ("/sitemap/", "Site Map"),
]

# --- sitemap.xml ---
today = date.today().isoformat()
urls = []
for path, _ in PAGES:
    urls.append(f"  <url><loc>{DOMAIN}{path}</loc><lastmod>{today}</lastmod></url>")
xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n"
with open("/Volumes/samsung/_WEB/ClaudeCode/clients/dane-anderson-window-cleaning/site/sitemap.xml", "w") as f:
    f.write(xml)
print("wrote sitemap.xml")

# --- HTML sitemap page ---
def group(label, items):
    lis = "".join(f'<li><a href="{p}">{n}</a></li>' for p, n in items)
    return f'<div class="sidebar-card" style="text-align:left"><h3>{label}</h3><ul style="list-style:disc;margin-left:18px">{lis}</ul></div>'

main = [("/", "Home"), ("/about/", "About")]
services = [p for p in PAGES if p[0].startswith("/services/")]
locations = [p for p in PAGES if p[0].startswith("/locations/")]
blog = [p for p in PAGES if p[0].startswith("/blog/")]

body = f'''
<section class="page-hero" style="padding:56px 0">
  <div class="wrap hero-content">
    {breadcrumb([("Home","/"),("Site Map",None)])}
    <h1>Site Map</h1>
    <p class="lede">Every page on Dane Anderson Window Cleaning, grouped by category.</p>
  </div>
</section>
<section style="background:var(--white)">
<div class="wrap">
<h2 class="section-title" style="font-size:1.5rem">Browse All Pages</h2>
<div class="card-grid">
{group("Main Pages", main)}
{group("Services", services)}
{group("Service Areas", locations)}
{group("Blog", blog)}
</div>
</div>
</section>
'''
schema = [LOCAL_BUSINESS_BASE, {"@type": "BreadcrumbList", "itemListElement": breadcrumb_schema([("Home","/"),("Site Map","/sitemap/")])}]
html = page_shell("Site Map | Dane Anderson Window Cleaning", "Full site map of Dane Anderson Window Cleaning, listing every service, location, and blog page.", "/sitemap/", schema, body)
write_page("sitemap/index.html", html)
