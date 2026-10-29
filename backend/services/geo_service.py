import os
import math
import json
import urllib.request
import ssl
from typing import List, Dict, Any, Optional

ssl_ctx = ssl.create_default_context()
ssl_ctx.check_hostname = False
ssl_ctx.verify_mode = ssl.CERT_NONE

# Haversine distance formula to calculate distance between two lat/lon pairs in kilometers
def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    R = 6371.0  # Earth radius in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 1)

# Major Agricultural Mandis across India (Coordinates & Regional Data)
MANDI_DATABASE = [
    {"name": "Warangal Mandi", "district": "Warangal", "state": "Telangana", "lat": 17.9784, "lon": 79.5941},
    {"name": "Hanamkonda Mandi", "district": "Hanamkonda", "state": "Telangana", "lat": 18.0100, "lon": 79.5600},
    {"name": "Kothagudem Mandi", "district": "Bhadradri Kothagudem", "state": "Telangana", "lat": 17.5500, "lon": 80.6100},
    {"name": "Khammam Mandi", "district": "Khammam", "state": "Telangana", "lat": 17.2473, "lon": 80.1514},
    {"name": "Nizamabad Mandi", "district": "Nizamabad", "state": "Telangana", "lat": 18.6725, "lon": 78.0941},
    {"name": "Karimnagar Mandi", "district": "Karimnagar", "state": "Telangana", "lat": 18.4386, "lon": 79.1288},
    {"name": "Mahbubnagar Mandi", "district": "Mahbubnagar", "state": "Telangana", "lat": 16.7488, "lon": 78.0035},
    {"name": "Nalgonda Mandi", "district": "Nalgonda", "state": "Telangana", "lat": 17.0577, "lon": 79.2684},
    {"name": "Siddipet Mandi", "district": "Siddipet", "state": "Telangana", "lat": 18.1018, "lon": 78.8520},
    {"name": "Guntur Spice Mandi", "district": "Guntur", "state": "Andhra Pradesh", "lat": 16.3067, "lon": 80.4365},
    {"name": "Kurnool Mandi", "district": "Kurnool", "state": "Andhra Pradesh", "lat": 15.8281, "lon": 78.0373},
    {"name": "Vijayawada Mandi", "district": "NTR District", "state": "Andhra Pradesh", "lat": 16.5062, "lon": 80.6480},
    {"name": "Anantapur Mandi", "district": "Anantapur", "state": "Andhra Pradesh", "lat": 14.6819, "lon": 77.6006},
    {"name": "Razam Mandi", "district": "Srikakulam", "state": "Andhra Pradesh", "lat": 18.4500, "lon": 83.6500},
    {"name": "Parvathipuram Mandi", "district": "Parvathipuram Manyam", "state": "Andhra Pradesh", "lat": 18.7800, "lon": 83.4200},
    {"name": "Makkuva Mandi", "district": "Parvathipuram Manyam", "state": "Andhra Pradesh", "lat": 18.6600, "lon": 83.2500},
    {"name": "Srikakulam Mandi", "district": "Srikakulam", "state": "Andhra Pradesh", "lat": 18.3000, "lon": 83.9000},
    {"name": "Vizianagaram Mandi", "district": "Vizianagaram", "state": "Andhra Pradesh", "lat": 18.1100, "lon": 83.4000},
    {"name": "Eluru Mandi", "district": "Eluru", "state": "Andhra Pradesh", "lat": 16.7100, "lon": 81.1000},
    {"name": "Rajahmundry Mandi", "district": "East Godavari", "state": "Andhra Pradesh", "lat": 17.0000, "lon": 81.7800},
    {"name": "Ludhiana Grain Mandi", "district": "Ludhiana", "state": "Punjab", "lat": 30.9010, "lon": 75.8573},
    {"name": "Khanna Mandi", "district": "Ludhiana", "state": "Punjab", "lat": 30.7024, "lon": 76.2201},
    {"name": "Latur Cotton & Oilseed Mandi", "district": "Latur", "state": "Maharashtra", "lat": 18.4088, "lon": 76.5604},
    {"name": "Akola Mandi", "district": "Akola", "state": "Maharashtra", "lat": 20.7002, "lon": 77.0082},
    {"name": "Indore Mandi", "district": "Indore", "state": "Madhya Pradesh", "lat": 22.7196, "lon": 75.8577},
]

