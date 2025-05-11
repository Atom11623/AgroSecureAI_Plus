def get_storage_guide(crop):
    guide = {
        "Maize": ["Dry to 12-13% moisture", "Store in sealed bags or silos"],
        "Tomato": ["Use cold storage below 15°C", "Avoid plastic bags to reduce spoilage"],
        "Cowpea": ["Use PICS bags", "Ensure room is dry and rodent-proof"],
        "Rice": ["Dry properly before bagging", "Use jute bags"],
        "Onion": ["Dry outer layers before storage", "Keep in ventilated baskets"],
        "Groundnut": ["Store pods in cool, dry place", "Avoid damp sacks"]
    }
    return guide.get(crop, ["Store in cool, dry, well-ventilated area."])
