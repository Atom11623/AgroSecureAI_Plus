def get_crop_recommendations(crop, soil, weather):
    recommendations = [
        f"📌 Crop: {crop}",
        f"🌡️ Temperature: {weather['temperature']}°C | 💧 Humidity: {weather['humidity']}%",
        f"☁️ Condition: {weather['description']}"
    ]

    if weather['temperature'] and weather['temperature'] > 35:
        recommendations.append("⚠️ Too hot – delay planting or increase irrigation.")
    if weather['humidity'] and weather['humidity'] < 30:
        recommendations.append("⚠️ Low humidity – apply mulch or irrigate more.")

    seed_advice = {
        "Maize": "SAMMAZ 52 or SAMMAZ 40",
        "Millet": "SOSAT-C88 or LCIC MV 5",
        "Rice": "FARO 44 (lowland) or NERICA 4 (upland)",
        "Tomato": "UC82B or Roma VF",
        "Cowpea": "SAMPEA 14 or 8",
        "Onion": "Red Creole or Galmi",
        "Groundnut": "SAMNUT 24 or 26",
        "Sorghum": "SAMSORG 45",
        "Soybean": "TGX 1835-10E"
    }

    soil_types = {
        "Maize": "Loamy",
        "Millet": "Sandy",
        "Rice": "Clay",
        "Tomato": "Sandy loam",
        "Cowpea": "Sandy",
        "Onion": "Sandy loam",
        "Groundnut": "Sandy",
        "Sorghum": "Loamy",
        "Soybean": "Loamy"
    }

    pesticide_recs = {
        "Maize": "Lambda-cyhalothrin or Emamectin benzoate",
        "Millet": "Neem-based spray or Dimethoate",
        "Rice": "Mancozeb or Carbofuran",
        "Tomato": "Actara or Ridomil Gold",
        "Cowpea": "Cypermethrin and Imidacloprid",
        "Onion": "Carbendazim or Malathion",
        "Groundnut": "Actara or Chlorpyrifos",
        "Sorghum": "Permethrin or Cypermethrin",
        "Soybean": "Carbaryl or Metalaxyl"
    }

    seed = seed_advice.get(crop, "Improved variety")
    soil_needed = soil_types.get(crop, "Loamy")
    pesticide = pesticide_recs.get(crop, "Use certified, crop-specific pesticides")

    recommendations.append(f"🌱 Recommended Seed: {seed}")
    if soil.lower() != soil_needed.lower():
        recommendations.append(f"⚠️ Optimal soil for {crop} is {soil_needed}.")
    else:
        recommendations.append("✅ Suitable soil type for this crop.")

    recommendations.append(f"💊 Recommended Pesticide: {pesticide}")

    return recommendations
