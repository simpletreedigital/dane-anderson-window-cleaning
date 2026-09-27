import sys, json
sys.path.insert(0, "/Volumes/samsung/_WEB/ClaudeCode/clients/dane-anderson-window-cleaning/site/scripts")
from common import *

slug = "residential-window-cleaning"
title = "Residential Window Cleaning Santa Cruz CA | Dane Anderson Window Cleaning"
desc = "Residential window cleaning across Santa Cruz, Capitola, Monterey and the coastal corridor. Interior, exterior, tracks & screens. Call (831) 224-3387."

faqs = [
    ("How much does residential window cleaning cost?", "Most homes along the coastal corridor fall into a straightforward per-pane or flat-rate price depending on window count and style. French panes, hard-to-reach upper stories, and heavy hard water buildup can add time. Call (831) 224-3387 and describe your home for a quote before we ever step on your property."),
    ("Can you clean windows without coming inside my house?", "We can clean the exterior-only if that is what you prefer, but interior glass usually shows the most visible improvement, especially on ocean-facing rooms where salt film collects on both sides. Many homeowners choose the full interior and exterior package for that reason."),
    ("Do you clean window tracks and sills too?", "Yes. Track and sill cleaning is included in a standard residential visit, since sand, salt residue, and dead insects collect there year-round along the coast and are often the source of a musty smell near windows."),
    ("How often should I get my windows professionally cleaned?", "Homes within a mile or two of the water typically benefit from cleaning every 60 to 90 days because of salt spray and marine layer moisture. Homes further inland, such as parts of Aptos or Watsonville set back from the shoreline, can often stretch to twice a year."),
    ("Will you clean second and third story windows?", "Yes, using extension poles with purified water-fed systems for upper stories where ladder access is impractical, which is common on the bluff-top homes found around Pleasure Point, Capitola, and parts of Pacific Grove."),
    ("What if it's foggy or rains the day of my appointment?", "Light coastal fog does not affect the work. If steady rain is forecast, we will call to reschedule so you are not paying for a cleaning that gets rained on within hours."),
    ("Do you use eco-friendly cleaning solutions?", "Our standard process relies primarily on purified, deionized water and a squeegee, which removes the need for heavy chemical cleaners on most jobs. Hard water and mineral buildup sometimes require a targeted solution, applied only where needed."),
]

