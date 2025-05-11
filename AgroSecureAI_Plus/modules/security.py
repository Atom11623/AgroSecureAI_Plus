STATES_AND_LGAS = {
    "Zamfara": ["Gusau", "Shinkafi", "Zurmi", "Maru"],
    "Kaduna": ["Birnin Gwari", "Chikun", "Igabi", "Zaria"],
    "Katsina": ["Jibia", "Batsari", "Safana", "Kankia"],
    "Sokoto": ["Isa", "Rabah", "Wurno", "Gwadabawa"],
    "Niger": ["Shiroro", "Rafi", "Munya", "Kontagora"],
    "Kano": ["Dambatta", "Kura", "Garko", "Tarauni"],
    "Yobe": ["Gujba", "Damaturu", "Bursari", "Potiskum"],
    "Borno": ["Maiduguri", "Konduga", "Gwoza", "Dikwa"]
}

REMOTE_THREATS = {
    "Zamfara": {"Zurmi": ["Yanbuki", "Kware"], "Shinkafi": ["Badarawa"]},
    "Kaduna": {"Birnin Gwari": ["Doka", "Dogon Dawa"]},
    "Katsina": {"Batsari": ["Dandume", "Zakka"]}
}

def get_threat_zones(state, lga):
    local_threats = REMOTE_THREATS.get(state, {}).get(lga, [])
    if local_threats:
        return [f"🚨 High risk areas in {lga}, {state}: {', '.join(local_threats)}"]
    return ["✅ No high-risk remote areas reported in this LGA."]
