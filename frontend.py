import streamlit as st
import requests

st.title("Price prediction")

state_building = st.selectbox("State of the building", ["GOOD_AS_NEW", "REQUIRES_RENOVATION"])
property_type = st.selectbox("Property type", ["APARTMENT", "HOUSE"])
zip_code = st.number_input("Zip code", min_value=1000, max_value=9999, step=1)
construction_year = st.number_input("Year of construction", min_value=1800, max_value=2024)
nbr_bedrooms = st.number_input("Number of bedrooms", min_value=1, max_value=10)
equipped_kitchen = st.selectbox("State of the kitchen", ["NOT_INSTALLED", "SEMI_EQUIPPED", "EQUIPPED", "HYPER_EQUIPPED"])
fl_furnished = st.checkbox("Furnished")
terrace_sqm = st.number_input("Terrace area (in sqm)", min_value=0.0)
garden_sqm = st.number_input("Garden area (in sqm)", min_value=0.0)
fl_swimming_pool = st.checkbox("Swimming pool")
epc = st.selectbox("EPC rating", ["A++", "A+", "A", "B", "C", "D", "E", "F", "G"])

if st.button("Predict price"):
    data = {
        "state_building": state_building,
        "property_type": property_type,
        "zip_code": zip_code,
        "construction_year": construction_year,
        "nbr_bedrooms": nbr_bedrooms,
        "equipped_kitchen": equipped_kitchen,
        "fl_furnished": fl_furnished,
        "terrace_sqm": terrace_sqm,
        "garden_sqm": garden_sqm,
        "fl_swimming_pool": fl_swimming_pool,
        "epc": epc
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict_price", json=data)
        result = response.json()
        st.success(f"Predicted price: {result}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
