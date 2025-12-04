import requests
import os
import urllib.request

#I have removed my unsplash key for privacy reasons
ACCESS_KEY = ""  
BASE_DIR = "."  

KEYWORDS = {
    "fire": [
        "wildfire flames",
        "forest fire",
        "burning forest",
        "bushfire flames",
        "wildfire emergency",
        "forest blaze",
        "wildfire aerial",
        "fire disaster",
        "forest wildfire aerial",
        "flames in forest",
        "burning trees",
        "fire outbreak forest"
    ],
    "smoke": [
        "wildfire smoke",
        "forest smoke haze",
        "smoke plumes",
        "heavy outdoor smoke",
        "forest haze pollution",
        "smoke in forest",
        "smoky forest landscape",
        "wildfire smoke aerial",
        "forest smoke aerial",
        "smoky wildfire",
        "smoke over forest",
        "forest haze morning"
    ],
    "no_fire": [
        "healthy green forest",
        "dense forest landscape",
        "mountain forest scenery",
        "forest nature photography",
        "woodland trail",
        "sunlit forest",
        "forest path trail",
        "river forest landscape",
        "sunlight forest trail",
        "peaceful forest scene",
        "forest path sunlight",
        "lush green forest"
    ]
}

IMAGES_PER_REQUEST = 30  
PAGE = 1  

def download_images(keyword, save_folder):
    url = (
        f"https://api.unsplash.com/search/photos"
        f"?query={keyword}&per_page={IMAGES_PER_REQUEST}&page={PAGE}"
        f"&client_id={ACCESS_KEY}"
    )

    try:
        response = requests.get(url).json()
    except Exception as e:
        print("Request failed for keyword:", keyword, "| Error:", e)
        return 0

    if "results" not in response:
        return 0

    count = 0
    for img in response["results"]:
        img_url = img["urls"]["regular"]
        filename = f"{save_folder}/{keyword.replace(' ', '_')}_{count}.jpg"
        try:
            urllib.request.urlretrieve(img_url, filename)
            count += 1
        except:
            continue

    return count

total_images = 0

for category, keywords_list in KEYWORDS.items():
    folder = f"{BASE_DIR}/{category}"
    print(f"Collecting images for category: {category}")

    for kw in keywords_list:
        collected = download_images(kw, folder)
        print(f"Keyword: {kw} | Images downloaded: {collected}")
        total_images += collected

print(f"\nCollection complete. Total images downloaded: {total_images}")
