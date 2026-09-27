import sys
sys.path.insert(0, "/Volumes/samsung/_WEB/ClaudeCode/clients/dane-anderson-window-cleaning/site/scripts")
from common import *

title = "Window Cleaning Services | Dane Anderson Window Cleaning"
desc = "Residential and commercial window cleaning, screen repair, hard water stain removal, and gutter cleaning across the Santa Cruz to Monterey coastal corridor."

body = f'''
<section class="page-hero" style="padding:56px 0">
  <div class="hero-bg"><img src="/images/services/window-cleaner-squeegee-closeup.jpg" alt="" role="presentation"><div class="hero-scrim" style="background:linear-gradient(105deg,rgba(11,61,92,.93) 50%,rgba(11,61,92,.6) 100%)"></div></div>
  <div class="wrap hero-content">
    {breadcrumb([("Home","/"),("Services",None)])}
    <h1>Window Cleaning &amp; Exterior Glass Services</h1>
    <p class="lede">From residential glass to commercial storefronts, screen repair, hard water removal, and gutter cleaning, we cover the full exterior maintenance picture for properties along the coast.</p>
    <a href="tel:{PHONE_TEL}" class="btn btn-cta">&#128222; Call {PHONE_DISPLAY}</a>
  </div>
</section>
<section style="background:var(--white)">
  <div class="wrap">
    <span class="section-label">Primary Services</span>
    <h2 class="section-title">Window Cleaning</h2>
    <div class="card-grid" style="margin-bottom:40px">
      <div class="svc-card"><div class="svc-icon">&#127968;</div><h3>Residential Window Cleaning</h3><p>Interior and exterior glass, tracks, sills, and screens for homes of every size.</p><a href="/services/residential-window-cleaning/" class="card-link">Learn more &rarr;</a></div>
      <div class="svc-card"><div class="svc-icon">&#127970;</div><h3>Commercial Window Cleaning</h3><p>Storefronts, offices, and multi-tenant buildings on a recurring schedule.</p><a href="/services/commercial-window-cleaning/" class="card-link">Learn more &rarr;</a></div>
    </div>
    <span class="section-label">Additional Services</span>
    <h2 class="section-title" style="font-size:1.6rem">Screen, Glass Care &amp; Gutters</h2>
    <div class="card-grid">
      <div class="svc-card"><div class="svc-icon">&#128737;</div><h3>Screen Cleaning &amp; Repair</h3><p>Screen washing, re-screening, and frame repair for salt-corroded mesh.</p><a href="/services/screen-cleaning-repair/" class="card-link">Learn more &rarr;</a></div>
      <div class="svc-card"><div class="svc-icon">&#128167;</div><h3>Hard Water Stain Removal</h3><p>Mineral deposit and sprinkler overspray removal that restores true clarity.</p><a href="/services/hard-water-stain-removal/" class="card-link">Learn more &rarr;</a></div>
      <div class="svc-card"><div class="svc-icon">&#127960;</div><h3>Gutter Cleaning</h3><p>Debris removal and downspout flushing ahead of the rainy season.</p><a href="/services/gutter-cleaning/" class="card-link">Learn more &rarr;</a></div>
    </div>
  </div>
</section>
<section style="background:var(--sand-deep)">
  <div class="wrap" style="max-width:820px">
    <p style="line-height:1.85">Not sure which service fits your property? Homeowners in <a href="/locations/santa-cruz/">Santa Cruz</a> and <a href="/locations/monterey/">Monterey</a> often start with a standard residential cleaning and add hard water removal once they see how much of a difference purified water makes near the coast. Businesses along <a href="/locations/carmel-by-the-sea/">Carmel-by-the-Sea's</a> village streets typically set up a recurring commercial plan. Call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> and we will recommend the right starting point for your property.</p>
  </div>
</section>
<section class="cta-banner">
  <div class="wrap">
    <h2>Get a Fast Quote Today</h2>
    <p>Call now, no in-person estimate needed for most residential jobs.</p>
    <a href="tel:{PHONE_TEL}" class="cta-phone">{PHONE_DISPLAY}</a>
    <a href="tel:{PHONE_TEL}" class="btn btn-cta">&#128222; Call Now</a>
  </div>
</section>
'''

schema = [LOCAL_BUSINESS_BASE, {"@type": "BreadcrumbList", "itemListElement": breadcrumb_schema([("Home","/"),("Services","/services/")])}]
html = page_shell(title, desc, "/services/", schema, body)
write_page("services/index.html", html)
