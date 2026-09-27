import sys
sys.path.insert(0, "/Volumes/samsung/_WEB/ClaudeCode/clients/dane-anderson-window-cleaning/site/scripts")
from common import *

CITIES = {
    "santa-cruz": {
        "name": "Santa Cruz",
        "hero_img": "/images/hero/santa-cruz-coastline.jpg",
        "gov_link": ("City of Santa Cruz", "https://www.cityofsantacruz.com"),
        "chamber_link": ("Santa Cruz Chamber of Commerce", "https://www.santacruzchamber.org"),
        "civic_link": ("Santa Cruz, California on Wikipedia", "https://en.wikipedia.org/wiki/Santa_Cruz,_California"),
        "neighborhoods": "Pleasure Point, West Cliff Drive, Seabright, and the hillside neighborhoods near Pogonip",
        "corridors": "West Cliff Drive along the bluffs, the Pleasure Point surf breaks, and the mixed residential streets around Seabright Beach",
        "context": "As the home base for Dane Anderson Window Cleaning, this is where our crew starts every route each morning. The city's mix of century-old Victorians downtown, mid-century beach cottages near the wharf, and newer construction on the west side means we see nearly every glass style and window age this coastline has to offer.",
        "neighbors": [("capitola", "Capitola"), ("aptos", "Aptos")],
        "case": (
            "Salt-Hazed Picture Windows Above Pleasure Point Restored for a Family Reunion",
            "A family hosting a reunion at their home above Pleasure Point noticed just days before the event that their large ocean-facing picture windows had a heavy salt haze from a stretch of winter storms, and the view they wanted to show off was badly dulled.",
            "We prioritized a same-week visit, using a purified water-fed pole system on the exterior and a mineral deposit treatment on the worst-affected lower panes, finishing with interior glass cleaning so the view looked sharp from both sides.",
            "The windows were fully restored two days ahead of the event, and the family has since booked a standing quarterly cleaning to keep the view clear year-round."
        ),
        "faqs": [
            ("Do you serve the Pleasure Point and West Cliff area specifically?", "Yes, this is one of our most frequently serviced neighborhoods given the high concentration of ocean-facing homes that take the heaviest direct salt spray on this stretch of coast."),
            ("How quickly can you schedule a visit here?", "Since this is our home base, scheduling here is typically the fastest on our route, often within a few days for standard residential jobs."),
            ("Do older Victorian-era homes downtown need a different approach?", "Older wood-frame windows can have more delicate glazing and putty than modern vinyl frames, so we adjust pressure and technique accordingly rather than using the same approach on every window style."),
            ("What is the most common service call in this area?", "Residential window cleaning paired with hard water treatment is the most common combination, particularly for homes with ocean-facing exposure along the coastal bluffs."),
        ],
        "climate": "Winter storm season brings the heaviest salt spray to bluff-top properties here, with wind-driven surf regularly reaching homes along the cliffside streets. Summer's marine layer settles in most mornings and burns off by early afternoon, leaving a fine residue on glass that accumulates gradually rather than all at once. Homeowners who wait for a visibly dirty window often find that gradual buildup is further along than it looked from a distance.",
        "landscape": "The mix of building stock adds its own wrinkle. Wood-frame Victorian homes near downtown and the beach flats have original single-pane glass with delicate glazing putty, while newer construction on the upper west side and near DeLaveaga tends to have dual-pane vinyl windows that handle cleaning pressure differently. Rental properties near the university corridor see less frequent upkeep between tenant turnovers, which is where we most often find the heaviest buildup on an otherwise routine service call.",
    },
    "capitola": {
        "name": "Capitola",
        "hero_img": "/images/hero/capitola-village-beach.jpg",
        "gov_link": ("City of Capitola", "https://www.cityofcapitola.org"),
        "chamber_link": ("Capitola Chamber of Commerce", "https://www.capitolachamber.com"),
        "civic_link": ("Capitola, California on Wikipedia", "https://en.wikipedia.org/wiki/Capitola,_California"),
        "neighborhoods": "Capitola Village, the Depot Hill bluffs, and the residential streets along Soquel Creek",
        "corridors": "the shops and restaurants of Capitola Village, the bluff-top homes on Depot Hill, and the beachfront esplanade",
        "context": "This coastal village is known for its brightly colored beachfront buildings and a shopping district that draws visitors year-round, which means storefront glass here takes on both salt spray and heavy foot traffic simultaneously. Bluff-top homes on Depot Hill face similar salt exposure to the ocean-facing properties found further north along the coast.",
        "neighbors": [("santa-cruz", "Santa Cruz"), ("aptos", "Aptos")],
        "case": (
            "Village Storefront Sets Up Weekly Cleaning Ahead of Summer Tourist Season",
            "A gift shop owner in Capitola Village had relied on staff wiping down the front windows between customers, but salt spray combined with fingerprints from browsing tourists left the glass looking smudged by midday most weekends.",
            "We set up a recurring weekly cleaning scheduled for early morning before the shop opened, using a purified water-fed system on the tall storefront glass and a manual squeegee pass on the entry door.",
            "The shop's front window has stayed presentable throughout the entire tourist season, and the owner reports the display merchandise photographs better in customer social media posts without the glare from smudged glass."
        ),
        "faqs": [
            ("Do you clean storefront glass in the Village during tourist season?", "Yes, and we typically schedule Village storefronts for early morning visits before shops open, so cleaning does not interfere with customer traffic during peak hours."),
            ("Are bluff-top homes on Depot Hill harder to service?", "Some have more limited exterior access, but our purified water-fed pole systems handle most bluff-top upper-story windows without needing scaffolding."),
            ("How often do homes near the esplanade need cleaning?", "Given the direct beachfront salt exposure, most properties in this area do best on a 60 to 90 day cleaning schedule."),
            ("Can you coordinate with a property manager for multiple Village storefronts?", "Yes, we regularly set up consolidated scheduling and single monthly invoicing for property managers overseeing several Village tenants."),
        ],
        "climate": "The beachfront esplanade sits directly exposed to onshore wind, and storefronts there take salt spray nearly identical to what oceanfront homes experience further up the coast. A block or two inland, the Depot Hill bluff homes get slightly more shelter from buildings and trees but still see enough direct exposure to need regular attention.",
        "landscape": "Retail buildings along the esplanade tend to have large plate glass display windows built specifically to show off merchandise, which means any haze or smudging is immediately visible to browsing customers in a way it would not be on a smaller residential pane. Homes on the bluff above mix older beach cottages with newer remodels, and the newer dual-pane construction generally resists hard water spotting better than the original single-pane glass still found in some of the older cottages.",
    },
    "aptos": {
        "name": "Aptos",
        "hero_img": "/images/hero/aptos-california-coast.jpg",
        "gov_link": ("County of Santa Cruz", "https://www.santacruzcountyca.gov"),
        "chamber_link": ("Aptos Chamber of Commerce", "https://www.aptoschamber.com"),
        "civic_link": ("Aptos, California on Wikipedia", "https://en.wikipedia.org/wiki/Aptos,_California"),
        "neighborhoods": "Seacliff, Rio Del Mar, and the wooded foothill streets toward Corralitos",
        "corridors": "the Seacliff beachfront, the Rio Del Mar esplanade, and the redwood-shaded residential roads set back from the shoreline",
        "context": "This unincorporated community stretches from a sandy beachfront at Seacliff and Rio Del Mar back into redwood-covered hillside neighborhoods, giving it two distinct maintenance profiles within the same town. Beachfront homes deal with heavier salt exposure, while the wooded foothill properties see more redwood needle debris and hard water buildup from garden irrigation.",
        "neighbors": [("capitola", "Capitola"), ("watsonville", "Watsonville")],
        "case": (
            "Hillside Home Near Corralitos Gets Ahead of Redwood Needle Gutter Buildup",
            "A homeowner in the wooded hills toward Corralitos had never had gutters professionally cleaned and discovered, after a neighbor's overflow issue during a storm, that their own gutters were packed nearly solid with years of redwood needle buildup.",
            "We combined a full gutter clearing and downspout flush with a residential window cleaning visit, since sprinkler overspray had also left noticeable hard water spotting on several ground-floor windows facing the garden.",
            "The gutters were cleared of debris that had compacted into a solid mat in several sections, and the homeowner set up a standing twice-yearly gutter service alongside seasonal window cleaning to avoid a repeat buildup."
        ),
        "faqs": [
            ("Do beachfront homes near Seacliff need more frequent cleaning than hillside homes?", "Generally yes, beachfront properties facing direct salt spray typically need cleaning every 60 to 90 days, while wooded hillside homes further from the water can often go longer between visits."),
            ("Is gutter cleaning more common in this area than elsewhere on your route?", "Yes, the redwood and pine tree cover in the foothill neighborhoods makes gutter cleaning one of the most requested services in this part of our service area."),
            ("Do you service both Seacliff and Rio Del Mar?", "Yes, both beachfront neighborhoods are part of our regular route alongside the wooded areas further inland."),
            ("What is the typical hard water issue here?", "Garden and lawn sprinkler overspray onto ground-floor windows is the most common source of hard water buildup we see in this community."),
        ],
        "climate": "The split geography here means two different maintenance patterns within a few miles of each other. Seacliff and Rio Del Mar sit directly on the sand and take on salt spray comparable to beachfront towns further north, while the redwood-shaded roads climbing toward Corralitos are sheltered from wind but see near-constant tree debris and shaded, slow-drying glass instead.",
        "landscape": "Beachfront homes here tend to be a mix of older beach cottages and larger modern rebuilds, both with significant ocean-facing glass meant to showcase the view, which makes salt haze especially noticeable to homeowners who chose the property specifically for that outlook. The hillside homes further back often have larger lots with automatic irrigation systems feeding established gardens, a setup that reliably produces the ground-floor hard water spotting we treat most often in this part of our service area.",
    },
    "watsonville": {
        "name": "Watsonville",
        "hero_img": "/images/hero/watsonville-agricultural-valley.jpg",
        "gov_link": ("City of Watsonville", "https://www.watsonville.gov"),
        "chamber_link": ("Watsonville Chamber of Commerce", "https://www.watsonvillechamber.com"),
        "civic_link": ("Watsonville, California on Wikipedia", "https://en.wikipedia.org/wiki/Watsonville,_California"),
        "neighborhoods": "downtown Watsonville, the Freedom Boulevard corridor, and the surrounding Pajaro Valley farmland",
        "corridors": "the historic downtown storefronts, the Freedom Boulevard commercial strip, and the agricultural roads through the Pajaro Valley",
        "context": "Set back from the immediate shoreline in the heart of the Pajaro Valley, this agricultural hub deals with less direct salt spray than the beach towns to its north, but sees its own combination of farmland dust, agricultural irrigation overspray, and a historic downtown with older storefront glass that needs regular attention.",
        "neighbors": [("aptos", "Aptos"), ("santa-cruz", "Santa Cruz")],
        "case": (
            "Downtown Storefront Restored After Years of Dust and Delivery Truck Grime",
            "A small business on a downtown storefront had not had its historic display windows professionally cleaned in several years, and a layer of farmland dust combined with delivery truck exhaust residue had left the glass looking permanently dingy.",
            "We used a degreasing pre-treatment before the standard squeegee cleaning to break down the combination of dust and exhaust film, working carefully around the older wood window frames typical of the building's era.",
            "The storefront glass came back to a clarity the owner said they had not seen in years, and the business signed up for a monthly recurring cleaning to keep dust buildup from accumulating again."
        ),
        "faqs": [
            ("Is hard water a bigger issue here than salt spray?", "Yes, properties in this valley deal more with irrigation and agricultural dust than with direct ocean salt spray, so our approach here focuses more on dust and mineral buildup than salt film removal."),
            ("Do you service the historic downtown storefronts?", "Yes, we regularly clean storefront glass along the downtown corridor, working carefully with the older wood window frames common to buildings in this area."),
            ("How far do you travel from Santa Cruz to reach this area?", "This community sits toward the southern end of our regular route, and we schedule visits here on set days each week rather than on demand, which keeps pricing efficient."),
            ("Can farms and agricultural offices in the valley book commercial service?", "Yes, we service office buildings and packing facility front offices throughout the valley on the same recurring commercial schedule we offer elsewhere."),
        ],
        "climate": "Set a few miles inland from the immediate coastline, this valley sees noticeably less direct salt spray than the beach towns to the north, but agricultural activity brings its own airborne dust, especially during harvest season when field work kicks up fine particulate that settles on glass surfaces across town, storefront and residential alike.",
        "landscape": "Downtown's historic storefronts date back several decades in some cases, with wood-frame display windows that require a gentler touch than modern aluminum storefront systems. Homes throughout the surrounding valley are set among working farmland, and many rely on well water for irrigation, which can carry a different, sometimes heavier mineral profile than municipal water used closer to the coast, something worth factoring in when we assess hard water buildup on a property here.",
    },
    "monterey": {
        "name": "Monterey",
        "hero_img": "/images/hero/monterey-bay-coastline.jpg",
        "gov_link": ("City of Monterey", "https://www.monterey.org"),
        "chamber_link": ("Monterey Peninsula Chamber of Commerce", "https://www.montereychamber.com"),
        "civic_link": ("Monterey, California on Wikipedia", "https://en.wikipedia.org/wiki/Monterey,_California"),
        "neighborhoods": "Cannery Row, Alvarado Street downtown, and the residential streets near Del Monte Beach",
        "corridors": "the restaurant and retail strip along Cannery Row, the Alvarado Street downtown business district, and the Del Monte waterfront",
        "context": "Home to one of the busiest tourist corridors on this coastline, this city's Cannery Row district sees storefront and restaurant glass exposed to constant bay-facing salt spray alongside heavy foot traffic from visitors. The downtown business district along Alvarado Street has its own mix of office and retail glass with a steadier, less tourist-driven rhythm.",
        "neighbors": [("pacific-grove", "Pacific Grove"), ("carmel-by-the-sea", "Carmel-by-the-Sea")],
        "case": (
            "Cannery Row Restaurant Ends Complaints About Hazy Bay-View Windows",
            "A restaurant along Cannery Row had received several customer comments about a persistent haze on the large bay-facing windows that staff wiping down the glass between shifts could not fully resolve.",
            "We established a weekly early-morning cleaning schedule before opening hours, combined with a monthly hard water treatment to address mineral buildup from salt spray, using purified water-fed poles for the tall storefront glass.",
            "Customer comments about the windows stopped within the first month, and the account has continued on the same weekly schedule for more than a year."
        ),
        "faqs": [
            ("Do you clean storefront glass along Cannery Row?", "Yes, this is one of our busiest commercial corridors, and most restaurant and retail accounts here run on a weekly or biweekly recurring schedule."),
            ("How does bay-facing exposure affect cleaning frequency?", "Storefronts directly facing the bay take heavier salt spray than interior downtown blocks, so we typically recommend more frequent visits for bay-facing glass."),
            ("Do you service office buildings on Alvarado Street too?", "Yes, downtown office and retail buildings are part of our regular commercial route alongside the tourist corridor accounts."),
            ("Can residential homes near Del Monte Beach book service?", "Yes, residential window cleaning is available throughout the neighborhoods near Del Monte Beach and the surrounding hillside streets."),
        ],
        "climate": "Bay-facing storefronts along the waterfront corridor take on salt spray at a rate closer to open-ocean exposure than a typical harbor town, since the bay's wind patterns funnel moisture directly onto that stretch. A few blocks inland toward the downtown core, exposure drops noticeably, which is part of why we run different visit frequencies for waterfront versus inland commercial accounts here rather than a single blanket schedule.",
        "landscape": "The tourist-driven waterfront district sees a volume of foot traffic and fingerprints on entry doors that few other towns on our route experience, particularly during peak season months. Away from the water, the downtown business district and residential hillside neighborhoods have a steadier, less seasonal rhythm, with older homes near the historic district often retaining original single-pane windows that need a more careful cleaning approach than newer dual-pane construction.",
    },
    "pacific-grove": {
        "name": "Pacific Grove",
        "hero_img": "/images/hero/pacific-grove-coast.jpg",
        "gov_link": ("City of Pacific Grove", "https://www.cityofpacificgrove.org"),
        "chamber_link": ("Pacific Grove Chamber of Commerce", "https://www.pacificgrove.org"),
        "civic_link": ("Pacific Grove, California on Wikipedia", "https://en.wikipedia.org/wiki/Pacific_Grove,_California"),
        "neighborhoods": "Lovers Point, Ocean View Boulevard, and the Asilomar coastal edge",
        "corridors": "the Lovers Point waterfront, the Ocean View Boulevard scenic drive, and the Asilomar dunes area",
        "context": "This small coastal city sits on some of the most exposed, wind-battered shoreline on the entire peninsula, with Ocean View Boulevard tracing the rocky coast almost the entire length of town. Homes directly along this drive take some of the heaviest direct salt spray we encounter anywhere on our route.",
        "neighbors": [("monterey", "Monterey"), ("carmel-by-the-sea", "Carmel-by-the-Sea")],
        "case": (
            "Ocean View Boulevard Home Adopts Monthly Cleaning After Severe Salt Etching",
            "A homeowner along Ocean View Boulevard had gone over a year without cleaning during an unusually stormy winter, and the ocean-facing windows had developed visible salt etching that a standard cleaning could only partially improve.",
            "We treated the affected panes with a mineral deposit solution across two visits spaced several weeks apart, since the buildup was too severe to fully address in a single pass, and recommended a monthly schedule going forward given the property's direct wind and spray exposure.",
            "Clarity improved significantly, though some permanent light etching remained visible at close range. The homeowner moved to monthly cleaning, which has prevented any further deterioration since."
        ),
        "faqs": [
            ("Why does this area need more frequent cleaning than other towns on your route?", "Homes directly along Ocean View Boulevard face some of the most exposed, wind-driven salt spray on the entire peninsula, which accelerates buildup faster than more sheltered locations."),
            ("Do you service homes near Lovers Point?", "Yes, this is a regular stop on our route given the concentration of ocean-facing residential properties in that neighborhood."),
            ("Is hard water etching common here?", "It is more common here than in most of our service area specifically because of the combination of direct salt spray and infrequent cleaning on some older properties."),
            ("Do you clean windows at properties near Asilomar?", "Yes, we service both residential homes and any commercial or event properties near the Asilomar coastal area."),
        ],
        "climate": "Ocean View Boulevard runs along some of the most exposed rocky shoreline on the entire peninsula, with almost no natural windbreak between the water and the row of homes facing it. Wind-driven spray here is a near-daily occurrence during the winter months, and even in summer the marine layer tends to linger longer than in more sheltered towns nearby.",
        "landscape": "Homes directly along the boulevard were largely built to capture unobstructed ocean views, meaning a high ratio of glass to wall space that magnifies any salt haze buildup compared to a typical inland home with smaller windows. Streets set back just a block or two see a meaningful drop in exposure, which is why we recommend different cleaning frequencies for oceanfront versus interior addresses even within this same small city.",
    },
    "carmel-by-the-sea": {
        "name": "Carmel-by-the-Sea",
        "hero_img": "/images/hero/carmel-by-the-sea.jpg",
        "gov_link": ("City of Carmel-by-the-Sea", "https://ci.carmel.ca.us"),
        "chamber_link": ("Carmel Chamber of Commerce", "https://www.carmelchamber.org"),
        "civic_link": ("Carmel-by-the-Sea, California on Wikipedia", "https://en.wikipedia.org/wiki/Carmel-by-the-Sea,_California"),
        "neighborhoods": "the village core along Ocean Avenue, the residential streets near Carmel Beach, and Scenic Road",
        "corridors": "the boutique shopping district along Ocean Avenue, the cottages near Carmel Beach, and the bluff-top homes on Scenic Road",
        "context": "This compact, walkable village is known for its boutique shops and galleries along Ocean Avenue and its cottage-style homes tucked among cypress and pine trees, many just blocks from the sand at Carmel Beach. The lack of street addresses and numbered signage in parts of the village is a well-known local quirk, and it means clear scheduling communication matters more here than almost anywhere else on our route.",
        "neighbors": [("pacific-grove", "Pacific Grove"), ("monterey", "Monterey")],
        "case": (
            "Ocean Avenue Boutique Sets Up Biweekly Cleaning Ahead of Holiday Shopping Season",
            "A boutique shop on Ocean Avenue wanted its display windows spotless heading into the holiday shopping season, but salt spray combined with the village's heavy pedestrian traffic left the glass smudged within days of any prior cleaning.",
            "We set up a biweekly recurring schedule with early morning visits before the shop opened, treating the display windows with extra attention to fingerprints and glare given how central the window displays were to the shop's holiday marketing.",
            "The shop's owner reported the cleanest window displays of any holiday season in recent memory, and the account has continued on the same biweekly schedule beyond the holidays."
        ),
        "faqs": [
            ("Do you navigate the village's unusual addressing when scheduling?", "Yes, our crew is familiar with the village's lack of standard street numbers and works from cross streets and business names to schedule and arrive accurately."),
            ("Do you service both village storefronts and residential cottages?", "Yes, we handle both the Ocean Avenue commercial corridor and residential window cleaning for the cottage-style homes throughout the village and near the beach."),
            ("How does the tree cover here affect gutter cleaning?", "The cypress and pine trees common throughout the village make gutter cleaning a frequently requested service alongside window cleaning."),
            ("Do bluff-top homes on Scenic Road need special access?", "Some do have more limited exterior access, but our pole systems and ladder equipment handle the majority of properties along this stretch without issue."),
        ],
        "climate": "Fog rolls through the village most mornings before burning off by midday, leaving a fine salt film that settles evenly across both storefront and residential glass. Wind off the water tends to funnel through the grid of streets running down to the beach, which pushes salt spray further inland here than in towns with a more sheltered layout.",
        "landscape": "Many homes here are cottage-style construction with smaller, multi-pane windows set among mature cypress and pine trees, a look the village is known for but one that also means more shaded, damp glass that takes longer to dry naturally between rains. The commercial buildings along Ocean Avenue mix older storefront glass with newer boutique renovations, and we adjust technique for each rather than treating every pane the same way.",
    },
}

