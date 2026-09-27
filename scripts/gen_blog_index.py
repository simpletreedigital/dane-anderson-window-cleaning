import sys
sys.path.insert(0, "/Volumes/samsung/_WEB/ClaudeCode/clients/dane-anderson-window-cleaning/site/scripts")
from common import *

title = "Blog | Dane Anderson Window Cleaning"
desc = "Coastal window care tips, hard water and salt air guidance, and local insight for homeowners and businesses from Santa Cruz to Monterey."

body = f'''
<section class="page-hero" style="padding:56px 0">
  <div class="hero-bg"><img src="/images/hero/ocean-wave-texture.jpg" alt="" role="presentation"><div class="hero-scrim" style="background:linear-gradient(105deg,rgba(11,61,92,.93) 50%,rgba(11,61,92,.6) 100%)"></div></div>
  <div class="wrap hero-content">
    {breadcrumb([("Home","/"),("Blog",None)])}
    <h1>The Coastal Window Care Blog</h1>
    <p class="lede">Practical guidance on keeping glass clear along the Santa Cruz to Monterey coastline, written for homeowners and businesses dealing with salt air and hard water firsthand.</p>
  </div>
</section>
<section style="background:var(--white)">
<div class="wrap">
<div class="card-grid">
<a href="/blog/how-often-clean-windows-coastal-climate/" class="svc-card" style="text-decoration:none">
<span class="section-label" style="align-self:flex-start">Coastal Climate</span>
<h3>How Often Should You Clean Your Windows in a Coastal Climate?</h3>
<p>Salt air and marine layer moisture accelerate mineral buildup compared to inland California. Here's a distance-from-shore breakdown of realistic cleaning schedules.</p>
<span class="card-link">Read Article &rarr; &middot; 9 min read</span>
</a>
<a href="/blog/salt-air-marine-layer-glass-santa-cruz-monterey/" class="svc-card" style="text-decoration:none">
<span class="section-label" style="align-self:flex-start">Salt Air &amp; Glass</span>
<h3>How Salt Air and Marine Layer Humidity Affect Glass Along This Coast</h3>
<p>A closer look at what actually happens to glass chemically and physically along Monterey Bay, and what homeowners and businesses can do about it.</p>
<span class="card-link">Read Article &rarr; &middot; 10 min read</span>
</a>
<div class="svc-card" style="opacity:.6">
<span class="section-label" style="align-self:flex-start">Coming Soon</span>
<h3>Preparing Storefront Glass for Tourist Season</h3>
<p>A seasonal guide for retail and restaurant owners along the coastal shopping corridors. Coming soon.</p>
</div>
</div>
</div>
</section>
<section class="cta-banner">
<div class="wrap"><h2>Have a Question About Your Windows?</h2><a href="tel:{PHONE_TEL}" class="cta-phone">{PHONE_DISPLAY}</a><a href="tel:{PHONE_TEL}" class="btn btn-cta">&#128222; Call Now</a></div>
</section>
'''
schema = [LOCAL_BUSINESS_BASE, {"@type": "BreadcrumbList", "itemListElement": breadcrumb_schema([("Home","/"),("Blog","/blog/")])}]
html = page_shell(title, desc, "/blog/", schema, body)
write_page("blog/index.html", html)
