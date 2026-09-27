import json, os, requests, sys
from PIL import Image
from io import BytesIO

BASE = "/Volumes/samsung/_WEB/ClaudeCode/clients/dane-anderson-window-cleaning/site/images"
UNSPLASH_KEY = json.load(open("/Volumes/samsung/_WEB/ClaudeCode/credentials/unsplash_agency.json"))["access_key"]
PEXELS_KEY = json.load(open("/Volumes/samsung/_WEB/ClaudeCode/credentials/pexels_agency.json"))["api_key"]

def unsplash_search(query, per_page=5):
    r = requests.get("https://api.unsplash.com/search/photos",
                      headers={"Authorization": f"Client-ID {UNSPLASH_KEY}"},
                      params={"query": query, "per_page": per_page, "orientation": "landscape"})
    r.raise_for_status()
    return r.json().get("results", [])

def pexels_search(query, per_page=5):
    r = requests.get("https://api.pexels.com/v1/search",
                      headers={"Authorization": PEXELS_KEY},
                      params={"query": query, "per_page": per_page, "orientation": "landscape"})
    r.raise_for_status()
    return r.json().get("photos", [])

def save_optimized(url, path, max_w=1920, quality=80):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    img = Image.open(BytesIO(r.content)).convert("RGB")
    if img.width > max_w:
        h = int(img.height * (max_w / img.width))
        img = img.resize((max_w, h), Image.LANCZOS)
    img.save(path, "JPEG", quality=quality, optimize=True)
    print("saved", path, img.size)

# jobs: (query, source, index_pick, out_path)
jobs = [
    ("Santa Cruz California coastline boardwalk", "unsplash", 0, f"{BASE}/hero/santa-cruz-coastline.jpg"),
    ("Monterey Bay California ocean", "unsplash", 0, f"{BASE}/hero/monterey-bay-coastline.jpg"),
    ("Capitola California beach village", "unsplash", 0, f"{BASE}/hero/capitola-village-beach.jpg"),
    ("Aptos California coast redwoods", "unsplash", 0, f"{BASE}/hero/aptos-california-coast.jpg"),
    ("Watsonville California farmland valley", "unsplash", 0, f"{BASE}/hero/watsonville-agricultural-valley.jpg"),
    ("Pacific Grove California coast rocks", "unsplash", 0, f"{BASE}/hero/pacific-grove-coast.jpg"),
    ("Carmel by the Sea California", "unsplash", 0, f"{BASE}/hero/carmel-by-the-sea.jpg"),
    ("California coastal home exterior", "unsplash", 0, f"{BASE}/hero/homepage-hero-coastal-home.jpg"),
    ("Santa Cruz wharf sunset", "unsplash", 0, f"{BASE}/hero/about-hero-santa-cruz-wharf.jpg"),
    ("ocean wave surf close up", "unsplash", 0, f"{BASE}/hero/ocean-wave-texture.jpg"),
    ("ocean wave aerial blue", "unsplash", 0, f"{BASE}/hero/ocean-wave-aerial.jpg"),
    ("window cleaner squeegee glass", "unsplash", 0, f"{BASE}/services/window-cleaner-squeegee-closeup.jpg"),
    ("professional window washing house", "unsplash", 0, f"{BASE}/services/residential-window-cleaning-progress.jpg"),
    ("commercial building glass cleaning", "unsplash", 0, f"{BASE}/services/commercial-window-cleaning-storefront.jpg"),
    ("gutter cleaning ladder house", "pexels", 0, f"{BASE}/services/gutter-cleaning-ladder.jpg"),
    ("clean modern house windows exterior", "unsplash", 0, f"{BASE}/services/clean-house-windows-exterior.jpg"),
    ("window screen mesh close up", "pexels", 0, f"{BASE}/services/window-screen-repair.jpg"),
    ("water droplets glass window", "unsplash", 0, f"{BASE}/services/hard-water-spots-glass.jpg"),
    ("squeegee window washing closeup", "pexels", 0, f"{BASE}/services/squeegee-closeup-2.jpg"),
    ("beach house windows ocean view", "unsplash", 0, f"{BASE}/services/ocean-view-windows-home.jpg"),
]

for query, source, idx, out in jobs:
    try:
        if source == "unsplash":
            results = unsplash_search(query)
            if not results:
                print("NO RESULTS", query); continue
            url = results[idx]["urls"]["regular"]
        else:
            results = pexels_search(query)
            if not results:
                print("NO RESULTS", query); continue
            url = results[idx]["src"]["large2x"]
        save_optimized(url, out)
    except Exception as e:
        print("ERROR", query, e)