ORDER = ["santa-cruz","capitola","aptos","watsonville","monterey","pacific-grove","carmel-by-the-sea"]

for slug in ORDER:
    c = CITIES[slug]
    name = c["name"]
    title = f"Window Cleaning {name}, CA | Dane Anderson Window Cleaning"
    desc = f"Professional window cleaning in {name}, CA. Residential & commercial, screen repair, hard water removal, gutter cleaning. Call (831) 224-3387."
    n1_slug, n1_name = c["neighbors"][0]
    n2_slug, n2_name = c["neighbors"][1]
    gov_name, gov_url = c["gov_link"]
    cham_name, cham_url = c["chamber_link"]
    civic_name, civic_url = c["civic_link"]

    faqs = c["faqs"] + [("Are you insured to work on my property here?", f"Yes, Dane Anderson Window Cleaning carries insurance covering both residential and commercial work throughout {name} and the rest of the coastal corridor, which matters whenever a crew is on a ladder or using extension poles at your property.")]
    case_title, case_sit, case_app, case_out = c["case"]

    body = f'''
<section class="page-hero">
  <div class="hero-bg"><img src="{c['hero_img']}" alt="" role="presentation"><div class="hero-scrim" style="background:linear-gradient(105deg,rgba(11,61,92,.93) 50%,rgba(11,61,92,.6) 100%)"></div></div>
  <div class="wrap hero-content">
    {breadcrumb([("Home","/"),("Service Areas","/locations/"),(name,None)])}
    <h1>Window Cleaning in {name}, CA</h1>
    <p class="lede">Dane Anderson Window Cleaning provides residential and commercial window cleaning throughout {name} and the surrounding coastal corridor. Fully insured, locally based, and built for the salt air this coastline sees year-round.</p>
    <a href="tel:{PHONE_TEL}" class="btn btn-cta">&#128222; Call {PHONE_DISPLAY}</a>
  </div>
</section>
<section style="background:var(--white)">
<div class="wrap">
<div class="content-grid">
<div class="prose">
<h2>Local Window Cleaning for {name}</h2>
<p>{c['context']}</p>
<p>We regularly service homes and businesses in {c['neighborhoods']}, and our crews know which properties along {c['corridors']} tend to need more frequent attention based on their sun and wind exposure. That local knowledge shapes the cleaning frequency and treatment approach we recommend, rather than applying one blanket schedule to every address.</p>
<p>Whether you are a homeowner noticing a hazy film on the living room glass or a property manager overseeing several commercial units, the same purified-water process applies, adjusted for the specific exposure and window style at your address. We keep detailed notes on returning accounts so each visit builds on what we learned about the property the time before, rather than starting from scratch every visit.</p>
<div style="background:var(--sand-deep);border-radius:10px;padding:16px 20px;margin:20px 0;border-left:3px solid var(--sky)">
<p style="font-size:.88rem;color:var(--muted);margin:0"><strong style="color:var(--dark)">Local resources:</strong> <a href="{gov_url}" target="_blank" rel="noopener">{gov_name}</a> &bull; <a href="{cham_url}" target="_blank" rel="noopener">{cham_name}</a> &bull; <a href="{civic_url}" target="_blank" rel="noopener">{civic_name}</a></p>
</div>
<h3>Local Climate &amp; Exposure</h3>
<p>{c['climate']}</p>
<h3>Property Landscape</h3>
<p>{c['landscape']}</p>
<h3>Services Available Here</h3>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:12px;margin-bottom:28px">
<a href="/services/residential-window-cleaning/" style="display:flex;align-items:center;gap:8px;padding:12px;background:var(--sand-deep);border-radius:8px;font-weight:600;font-size:.9rem;color:var(--navy)">&#127968; Residential Window Cleaning</a>
<a href="/services/commercial-window-cleaning/" style="display:flex;align-items:center;gap:8px;padding:12px;background:var(--sand-deep);border-radius:8px;font-weight:600;font-size:.9rem;color:var(--navy)">&#127970; Commercial Window Cleaning</a>
<a href="/services/screen-cleaning-repair/" style="display:flex;align-items:center;gap:8px;padding:12px;background:var(--sand-deep);border-radius:8px;font-weight:600;font-size:.9rem;color:var(--navy)">&#128737; Screen Cleaning &amp; Repair</a>
<a href="/services/hard-water-stain-removal/" style="display:flex;align-items:center;gap:8px;padding:12px;background:var(--sand-deep);border-radius:8px;font-weight:600;font-size:.9rem;color:var(--navy)">&#128167; Hard Water Stain Removal</a>
<a href="/services/gutter-cleaning/" style="display:flex;align-items:center;gap:8px;padding:12px;background:var(--sand-deep);border-radius:8px;font-weight:600;font-size:.9rem;color:var(--navy)">&#127960; Gutter Cleaning</a>
</div>
{case_study(case_title, case_sit, case_app, case_out)}
<h3>What a Visit Looks Like</h3>
<div class="steps-list">
<div class="step-item"><div class="step-num">1</div><div><h4>Call for a quote</h4><p>Describe the property and we give a straightforward price range on the phone.</p></div></div>
<div class="step-item"><div class="step-num">2</div><div><h4>Scheduling</h4><p>We book a visit window that fits your route day in this part of the coast, often within the same week.</p></div></div>
<div class="step-item"><div class="step-num">3</div><div><h4>On-site service</h4><p>Interior and exterior glass, tracks, and screens are cleaned using purified water-fed systems for upper stories.</p></div></div>
<div class="step-item"><div class="step-num">4</div><div><h4>Walkthrough</h4><p>We point out anything worth watching, such as early hard water spotting or a screen needing repair.</p></div></div>
</div>
<h3>Booking and Scheduling Notes</h3>
<p>Because this area is a regular part of our route, we typically service it on set days each week rather than purely on demand, which keeps travel efficient and pricing consistent for everyone on that route. First-time customers can usually get on the schedule within a few days of calling, and recurring accounts are simply added to the existing route rotation without any special coordination needed on the customer's end.</p>
<h3>Pricing for This Area</h3>
<p>Pricing is based on window count, style, and accessibility rather than a flat citywide rate, since a compact cottage and a large bluff-top home require very different amounts of work. Most residential visits in this part of the service area are quoted over the phone without an in-person estimate, and commercial accounts receive a custom quote based on glass square footage and desired visit frequency. Call and describe the property for an honest number before we ever schedule a visit.</p>
<h3>Nearby Areas We Also Serve</h3>
<p>Our route through this stretch of the coast also regularly covers <a href="/locations/{n1_slug}/">{n1_name}</a> and <a href="/locations/{n2_slug}/">{n2_name}</a>, and properties in between are typically scheduled on the same visit day for efficiency. If your address falls between two of our listed service areas, call and we will confirm coverage.</p>
<h3>Why Local Knowledge Matters</h3>
<p>A window cleaning company that only passes through occasionally has no real basis for recommending the right cleaning frequency or catching an early hard water problem before it becomes expensive to fix. Because we service this area on a regular route rather than as an occasional out-of-territory job, we build up a working knowledge of which specific streets and building types need more frequent attention, information that simply is not available to a crew showing up for the first and only time. That local pattern recognition is part of what customers are paying for beyond the cleaning itself.</p>
{faq_block(faqs)}
</div>
<div class="sidebar">
<div class="cta-card"><h3>Get a Fast Quote</h3><p>Serving this area regularly.</p><a href="tel:{PHONE_TEL}" class="btn btn-cta">&#128222; {PHONE_DISPLAY}</a></div>
<div class="sidebar-card"><h3>Nearby Areas</h3><ul><li><a href="/locations/{n1_slug}/">{n1_name}</a></li><li><a href="/locations/{n2_slug}/">{n2_name}</a></li><li><a href="/locations/">All Areas &rarr;</a></li></ul></div>
<div class="sidebar-card"><h3>All Services</h3><ul><li><a href="/services/residential-window-cleaning/">Residential</a></li><li><a href="/services/commercial-window-cleaning/">Commercial</a></li><li><a href="/services/">View All &rarr;</a></li></ul></div>
</div>
</div>
</div>
</section>
<section style="background:var(--sand-deep)">
<div class="wrap" style="max-width:860px"><p style="line-height:1.85">Local homeowners and businesses get the same purified-water process that has made Dane Anderson Window Cleaning a trusted name along <a href="/">the coastal corridor</a>. Explore our full <a href="/services/">list of services</a> or read about <a href="/blog/how-often-clean-windows-coastal-climate/">how often coastal homes should be cleaned</a> on our blog.</p></div>
</section>
<section class="cta-banner">
<div class="wrap"><h2>Ready for Clearer Windows in {name}?</h2><p>Call now for a fast, honest quote.</p><a href="tel:{PHONE_TEL}" class="cta-phone">{PHONE_DISPLAY}</a><a href="tel:{PHONE_TEL}" class="btn btn-cta">&#128222; Call Now</a></div>
</section>
'''

    schema = [
        {**LOCAL_BUSINESS_BASE, "areaServed": {"@type": "City", "name": f"{name}, CA"}},
        {"@type": "BreadcrumbList", "itemListElement": breadcrumb_schema([("Home","/"),("Service Areas","/locations/"),(name, f"/locations/{slug}/")])},
        faq_schema(faqs),
    ]
    html = page_shell(title, desc, f"/locations/{slug}/", schema, body, show_call_bar=True)
    write_page(f"locations/{slug}/index.html", html)

