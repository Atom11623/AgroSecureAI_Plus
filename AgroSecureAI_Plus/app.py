import streamlit as st
from modules.translator import detect_language, translate_to_english, translate_to_hausa
from modules.weather import get_weather
from modules.crop_advisor import get_crop_recommendations
from modules.security import STATES_AND_LGAS, get_threat_zones
from modules.economics import estimate_revenue
from modules.storage import get_storage_guide

st.set_page_config(page_title="AgroSecure AI+", layout="wide")
st.title("🌾 AgroSecure AI+ – Expert Farming Support for Northern Nigeria")
st.markdown("Empowering farmers with data-driven crop, security, and market insights.")

api_key = st.secrets["OPENWEATHER_API"]

# Language handling
query = st.text_input("Ask your question (Hausa or English):")
if query:
    lang = detect_language(query)
    query_en = translate_to_english(query) if lang != "en" else query
    st.write(f"📘 Detected language: {'Hausa' if lang == 'ha' else 'English'}")

# Location input
state = st.selectbox("Select your state", list(STATES_AND_LGAS.keys()))
lga = st.selectbox("Select your Local Government Area (LGA)", STATES_AND_LGAS[state])

# Crop selection and weather integration
crop = st.selectbox("Select your crop", ["Maize", "Millet", "Sorghum", "Rice", "Cowpea", "Groundnut", "Tomato", "Soybean", "Onion"])
soil = st.selectbox("Your farm's soil type", ["Loamy", "Sandy", "Clay", "Other"])
hectares = st.number_input("Enter your farm size in hectares", min_value=0.1, value=1.0, step=0.1)

if st.button("Get Expert Recommendations"):
    weather = get_weather(state, api_key)
    crop_advice = get_crop_recommendations(crop, soil, weather)
    security_info = get_threat_zones(state, lga)
    revenue_forecast = estimate_revenue(crop, hectares)
    storage_advice = get_storage_guide(crop)

    st.subheader("🌾 Crop Advice")
    st.write("\n".join(crop_advice))

    st.subheader("🛡️ Security Risk (LGA level)")
    st.write("\n".join(security_info))

    st.subheader("📦 Storage Tips")
    st.write("\n".join(storage_advice))

    st.subheader("💰 Revenue Estimate")
    st.write(revenue_forecast)

    if lang == "ha":
        st.subheader("🔄 Hausa Translation")
        hausa_translation = translate_to_hausa("\n".join(crop_advice + security_info + storage_advice))
        st.write(hausa_translation)