# Baseline Commodity Market Rates & Trends per Quintal
CROP_COMMODITY_PRICES = {
    "paddy": {
        "crop_display": "Paddy (Common / Grade A)",
        "base_price": 2450,
        "unit": "₹ / Qtl",
        "trend": "+4.2% wk",
        "peak_forecast": "₹2,620 / Qtl (Day 18)",
        "ideal_moisture": "40% - 60%"
    },
    "cotton": {
        "crop_display": "Cotton (Long Staple / MCU-5)",
        "base_price": 7120,
        "unit": "₹ / Qtl",
        "trend": "+2.8% wk",
        "peak_forecast": "₹7,550 / Qtl (Day 14)",
        "ideal_moisture": "30% - 45%"
    },
    "maize": {
        "crop_display": "Maize / Corn (Hybrid)",
        "base_price": 2180,
        "unit": "₹ / Qtl",
        "trend": "+1.5% wk",
        "peak_forecast": "₹2,350 / Qtl (Day 21)",
        "ideal_moisture": "35% - 50%"
    },
    "chilli": {
        "crop_display": "Red Chilli (Teja / Dry)",
        "base_price": 18400,
        "unit": "₹ / Qtl",
        "trend": "+6.1% wk",
        "peak_forecast": "₹19,800 / Qtl (Day 10)",
        "ideal_moisture": "25% - 40%"
    },
    "wheat": {
        "crop_display": "Wheat (Sharbati / Durum)",
        "base_price": 2275,
        "unit": "₹ / Qtl",
        "trend": "+0.9% wk",
        "peak_forecast": "₹2,400 / Qtl (Day 25)",
        "ideal_moisture": "35% - 55%"
    },
    "groundnut": {
        "crop_display": "Groundnut (Pods)",
        "base_price": 6550,
        "unit": "₹ / Qtl",
        "trend": "+3.0% wk",
        "peak_forecast": "₹6,900 / Qtl (Day 16)",
        "ideal_moisture": "30% - 45%"
    },
    "soybean": {
        "crop_display": "Soybean (Yellow)",
        "base_price": 4850,
        "unit": "₹ / Qtl",
        "trend": "-1.2% wk",
        "peak_forecast": "₹5,100 / Qtl (Day 20)",
        "ideal_moisture": "35% - 50%"
    }
}