body = f'''
<section class="page-hero">
  <div class="hero-bg"><img src="/images/services/professional-window-cleaning-pole.jpg" alt="" role="presentation"><div class="hero-scrim" style="background:linear-gradient(105deg,rgba(11,61,92,.93) 50%,rgba(11,61,92,.6) 100%)"></div></div>
  <div class="wrap hero-content">
    {breadcrumb([("Home","/"),("Services","/services/"),("Residential Window Cleaning",None)])}
    <h1>Residential Window Cleaning in Santa Cruz, CA</h1>
    <p class="lede">Dane Anderson Window Cleaning provides thorough interior and exterior window cleaning for homes across Santa Cruz, Capitola, Aptos, and the surrounding coastal communities. Call for a fast quote, no in-person estimate needed for most homes.</p>
    <a href="tel:{PHONE_TEL}" class="btn btn-cta">&#128222; Call {PHONE_DISPLAY}</a>
  </div>
</section>
{wash_section_open("/images/hero/ocean-wave-texture.jpg", opacity=0.07, on_white=True)}
<div class="content-grid">
<div class="prose">
<h2>What Residential Window Cleaning Actually Includes</h2>
<p>A proper residential window cleaning covers more than the visible glass. Our standard visit includes interior and exterior pane cleaning, wiping down tracks and sills, spot-checking screens, and removing cobwebs from window corners and frames. Along this stretch of coastline that last step matters more than it would inland, since salt air draws spiders and insects to window frames looking for moisture.</p>
<p>We use a purified, deionized water-fed pole system for exterior glass on taller homes, paired with a traditional squeegee-and-scrubber approach for interior panes and ground-floor exterior windows. Deionized water leaves no mineral residue behind as it dries, which is the reason professionally cleaned windows stay streak-free days longer than a garden-hose rinse.</p>
<h3>Why Coastal Homes Need a Different Approach</h3>
<p>Homes near Monterey Bay collect a mix of salt spray, marine layer condensation, and hard water sprinkler overspray that inland California properties do not deal with in the same combination. Salt residue is mildly corrosive to window seals and hardware over time, and it also acts like a magnet for moisture, which is part of why coastal glass looks hazy again faster than glass in a drier climate. A cleaning approach built around that reality, rather than a generic spray-and-wipe routine, is the difference between windows that stay clear for weeks and windows that fog over again within days.</p>
<p>For bluff-top and ocean-view properties, we also inspect for early hard water etching during every visit. Left untreated for a year or more, mineral deposits can etch into the glass surface itself, at which point cleaning alone will not fully restore clarity. Our <a href="/services/hard-water-stain-removal/">hard water stain removal service</a> handles that more advanced buildup when it has already set in.</p>
<h3>What Residential Window Cleaning Costs</h3>
<p>Pricing depends on window count, style, and accessibility. A typical single-story home with standard double-hung windows runs toward the lower end of a per-visit quote, while multi-story homes with French panes, bay windows, or difficult roofline access take more time and cost more accordingly. Homes with heavy existing hard water etching may need an add-on treatment beyond a standard cleaning. We quote most residential jobs over the phone based on a short description of your home, and we do not pad quotes with hidden trip fees.</p>
<h3>Our Process</h3>
<div class="steps-list">
<div class="step-item"><div class="step-num">1</div><div><h4>Phone quote</h4><p>Describe your home, window count, and any known problem areas. We give you a straightforward price range on the call.</p></div></div>
<div class="step-item"><div class="step-num">2</div><div><h4>Scheduling</h4><p>We book a visit window that works with your schedule, including early morning slots before the marine layer burns off.</p></div></div>
<div class="step-item"><div class="step-num">3</div><div><h4>Interior walkthrough</h4><p>If interior cleaning is included, we protect sills and flooring before starting, working room by room.</p></div></div>
<div class="step-item"><div class="step-num">4</div><div><h4>Exterior cleaning</h4><p>Purified water-fed poles handle upper stories, squeegee work handles ground-floor and interior glass.</p></div></div>
<div class="step-item"><div class="step-num">5</div><div><h4>Tracks, sills &amp; screens</h4><p>We wipe down tracks and sills and spot-check screens for tears or salt corrosion.</p></div></div>
<div class="step-item"><div class="step-num">6</div><div><h4>Final walkthrough</h4><p>We walk the exterior with you if you are home, and point out anything worth watching, like early hard water spotting.</p></div></div>
</div>
<h3>Detailed Services List</h3>
<ul>
<li><strong>Interior glass cleaning:</strong> full pane cleaning on the inside of every accessible window, including sliding glass doors and French doors.</li>
<li><strong>Exterior glass cleaning:</strong> purified water-fed pole system for upper stories, traditional squeegee work at ground level.</li>
<li><strong>Track and sill detailing:</strong> removal of sand, salt residue, and debris that collects in window channels along the coast.</li>
<li><strong>Screen inspection:</strong> a check for tears, sagging, or salt corrosion on window screens during every visit, with cleaning included and repair available separately.</li>
<li><strong>Cobweb and frame cleanup:</strong> corners and frames cleared of webs and insect debris that build up faster near the water.</li>
<li><strong>Hard water spot check:</strong> a visual assessment for mineral etching, with a referral to our dedicated hard water removal service when needed.</li>
</ul>
{body_image("/images/services/clean-house-windows-exterior.jpg", "A Santa Cruz area home after a full residential window cleaning visit")}
<h3>Local Conditions That Shape Our Process</h3>
<p>Properties along West Cliff Drive and the bluffs above Pleasure Point take the heaviest direct salt spray on this part of the coast, and homeowners there often notice glass haze returning within a few weeks of a standard cleaning during winter storm season. Further south, homes set back in neighborhoods like Seabright or the Pogonip-adjacent hillsides see less direct spray but more marine layer condensation overnight, which still leaves mineral spotting once it evaporates off the glass each morning. We adjust the recommended cleaning frequency for each property based on its actual exposure rather than applying one blanket schedule to every address on our route.</p>
{case_study(
  "Ocean-Facing Windows on West Cliff Drive Restored After Winter Storm Season",
  "A homeowner along West Cliff Drive had gone through an unusually stormy winter with heavy surf and repeated salt spray hitting the ocean-facing side of the house. By spring, the living room and primary bedroom windows had a visible white haze that regular household glass cleaner would not touch.",
  "Our crew identified early-stage hard water and salt mineral etching rather than simple surface grime. We used a mineral deposit remover on the affected panes before the standard purified water-fed cleaning, working the solution in with a non-abrasive pad to avoid scratching the glass.",
  "The haze lifted almost completely in a single visit, and the homeowner reported the ocean view from the living room looked clear again for the first time in over a year. They switched to a quarterly maintenance plan to prevent the buildup from returning."
)}
<h3>Interior Versus Exterior-Only Service</h3>
<p>Some homeowners prefer exterior-only cleaning, particularly for a rental property between tenants or a vacation home visited infrequently. Exterior-only service still addresses the salt spray and marine layer film that does the most visible damage to a home's curb appeal, but it will not remove interior condensation, cooking residue near kitchen windows, or fingerprints on sliding glass doors. For a primary residence, most homeowners find the interior and exterior combination worth the modest additional cost, since ocean-facing rooms in particular show buildup on both sides of the glass simultaneously.</p>
<h3>Preparing for Your Appointment</h3>
<p>There is not much a homeowner needs to do to prepare. Clearing window sills of plants, decor, or electronics makes the interior portion of the visit faster, and letting us know about any pets in advance helps our crew plan entry points. If a specific window has been a persistent problem spot, mentioning it when you book the appointment lets us bring the right treatment supplies rather than discovering the issue mid-visit and having to adjust on the fly.</p>
<h3>Seasonal Timing for Residential Cleaning</h3>
<p>While a recurring schedule works well for most homes, some homeowners prefer to time cleanings around specific events rather than a fixed calendar interval. Booking a cleaning ahead of a holiday gathering, a home sale listing photo shoot, or simply the start of the drier summer months when a home's windows get more daily sunlight and visible attention are all common reasons homeowners call outside their normal rotation. We accommodate one-off requests alongside standing recurring accounts without treating either as a lesser priority.</p>
<h3>Why Choose Dane Anderson Window Cleaning</h3>
<ul>
<li>Fully insured for residential work, including ladder and upper-story access.</li>
<li>Locally owned and operated along the Santa Cruz to Monterey corridor.</li>
<li>Purified water-fed systems built for salt air and hard water conditions specific to this coastline.</li>
<li>Straightforward phone quotes, no pressure and no hidden trip fees.</li>
<li>Add-on services like hard water removal, screen repair, and gutter cleaning available on the same visit.</li>
</ul>
<p>For a broader look at how coastal climate affects glass over time, our blog covers <a href="/blog/how-often-clean-windows-coastal-climate/">how often you should clean windows in a coastal climate</a> in more depth, including a comparison table for different distances from the shoreline. The <a href="https://www.weather.gov/mtr/" target="_blank" rel="noopener">National Weather Service's Monterey forecast office</a> tracks the marine layer patterns behind much of this buildup, and the <a href="https://www.epa.gov/watersense/hard-water" target="_blank" rel="noopener">EPA's WaterSense program</a> documents how water hardness varies by region. Homeowners can also reference the <a href="https://www.cityofsantacruz.com" target="_blank" rel="noopener">City of Santa Cruz</a> website for local property resources.</p>
{faq_block(faqs)}
</div>
<div class="sidebar">
<div class="cta-card"><h3>Get a Fast Quote</h3><p>Call now, most residential jobs quoted over the phone.</p><a href="tel:{PHONE_TEL}" class="btn btn-cta">&#128222; {PHONE_DISPLAY}</a></div>
<div class="sidebar-card"><h3>Related Services</h3><ul><li><a href="/services/hard-water-stain-removal/">Hard Water Stain Removal</a></li><li><a href="/services/screen-cleaning-repair/">Screen Cleaning &amp; Repair</a></li><li><a href="/services/gutter-cleaning/">Gutter Cleaning</a></li></ul></div>
<div class="sidebar-card"><h3>Service Areas</h3><ul><li><a href="/locations/santa-cruz/">Santa Cruz</a></li><li><a href="/locations/capitola/">Capitola</a></li><li><a href="/locations/aptos/">Aptos</a></li><li><a href="/locations/">All Areas &rarr;</a></li></ul></div>
</div>
</div>
{wash_section_close()}
<section style="background:var(--sand-deep)">
<div class="wrap" style="max-width:860px"><p style="line-height:1.85">Dane Anderson Window Cleaning is the residential glass specialist <a href="/locations/santa-cruz/">Santa Cruz</a> homeowners call when the marine layer has taken its toll. We also serve <a href="/locations/aptos/">Aptos</a> and <a href="/locations/capitola/">Capitola</a>, and we pair residential visits with <a href="/services/gutter-cleaning/">gutter cleaning</a> for homeowners who want the full exterior handled in one visit. Businesses can see our separate <a href="/services/commercial-window-cleaning/">commercial window cleaning</a> page.</p></div>
</section>
<section class="cta-banner">
<div class="wrap"><h3>Ready for Streak-Free Windows?</h3><p>Call now for a fast, honest quote.</p><a href="tel:{PHONE_TEL}" class="cta-phone">{PHONE_DISPLAY}</a><a href="tel:{PHONE_TEL}" class="btn btn-cta">&#128222; Call Now</a></div>
</section>
'''

schema = [
    LOCAL_BUSINESS_BASE,
    {"@type": "Service", "serviceType": "Residential Window Cleaning", "provider": {"@id": DOMAIN + "/#business"}, "areaServed": "Santa Cruz to Monterey, CA", "name": "Residential Window Cleaning"},
    {"@type": "BreadcrumbList", "itemListElement": breadcrumb_schema([("Home","/"),("Services","/services/"),("Residential Window Cleaning", f"/services/{slug}/")])},
    faq_schema(faqs),
]
html = page_shell(title, desc, f"/services/{slug}/", schema, body, show_call_bar=True)
write_page(f"services/{slug}/index.html", html)
