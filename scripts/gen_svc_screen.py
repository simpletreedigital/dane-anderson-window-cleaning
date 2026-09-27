import sys
sys.path.insert(0, "/Volumes/samsung/_WEB/ClaudeCode/clients/dane-anderson-window-cleaning/site/scripts")
from common import *

slug = "screen-cleaning-repair"
title = "Screen Cleaning & Repair Santa Cruz CA | Dane Anderson Window Cleaning"
desc = "Window screen cleaning, re-screening, and frame repair for salt-corroded mesh across the Santa Cruz to Monterey coastal corridor. Call (831) 224-3387."

faqs = [
    ("How do I know if my screens need repair versus just cleaning?", "If the mesh is torn, sagging, or has visible rust or corrosion at the frame corners, it needs repair rather than cleaning alone. A quick way to check is to press gently on the mesh; if it feels brittle or crumbles at the edges, salt corrosion has likely weakened the frame."),
    ("Can salt air really damage window screens?", "Yes. Aluminum screen frames near the coast corrode faster than the same frames further inland, and fiberglass mesh can become brittle from repeated salt exposure and UV combined. It is one of the more overlooked maintenance items on coastal homes."),
    ("Do you replace the mesh or the whole screen frame?", "Both, depending on condition. If the frame itself is still solid, we re-screen with new mesh in the existing frame. If the frame has corroded or bent, we replace the full screen unit to match your window."),
    ("How often should screens be cleaned?", "Most coastal homes benefit from a screen cleaning alongside each window cleaning visit, roughly every 60 to 90 days for homes closest to the water, since salt residue and dust build up on mesh just as it does on glass."),
    ("Do you match mesh color and frame finish?", "Yes, we match standard mesh colors and common aluminum frame finishes so repaired or replaced screens blend in with the rest of your home rather than standing out."),
]