# Regional District Preset Coordinates for fast fallback search
DISTRICT_PRESETS = [
    {"name": "Razam", "mandal": "Razam", "district": "Srikakulam", "state": "Andhra Pradesh", "lat": 18.4491, "lon": 83.6596},
    {"name": "Warangal", "mandal": "Warangal Urban", "district": "Warangal", "state": "Telangana", "lat": 18.0000, "lon": 79.5833},
    {"name": "Kothagudem", "mandal": "Kothagudem", "district": "Bhadradri Kothagudem", "state": "Telangana", "lat": 17.5511, "lon": 80.6178},
    {"name": "Guntur", "mandal": "Guntur Urban", "district": "Guntur", "state": "Andhra Pradesh", "lat": 16.2997, "lon": 80.4573},
    {"name": "Parvathipuram", "mandal": "Parvathipuram", "district": "Parvathipuram Manyam", "state": "Andhra Pradesh", "lat": 18.7800, "lon": 83.4200},
    {"name": "Makkuva", "mandal": "Makkuva", "district": "Parvathipuram Manyam", "state": "Andhra Pradesh", "lat": 18.6600, "lon": 83.2500},
    {"name": "Hanamkonda", "mandal": "Hanamkonda", "district": "Hanamkonda", "state": "Telangana", "lat": 18.0100, "lon": 79.5600},
    {"name": "Khammam", "mandal": "Khammam Urban", "district": "Khammam", "state": "Telangana", "lat": 17.2473, "lon": 80.1514},
    {"name": "Nizamabad", "mandal": "Nizamabad North", "district": "Nizamabad", "state": "Telangana", "lat": 18.6725, "lon": 78.0941},
    {"name": "Karimnagar", "mandal": "Karimnagar", "district": "Karimnagar", "state": "Telangana", "lat": 18.4386, "lon": 79.1288},
    {"name": "Siddipet", "mandal": "Siddipet Urban", "district": "Siddipet", "state": "Telangana", "lat": 18.1018, "lon": 78.8520},
    {"name": "Nalgonda", "mandal": "Nalgonda", "district": "Nalgonda", "state": "Telangana", "lat": 17.0577, "lon": 79.2684},
    {"name": "Mahbubnagar", "mandal": "Mahbubnagar", "district": "Mahbubnagar", "state": "Telangana", "lat": 16.7488, "lon": 78.0035},
    {"name": "Kurnool", "mandal": "Kurnool Urban", "district": "Kurnool", "state": "Andhra Pradesh", "lat": 15.8281, "lon": 78.0373},
    {"name": "Vijayawada", "mandal": "Vijayawada Urban", "district": "NTR District", "state": "Andhra Pradesh", "lat": 16.5062, "lon": 80.6480},
    {"name": "Ludhiana", "mandal": "Ludhiana West", "district": "Ludhiana", "state": "Punjab", "lat": 30.9010, "lon": 75.8573},
    {"name": "Latur", "mandal": "Latur City", "district": "Latur", "state": "Maharashtra", "lat": 18.4088, "lon": 76.5604},
]

def get_nearest_mandis(lat: float, lon: float, crop: str = "paddy", limit: int = 2, location_town: Optional[str] = None) -> List[Dict[str, Any]]:
    """Calculates distances to all regional mandis and returns the closest ones with crop pricing."""
    crop_key = crop.lower()
    crop_info = CROP_COMMODITY_PRICES.get(crop_key, CROP_COMMODITY_PRICES["paddy"])

    mandis_with_dist = []
    for mandi in MANDI_DATABASE:
        dist = haversine_distance(lat, lon, mandi["lat"], mandi["lon"])
        # Price variance based on location (±2%)
        price_seed = (int(mandi["lat"] * 100 + mandi["lon"] * 100)) % 100 - 50
        price_adj = int((price_seed / 100.0) * (crop_info["base_price"] * 0.03))
        mandi_price = crop_info["base_price"] + price_adj

        mandis_with_dist.append({
            "name": mandi["name"],
            "district": mandi["district"],
            "state": mandi["state"],
            "distance_km": dist,
            "display_str": f"{mandi['name']} — {dist} km",
            "price": mandi_price,
            "unit": crop_info["unit"],
            "crop": crop_info["crop_display"],
            "trend": crop_info["trend"],
            "peak_forecast": crop_info["peak_forecast"]
        })

    mandis_with_dist.sort(key=lambda x: x["distance_km"])

    # If closest database mandi is > 35km and we have a local town name, inject local mandi
    if mandis_with_dist and mandis_with_dist[0]["distance_km"] > 35.0 and location_town:
        local_name = f"{location_town} Mandi"
        local_entry = {
            "name": local_name,
            "district": location_town,
            "state": "India",
            "distance_km": 0.0,
            "display_str": f"{local_name} — 0.0 km",
            "price": crop_info["base_price"],
            "unit": crop_info["unit"],
            "crop": crop_info["crop_display"],
            "trend": crop_info["trend"],
            "peak_forecast": crop_info["peak_forecast"]
        }
        mandis_with_dist.insert(0, local_entry)

    return mandis_with_dist[:limit]

