import sys
sys.path.insert(0, "/Volumes/samsung/_WEB/ClaudeCode/clients/dane-anderson-window-cleaning/site/scripts")
from common import *

title = "About Dane Anderson Window Cleaning | Santa Cruz to Monterey"
desc = "Learn about Dane Anderson Window Cleaning, a locally owned, fully insured window cleaning company serving the Santa Cruz to Monterey coastal corridor."

faqs = [
    ("Who owns Dane Anderson Window Cleaning?", "Dane Anderson founded the company to provide dependable, locally owned window cleaning to the communities along Monterey Bay, and remains actively involved in the business today."),
    ("Is the business insured?", "Yes, the company is fully insured for both residential and commercial work, which matters whenever a crew is on a ladder or using extension poles at your property."),
    ("What makes coastal window cleaning different from a general cleaning service?", "Salt air, marine layer humidity, and hard water sprinkler overspray combine to create a specific kind of buildup on glass that a generic cleaning routine does not fully address. Our process was built around those local conditions rather than imported from an inland climate."),
    ("Do you only work with homeowners, or businesses too?", "Both. Residential and commercial window cleaning make up roughly equal parts of the business, alongside screen repair, hard water removal, and gutter cleaning."),
]

body = f'''
<section class="page-hero">
  <div class="hero-bg"><img src="/images/hero/about-hero-santa-cruz-wharf.jpg" alt="" role="presentation"><div class="hero-scrim" style="background:linear-gradient(105deg,rgba(11,61,92,.93) 50%,rgba(11,61,92,.6) 100%)"></div></div>
  <div class="wrap hero-content">
    {breadcrumb([("Home","/"),("About",None)])}
    <h1>About Dane Anderson Window Cleaning</h1>
    <p class="lede">A locally owned window cleaning company built for the specific conditions this coastline puts on glass, from Santa Cruz down to Monterey.</p>
    <a href="tel:{PHONE_TEL}" class="btn btn-cta">&#128222; Call {PHONE_DISPLAY}</a>
  </div>
</section>
{wash_section_open("/images/hero/ocean-wave-texture.jpg", opacity=0.07, on_white=True)}
<div class="content-grid">
<div class="prose">
<h2>Built for This Coastline, Not Imported From One</h2>
<p>Dane Anderson Window Cleaning was started to give homeowners and businesses along Monterey Bay a window cleaning service built specifically around local conditions rather than a generic residential cleaning routine applied without adjustment to a very particular climate. Salt spray, marine layer humidity, and hard water sprinkler overspray combine here in a way that most cleaning approaches simply are not designed to handle well over time.</p>
<p>As a locally owned and operated business, we are not a national franchise cycling crews through the area once and moving on. We drive this coastline daily, from the bluffs above Pleasure Point down through the shopping streets of Carmel-by-the-Sea, and that regular presence is part of how we know which properties need attention every 60 days and which can comfortably wait twice as long.</p>
<h3>Our Approach</h3>
<p>Every job starts with an honest assessment of the property rather than a one-size-fits-all quote. A bluff-top home taking direct salt spray gets a different recommendation than a sheltered inland property in the Pajaro Valley, and a storefront with heavy foot traffic gets a different schedule than a quiet office building. We use purified, deionized water-fed systems for exterior and upper-story glass, paired with traditional squeegee work for interior panes, and we treat hard water mineral buildup as its own distinct problem rather than assuming a standard cleaning will fix it.</p>
<h3>Fully Insured, Locally Accountable</h3>
<p>The business carries insurance appropriate to both residential and commercial window cleaning work, which matters whenever a crew is on a ladder, using extension poles, or accessing upper-story glass on your property. Being local also means accountability. If something about a visit was not right, there is a real business and a real phone number to call, not a call center routing you to whichever contractor is available that week.</p>
<div class="team-bio">
<img src="/images/team/dane-anderson-portrait.jpg" alt="Dane Anderson, owner of Dane Anderson Window Cleaning, at home in Santa Cruz">
<div>
<h3 style="margin-top:0">Meet Dane</h3>
<p>Dane grew up in Monterey, close enough to the water that a foggy morning and a salt-hazed car window were just part of daily life long before he ever cleaned glass for a living. He spent his teenage years surfing the breaks around the peninsula, and that same stretch of coastline is still where he spends most mornings before the workday starts.</p>
<p>These days Dane lives in Santa Cruz with his dog, and he built this business around the two things he knows best: this coastline and doing a job right. He started Dane Anderson Window Cleaning to give local homeowners and businesses the kind of dependable, face-to-face service that a national franchise cycling through the area can't offer, someone who actually understands why a Pleasure Point bluff-top house needs a different cleaning schedule than a place a few miles inland.</p>
<p>Outside of work, you'll usually find Dane in the water at first light. That's not just a lifestyle detail, it's part of why he takes coastal glass care seriously. He sees firsthand, nearly every day, exactly what salt spray and marine layer moisture do to everything they touch along this coast, windows included.</p>
</div>
</div>
<h3>Serving the Full Coastal Corridor</h3>
<p>We serve <a href="/locations/santa-cruz/">Santa Cruz</a>, <a href="/locations/capitola/">Capitola</a>, <a href="/locations/aptos/">Aptos</a>, <a href="/locations/watsonville/">Watsonville</a>, <a href="/locations/monterey/">Monterey</a>, <a href="/locations/pacific-grove/">Pacific Grove</a>, and <a href="/locations/carmel-by-the-sea/">Carmel-by-the-Sea</a>, covering the full stretch of coastline from the Santa Cruz Mountains foothills down to the Monterey Peninsula. Our full range of services includes <a href="/services/residential-window-cleaning/">residential window cleaning</a>, <a href="/services/commercial-window-cleaning/">commercial window cleaning</a>, <a href="/services/screen-cleaning-repair/">screen cleaning and repair</a>, <a href="/services/hard-water-stain-removal/">hard water stain removal</a>, and <a href="/services/gutter-cleaning/">gutter cleaning</a>.</p>
<p>For more on why this stretch of coast demands a different approach to glass care, see our blog articles on <a href="/blog/how-often-clean-windows-coastal-climate/">how often to clean windows in a coastal climate</a> and <a href="/blog/salt-air-marine-layer-glass-santa-cruz-monterey/">how salt air and marine layer affect glass here specifically</a>. According to the <a href="https://www.weather.gov/mtr/" target="_blank" rel="noopener">National Weather Service Monterey office</a>, marine layer conditions are a near-daily feature of this coastline for much of the year, which is part of why local expertise matters more here than it might in a drier inland climate. The <a href="https://www.epa.gov/watersense/hard-water" target="_blank" rel="noopener">EPA's WaterSense program</a> and the <a href="https://www.montereychamber.com" target="_blank" rel="noopener">Monterey Peninsula Chamber of Commerce</a> are both useful resources for property owners along this corridor who want to understand water quality and local business conditions in more depth.</p>
{faq_block(faqs)}
</div>
<div class="sidebar">
<div class="cta-card"><h3>Get a Fast Quote</h3><p>Call now to describe your property.</p><a href="tel:{PHONE_TEL}" class="btn btn-cta">&#128222; {PHONE_DISPLAY}</a></div>
<div class="sidebar-card"><h3>Explore</h3><ul><li><a href="/services/">All Services</a></li><li><a href="/locations/">Service Areas</a></li><li><a href="/blog/">Blog</a></li></ul></div>
<img src="/images/team/dane-anderson-surfboards.jpg" alt="Dane Anderson with his surfboards at home in Santa Cruz" style="width:100%;border-radius:var(--radius);box-shadow:var(--shadow)">
</div>
</div>
{wash_section_close()}
<section class="cta-banner">
<div class="wrap"><h2>Let's Get Your Windows Looking Their Best</h2><a href="tel:{PHONE_TEL}" class="cta-phone">{PHONE_DISPLAY}</a><a href="tel:{PHONE_TEL}" class="btn btn-cta">&#128222; Call Now</a></div>
</section>
'''

schema = [LOCAL_BUSINESS_BASE, {"@type": "BreadcrumbList", "itemListElement": breadcrumb_schema([("Home","/"),("About","/about/")])}, faq_schema(faqs)]
html = page_shell(title, desc, "/about/", schema, body)
write_page("about/index.html", html)