body = f'''
<section class="page-hero">
  <div class="hero-bg"><img src="/images/services/window-screen-repair.jpg" alt="" role="presentation"><div class="hero-scrim" style="background:linear-gradient(105deg,rgba(11,61,92,.93) 50%,rgba(11,61,92,.6) 100%)"></div></div>
  <div class="wrap hero-content">
    {breadcrumb([("Home","/"),("Services","/services/"),("Screen Cleaning & Repair",None)])}
    <h1>Screen Cleaning &amp; Repair in Santa Cruz, CA</h1>
    <p class="lede">Salt air corrodes screen frames and clogs mesh faster than an inland climate ever would. We clean, re-screen, and repair window screens across the coastal corridor so the view and the airflow both stay clear.</p>
    <a href="tel:{PHONE_TEL}" class="btn btn-cta">&#128222; Call {PHONE_DISPLAY}</a>
  </div>
</section>
{wash_section_open("/images/hero/ocean-wave-texture.jpg", opacity=0.07, on_white=True)}
<div class="content-grid">
<div class="prose">
<h2>Why Coastal Screens Need More Attention</h2>
<p>Window screens do double duty along Monterey Bay. They keep out the same insects that any inland home deals with, but they also act as a filter that catches windblown salt, sand, and dust before it settles inside the house. Over time that filtering role takes a toll on the mesh and frame that homeowners further from the coast simply do not experience at the same rate.</p>
<p>Aluminum screen frames corrode faster in salt air, especially at the corners where two pieces of frame meet and moisture tends to collect. Fiberglass mesh can become brittle when repeated salt exposure combines with UV exposure from the coastal sun, leading to small tears that widen over a season. A screen that looked fine last year can be genuinely fragile by the time the next one rolls around, which is why we inspect screens as part of every residential window cleaning visit rather than waiting for a homeowner to notice a problem.</p>
{body_image("/images/services/window-screen-repair.jpg", "A repaired window screen ready for reinstallation")}
<h3>Cleaning Versus Repair</h3>
<p>Screen cleaning removes the dust, salt residue, and pollen that reduces airflow and leaves a hazy look when you view the yard or ocean through the mesh. It is a straightforward process using a soft brush and rinse that will not stretch or tear healthy mesh. Repair becomes necessary once the mesh itself has torn, sagged, or pulled away from the frame track, or once the frame has visibly corroded or bent. We assess each screen individually rather than assuming every screen on a property needs the same treatment.</p>
<h3>What Screen Cleaning &amp; Repair Costs</h3>
<p>Screen cleaning is typically bundled into a residential window cleaning visit at a modest add-on cost per screen. Re-screening, where we replace just the mesh in an existing frame, costs more per unit but less than replacing the entire screen. Full screen replacement, used when a frame has corroded or bent beyond repair, is priced individually based on size and frame style. We quote screen work honestly rather than upselling a full replacement when a re-screen would do the job.</p>
<h3>Our Process</h3>
<div class="steps-list">
<div class="step-item"><div class="step-num">1</div><div><h4>Inspection</h4><p>Every screen is checked for tears, sagging, and frame corrosion before we recommend cleaning or repair.</p></div></div>
<div class="step-item"><div class="step-num">2</div><div><h4>Cleaning</h4><p>Salvageable screens are brushed and rinsed to remove salt residue, dust, and pollen buildup.</p></div></div>
<div class="step-item"><div class="step-num">3</div><div><h4>Re-screening</h4><p>Screens with torn or sagging mesh but a solid frame get new mesh installed in the existing frame.</p></div></div>
<div class="step-item"><div class="step-num">4</div><div><h4>Frame replacement</h4><p>Corroded or bent frames are replaced entirely with matching finish and mesh color.</p></div></div>
<div class="step-item"><div class="step-num">5</div><div><h4>Reinstallation</h4><p>Every screen is reinstalled and checked for a proper fit in the window track before we finish.</p></div></div>
</div>
<h3>Detailed Services List</h3>
<ul>
<li><strong>Screen mesh cleaning:</strong> soft brush and rinse process that removes salt film and dust without stretching the mesh.</li>
<li><strong>Re-screening:</strong> new mesh installed in an existing, still-solid frame at lower cost than full replacement.</li>
<li><strong>Frame repair and replacement:</strong> corroded or bent aluminum frames replaced to match existing finish.</li>
<li><strong>Sliding door screen service:</strong> patio and slider screens cleaned and repaired, including roller and track adjustment.</li>
<li><strong>Pet-resistant and solar mesh options:</strong> upgraded mesh available for households with pets or homeowners wanting extra UV reduction.</li>
</ul>
<h3>A Local Pattern Worth Knowing</h3>
<p>Homes closest to the water on bluffs above Pleasure Point and along the Capitola shoreline see the fastest frame corrosion we encounter on this route, often within just a few years compared to a decade or more inland. Properties further back in neighborhoods like Aptos or set inland near Watsonville deal much more with dust and pollen buildup on mesh than with frame corrosion itself, so a cleaning-only approach is more often sufficient there. Knowing which category a property falls into helps us recommend the right service instead of defaulting to a full replacement quote every time.</p>
{case_study(
  "Sliding Door Screens Near Pleasure Point Replaced After Years of Salt Exposure",
  "A homeowner near Pleasure Point had two sliding door screens with mesh so brittle it was tearing at the slightest touch, and the aluminum frame track had visible white corrosion buildup that was making the door stick when opened.",
  "We assessed the frames and determined the tracks themselves were still structurally sound despite the corrosion, so we cleaned and lubricated the tracks, then installed fresh solar-grade mesh in the existing frames rather than replacing the full door screen units.",
  "The repair cost roughly half of what a full screen replacement would have run, the doors slid smoothly again, and the homeowner added both screens to their regular window cleaning visit going forward to catch corrosion earlier next time."
)}
<h3>Solar and Pet-Resistant Mesh Options</h3>
<p>Beyond standard fiberglass mesh, we offer upgraded mesh options for homeowners with specific needs. Solar screen mesh has a tighter weave that blocks a meaningfully higher percentage of UV radiation, useful for ocean-facing rooms that take direct afternoon sun for much of the year and where furniture or flooring fading has become a concern. Pet-resistant mesh uses a thicker, more tear-resistant weave designed to hold up against scratching and pushing from cats and dogs, which is a common request for households with sliding door screens that see daily pet traffic.</p>
<p>Both upgraded mesh types cost more per screen than standard fiberglass, but for the right household the added durability or UV protection pays for itself by extending the interval between repairs. We can install either type during a standard re-screening visit without any additional scheduling complexity.</p>
<h3>How This Fits With Other Services</h3>
<p>Screen work rarely happens in isolation. Because our crew is already on site and often already on a ladder for exterior glass, bundling screen cleaning or repair into a scheduled <a href="/services/residential-window-cleaning/">residential window cleaning</a> or <a href="/services/commercial-window-cleaning/">commercial window cleaning</a> visit is more efficient than scheduling a separate appointment. Many of our recurring residential accounts include a screen check on every visit at no separate trip cost, with cleaning or repair quoted only when an issue is actually found.</p>
<p>For more on why coastal conditions affect exterior materials broadly, the <a href="https://www.nps.gov/subjects/climatechange/coastalprocesses.htm" target="_blank" rel="noopener">National Park Service's overview of coastal processes</a> documents salt spray deposition patterns, and the <a href="https://www.epa.gov/watersense/hard-water" target="_blank" rel="noopener">EPA's WaterSense program</a> covers related regional water hardness data. The <a href="https://www.santacruzchamber.org" target="_blank" rel="noopener">Santa Cruz Chamber of Commerce</a> lists additional local property maintenance resources.</p>
{faq_block(faqs)}
</div>
<div class="sidebar">
<div class="cta-card"><h3>Get Your Screens Checked</h3><p>Bundle with a window cleaning visit.</p><a href="tel:{PHONE_TEL}" class="btn btn-cta">&#128222; {PHONE_DISPLAY}</a></div>
<div class="sidebar-card"><h3>Related Services</h3><ul><li><a href="/services/residential-window-cleaning/">Residential Window Cleaning</a></li><li><a href="/services/hard-water-stain-removal/">Hard Water Stain Removal</a></li><li><a href="/services/gutter-cleaning/">Gutter Cleaning</a></li></ul></div>
<div class="sidebar-card"><h3>Service Areas</h3><ul><li><a href="/locations/santa-cruz/">Santa Cruz</a></li><li><a href="/locations/capitola/">Capitola</a></li><li><a href="/locations/">All Areas &rarr;</a></li></ul></div>
</div>
</div>
{wash_section_close()}
<section style="background:var(--sand-deep)">
<div class="wrap" style="max-width:860px"><p style="line-height:1.85">Homeowners in <a href="/locations/aptos/">Aptos</a> and along the <a href="/locations/santa-cruz/">Santa Cruz</a> bluffs often bundle screen service with a full <a href="/services/residential-window-cleaning/">residential window cleaning</a> visit. Businesses with storefront screen doors can add this to a <a href="/services/commercial-window-cleaning/">commercial window cleaning</a> schedule as well.</p></div>
</section>
<section class="cta-banner">
<div class="wrap"><h2>Restore Airflow and Clarity</h2><p>Call now to get your screens inspected.</p><a href="tel:{PHONE_TEL}" class="cta-phone">{PHONE_DISPLAY}</a><a href="tel:{PHONE_TEL}" class="btn btn-cta">&#128222; Call Now</a></div>
</section>
'''

schema = [
    LOCAL_BUSINESS_BASE,
    {"@type": "Service", "serviceType": "Screen Cleaning & Repair", "provider": {"@id": DOMAIN + "/#business"}, "areaServed": "Santa Cruz to Monterey, CA", "name": "Screen Cleaning & Repair"},
    {"@type": "BreadcrumbList", "itemListElement": breadcrumb_schema([("Home","/"),("Services","/services/"),("Screen Cleaning & Repair", f"/services/{slug}/")])},
    faq_schema(faqs),
]
html = page_shell(title, desc, f"/services/{slug}/", schema, body, show_call_bar=True)
write_page(f"services/{slug}/index.html", html)