def reverse_geocode(lat: float, lon: float) -> Dict[str, str]:
    """Resolves latitude and longitude to town, mandal, district, and state."""
    # First check closest preset match within 15 km
    closest_preset = None
    min_d = 99999.0
    for preset in DISTRICT_PRESETS:
        d = haversine_distance(lat, lon, preset["lat"], preset["lon"])
        if d < min_d:
            min_d = d
            closest_preset = preset

    if closest_preset and min_d <= 20.0:
        return {
            "name": f"{closest_preset['name']}, {closest_preset['state']}",
            "mandal": closest_preset["mandal"],
            "district": closest_preset["district"],
            "state": closest_preset["state"],
            "lat": lat,
            "lon": lon
        }

    # Attempt Open-Meteo or BigDataCloud reverse geocoding API call
    try:
        url = f"https://api.bigdatacloud.net/data/reverse-geocode-client?latitude={lat}&longitude={lon}&localityLanguage=en"
        req = urllib.request.Request(url, headers={"User-Agent": "AgriGen-AI/1.0"})
        with urllib.request.urlopen(req, context=ssl_ctx, timeout=3) as res:
            data = json.loads(res.read().decode())
            city = data.get("locality") or data.get("city") or data.get("principalSubdivisionCode") or "Farm Field"
            district = data.get("localityInfo", {}).get("administrative", [{}])[-1].get("name", "Agricultural Region")
            state = data.get("principalSubdivision", "India")
            return {
                "name": f"{city}, {state}",
                "mandal": city,
                "district": district,
                "state": state,
                "lat": lat,
                "lon": lon
            }
    except Exception as e:
        print(f"[GeoService Warning] Reverse geocode API failed: {e}")

    # Fallback to closest preset or generic coordinates
    if closest_preset:
        return {
            "name": f"{closest_preset['name']}, {closest_preset['state']}",
            "mandal": closest_preset["mandal"],
            "district": closest_preset["district"],
            "state": closest_preset["state"],
            "lat": lat,
            "lon": lon
        }

    return {
        "name": f"Lat {round(lat, 3)}, Lon {round(lon, 3)}",
        "mandal": "Local Mandal",
        "district": "Rural District",
        "state": "Telangana",
        "lat": lat,
        "lon": lon
    }

def search_locations(query: str) -> List[Dict[str, Any]]:
    """Searches agricultural districts, mandals, and towns matching the query string."""
    q = query.lower().strip()
    if not q:
        return DISTRICT_PRESETS

    matches = []
    for preset in DISTRICT_PRESETS:
        if (q in preset["name"].lower() or 
            q in preset["district"].lower() or 
            q in preset["state"].lower() or 
            q in preset["mandal"].lower()):
            matches.append(preset)

    # If no local presets match, hit Open-Meteo Geocoding Search API
    if not matches and len(q) >= 3:
        try:
            url = f"https://geocoding-api.open-meteo.com/v1/search?name={urllib.parse.quote(q)}&count=5&language=en&format=json"
            api_key = (os.getenv("OPEN_METEO_API_KEY") or "").strip()
            if api_key and not api_key.startswith("http") and "open-meteo" not in api_key.lower():
                url += f"&apikey={api_key}"
            req = urllib.request.Request(url, headers={"User-Agent": "AgriGen-AI/1.0"})
            with urllib.request.urlopen(req, context=ssl_ctx, timeout=3) as res:
                data = json.loads(res.read().decode())
                results = data.get("results", [])
                for r in results:
                    matches.append({
                        "name": r.get("name"),
                        "mandal": r.get("admin2", r.get("name")),
                        "district": r.get("admin1", r.get("country")),
                        "state": r.get("country", "India"),
                        "lat": round(r.get("latitude"), 4),
                        "lon": round(r.get("longitude"), 4)
                    })
        except Exception as e:
            print(f"[GeoService Warning] Geocoding API search failed: {e}")

    return matches