# ---- locations index ----
cards = "".join(f'<a href="/locations/{slug}/" class="loc-card"><h3>{CITIES[slug]["name"]}</h3><p>Window cleaning &amp; more</p></a>' for slug in ORDER)
title = "Service Areas | Dane Anderson Window Cleaning"
desc = "Dane Anderson Window Cleaning serves Santa Cruz, Capitola, Aptos, Watsonville, Monterey, Pacific Grove, and Carmel-by-the-Sea. Call (831) 224-3387."
body = f'''
<section class="page-hero" style="padding:56px 0">
  <div class="hero-bg"><img src="/images/hero/ocean-wave-aerial.jpg" alt="" role="presentation"><div class="hero-scrim" style="background:linear-gradient(105deg,rgba(11,61,92,.93) 50%,rgba(11,61,92,.6) 100%)"></div></div>
  <div class="wrap hero-content">
    {breadcrumb([("Home","/"),("Service Areas",None)])}
    <h1>Serving the Santa Cruz to Monterey Coastal Corridor</h1>
    <p class="lede">Based in Santa Cruz, we serve homes and businesses across seven coastal communities from Pleasure Point down to Carmel-by-the-Sea.</p>
    <a href="tel:{PHONE_TEL}" class="btn btn-cta">&#128222; Call {PHONE_DISPLAY}</a>
  </div>
</section>
<section style="background:var(--white)">
<div class="wrap">
<span class="section-label">Service Areas</span>
<h2 class="section-title">Choose Your City</h2>
<div class="card-grid">{cards}</div>
</div>
</section>
<section style="background:var(--sand-deep)">
<div class="wrap" style="max-width:820px"><p style="line-height:1.85">Not seeing your town listed? We often service addresses between our listed cities as part of our regular route. Call <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a> to confirm coverage, or browse our full <a href="/services/">list of services</a>.</p></div>
</section>
<section class="cta-banner">
<div class="wrap"><h2>Find Your City Above and Call Today</h2><a href="tel:{PHONE_TEL}" class="cta-phone">{PHONE_DISPLAY}</a><a href="tel:{PHONE_TEL}" class="btn btn-cta">&#128222; Call Now</a></div>
</section>
'''
schema = [LOCAL_BUSINESS_BASE, {"@type": "BreadcrumbList", "itemListElement": breadcrumb_schema([("Home","/"),("Service Areas","/locations/")])}]
html = page_shell(title, desc, "/locations/", schema, body)
write_page("locations/index.html", html)
