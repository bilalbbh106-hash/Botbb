# === modules/ads.py ===

from database import ads_db

def create_ad(owner_id, url, budget):
    ads_db.insert_one({
        "owner": owner_id,
        "url": url,
        "budget": budget,
        "spent": 0,
        "active": True
    })