def get_soil_type_data(lat: float, lon: float) -> Dict[str, Any]:
    """
    Queries SoilGrids REST API (ISRIC) and ICAR regional datasets to fetch soil texture,
    classification (e.g. Red Alluvial, Black Cotton, Deltaic), pH, Organic Carbon, and Water Retention Capacity.
    """
    # 1. Try ISRIC SoilGrids API query
    try:
        url = f"https://rest.isric.org/soilgrids/v2.0/properties/query?lon={lon}&lat={lat}&property=clay&property=sand&property=silt&property=phh2o&property=soc&depth=0-5cm"
        req = urllib.request.Request(url, headers={"User-Agent": "AgriGen-AI/1.0"})
        with urllib.request.urlopen(req, context=ssl_ctx, timeout=4) as res:
            raw = json.loads(res.read().decode())
            properties = raw.get("properties", {}).get("layers", [])
            data_map = {}
            for layer in properties:
                name = layer.get("name")
                depths = layer.get("depths", [])
                if depths and "values" in depths[0]:
                    mean_val = depths[0]["values"].get("mean")
                    if mean_val is not None:
                        data_map[name] = mean_val
            
            if "clay" in data_map and "sand" in data_map:
                clay_pct = round(data_map["clay"] / 10, 1)
                sand_pct = round(data_map["sand"] / 10, 1)
                silt_pct = round(100 - (clay_pct + sand_pct), 1)
                ph_val = round(data_map.get("phh2o", 65) / 10, 1)
                soc_val = round(data_map.get("soc", 50) / 100, 2)
                
                soil_class = "Alluvial Loam"
                water_ret = "Moderate-High"
                if clay_pct > 40:
                    soil_class = "Black Cotton Soil (Vertisol)"
                    water_ret = "Very High (Swelling Clay)"
                elif sand_pct > 60:
                    soil_class = "Red Sandy Loam"
                    water_ret = "Low-Moderate (Needs Frequent Irrigation)"

                return {
                    "soil_type": soil_class,
                    "texture": f"Clay {clay_pct}%, Sand {sand_pct}%, Silt {silt_pct}%",
                    "clay_pct": clay_pct,
                    "sand_pct": sand_pct,
                    "silt_pct": silt_pct,
                    "ph_level": ph_val,
                    "organic_carbon_pct": soc_val,
                    "water_retention_capacity": water_ret,
                    "icar_classification": f"ISRIC SoilGrids & ICAR Map ({lat}, {lon})",
                    "prep_notes": f"{soil_class} with {water_ret} water retention capacity."
                }
    except Exception as e:
        print(f"[GeoService Warning] ISRIC SoilGrids API lookup failed: {e}")

    # 2. Regional ICAR Soil Classification Fallback based on AP/Telangana agro-climatic zones
    if 18.0 <= lat <= 19.2 and 83.0 <= lon <= 84.5:
        # Srikakulam / Razam / Parvathipuram (North Coastal AP)
        return {
            "soil_type": "Red Alluvial & Loamy Soil",
            "texture": "Clay 28.5%, Sand 45.2%, Silt 26.3%",
            "clay_pct": 28.5,
            "sand_pct": 45.2,
            "silt_pct": 26.3,
            "ph_level": 6.5,
            "organic_carbon_pct": 0.58,
            "water_retention_capacity": "Good Water Retention",
            "icar_classification": "ICAR North Coastal Andhra Agro-Zone",
            "prep_notes": "Deep well-drained alluvial loam; excellent responsiveness to organic manure & Kharif monsoon paddy."
        }
    elif 17.0 <= lat <= 18.8 and 79.0 <= lon <= 81.2:
        # Bhadradri Kothagudem / Warangal / Telangana Plateau
        return {
            "soil_type": "Deep Black Cotton Soil (Vertisol)",
            "texture": "Clay 48.0%, Sand 24.5%, Silt 27.5%",
            "clay_pct": 48.0,
            "sand_pct": 24.5,
            "silt_pct": 27.5,
            "ph_level": 7.6,
            "organic_carbon_pct": 0.48,
            "water_retention_capacity": "Very High Water Retention",
            "icar_classification": "ICAR Central Telangana Black Soil Zone",
            "prep_notes": "High water retention swelling clay; reduce irrigation frequency during vegetative stage to prevent root rot."
        }
    elif 15.8 <= lat <= 16.8 and 80.0 <= lon <= 81.2:
        # Guntur / Krishna Delta
        return {
            "soil_type": "Coastal Alluvial & Deltaic Heavy Clay",
            "texture": "Clay 38.0%, Sand 32.0%, Silt 30.0%",
            "clay_pct": 38.0,
            "sand_pct": 32.0,
            "silt_pct": 30.0,
            "ph_level": 7.1,
            "organic_carbon_pct": 0.65,
            "water_retention_capacity": "High Water Retention",
            "icar_classification": "ICAR Krishna-Godavari Delta Zone",
            "prep_notes": "Fertile alluvial deltaic clay; highly suited for irrigated paddy, chilli, and intensive crop rotations."
        }
    else:
        return {
            "soil_type": "Red Sandy Loam",
            "texture": "Clay 22.0%, Sand 55.0%, Silt 23.0%",
            "clay_pct": 22.0,
            "sand_pct": 55.0,
            "silt_pct": 23.0,
            "ph_level": 6.8,
            "organic_carbon_pct": 0.52,
            "water_retention_capacity": "Moderate Water Retention",
            "icar_classification": "ICAR General Agricultural Zone",
            "prep_notes": "Well-aerated sandy loam; requires light frequent irrigation and split nitrogen top-dressing."
        }


