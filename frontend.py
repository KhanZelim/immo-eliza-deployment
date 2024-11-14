import streamlit as st
import requests

st.title("Wages test")

salary = st.number_input("Enter your salary:", min_value=0.0, format="%.2f")
bonus = st.number_input("Enter your bonus:", min_value=0.0, format="%.2f")
taxes = st.number_input("Enter your taxes:", min_value=0.0, format="%.2f")

if st.button("Calculate wage"):
    data = {
        "salary": salary,
        "bonus": bonus,
        "taxes": taxes
    }

    try:
        response = requests.post("http://127.0.0.1:8000/calculate_wage", json=data)
        result = response.json()
        st.success(f"Wage: {result['total_compensation']}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