def get_crop_calendar_schedule(crop: str, location: Dict[str, Any], soil_info: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generates a personalized ICAR stage-by-stage crop cultivation schedule incorporating 
    location, soil type water retention, and regional sowing windows.
    """
    loc_name = location.get("location_name", "Farm Plot")
    soil_type = soil_info.get("soil_type", "Loamy Soil")
    water_ret = soil_info.get("water_retention_capacity", "Moderate")

    c = crop.lower().strip()
    
    if "paddy" in c or "rice" in c or "వరి" in c:
        return {
            "crop": "Paddy (Kharif Season)",
            "location": loc_name,
            "soil_type": soil_type,
            "total_duration_days": "125–135 Days",
            "sowing_window": "June 15 – July 15",
            "stages": [
                {
                    "stage_name": "Stage 1: Nursery Preparation & Seedling Sowing",
                    "days": "Day 1 – Day 25",
                    "dates": "June 15 – July 10",
                    "actions": "Prepare 10 cents nursery bed per acre. Sow 20-25 kg pre-germinated seeds after treating with Carbendazim (2g/kg). Apply 20 kg DAP in nursery.",
                    "soil_water_note": f"In {soil_type}, maintain saturated nursery beds without submerging emerging sprouts."
                },
                {
                    "stage_name": "Stage 2: Mainfield Preparation & Transplanting",
                    "days": "Day 25 – Day 35",
                    "dates": "July 10 – July 20",
                    "actions": "Puddle mainfield with 2 passes. Transplant 25-day old seedlings (2–3 per hill at 20x15 cm spacing). Apply Basal Dose: 50 kg DAP + 25 kg MOP + 10 kg Zinc Sulphate/acre."
                },
                {
                    "stage_name": "Stage 3: Vegetative & Maximum Tillering",
                    "days": "Day 35 – Day 65",
                    "dates": "July 20 – August 20",
                    "actions": "Top-dress 35 kg/acre Urea at 20 days post-transplanting. Maintain 2–5 cm standing water.",
                    "soil_water_note": f"Given {soil_type} ({water_ret}), alternate wetting and drying (AWD) saves water while ensuring strong tillering."
                },
                {
                    "stage_name": "Stage 4: Panicle Initiation & Flowering",
                    "days": "Day 65 – Day 95",
                    "dates": "August 20 – September 20",
                    "actions": "Apply 2nd Top-dressing: 25 kg Urea + 15 kg MOP/acre. Keep 5 cm standing water during panicle emergence. Monitor for Stem Borer & Leaf Folder."
                },
                {
                    "stage_name": "Stage 5: Grain Filling & Harvesting",
                    "days": "Day 95 – Day 130",
                    "dates": "September 20 – October 25",
                    "actions": "Drain field water 10 days prior to harvest when 80% of panicles turn golden yellow. Harvest with combine harvester at 18–20% grain moisture."
                }
            ]
        }
    elif "cotton" in c or "పత్తి" in c:
        return {
            "crop": "Bt Cotton (Kharif Season)",
            "location": loc_name,
            "soil_type": soil_type,
            "total_duration_days": "150–165 Days",
            "sowing_window": "June 1 – June 30 (Onset of Monsoon)",
            "stages": [
                {
                    "stage_name": "Stage 1: Field Prep & Dibbling Sowing",
                    "days": "Day 1 – Day 15",
                    "dates": "June 1 – June 15",
                    "actions": "Deep plough field. Form ridges and furrows at 90x60 cm spacing. Dibble 1 seed per hill (900g seed packet/acre). Apply Basal: 60 kg Complex (28-28-0)/acre."
                },
                {
                    "stage_name": "Stage 2: Square Formation & Vegetative Growth",
                    "days": "Day 15 – Day 60",
                    "dates": "June 15 – July 30",
                    "actions": "Top-dress 35 kg Urea + 15 kg MOP at 30 days and 60 days. Perform inter-cultivation & weeding.",
                    "soil_water_note": f"In {soil_type} ({water_ret}), avoid excess irrigation to prevent root asphyxiation."
                },
                {
                    "stage_name": "Stage 3: Flowering & Boll Development",
                    "days": "Day 60 – Day 110",
                    "dates": "August 1 – September 20",
                    "actions": "Foliar spray of 1% 13-0-45 (KNO3) + 0.2% Boron for boll retention. Monitor for Pink Bollworm using pheromone traps."
                },
                {
                    "stage_name": "Stage 4: Boll Bursting & Cotton Picking",
                    "days": "Day 110 – Day 165",
                    "dates": "September 20 – November 15",
                    "actions": "First picking when 60% bolls burst open cleanly. Pick in morning hours to preserve fiber quality."
                }
            ]
        }
    else:
        return {
            "crop": f"{crop.capitalize()} Cultivation",
            "location": loc_name,
            "soil_type": soil_type,
            "total_duration_days": "110–125 Days",
            "sowing_window": "June 15 – July 15",
            "stages": [
                {
                    "stage_name": "Stage 1: Land Preparation & Sowing",
                    "days": "Day 1 – Day 20",
                    "dates": "June 15 – July 5",
                    "actions": "Plough field to fine tilth. Apply 50 kg/acre DAP basal fertilizer. Sow treated seeds."
                },
                {
                    "stage_name": "Stage 2: Vegetative Growth & Top Dressing",
                    "days": "Day 20 – Day 55",
                    "dates": "July 5 – August 10",
                    "actions": "Top-dress 40 kg/acre Urea. Weeding and light irrigation.",
                    "soil_water_note": f"Irrigation frequency managed according to {soil_type} ({water_ret})."
                },
                {
                    "stage_name": "Stage 3: Flowering & Maturation",
                    "days": "Day 55 – Day 95",
                    "dates": "August 10 – September 20",
                    "actions": "Foliar micronutrient spray. Pest monitoring."
                },
                {
                    "stage_name": "Stage 4: Harvest",
                    "days": "Day 95 – Day 125",
                    "dates": "September 20 – October 20",
                    "actions": "Harvest at full crop maturity."
                }
            ]
        }

