import streamlit as st
import pandas as pd
import joblib


st.set_page_config(
    page_title="Driver Station",
    page_icon="🚗",
    layout="centered"
)

st.title("🚗 Driver Station")
st.write("Prédiction du prix d'une voiture")


model = joblib.load("model/model.pkl")


st.header("Informations de la voiture")


brand = st.selectbox(
    "Marque",
    [
        "Ambassador",
        "Audi",
        "BMW",
        "Chevrolet",
        "Daewoo",
        "Datsun",
        "Fiat",
        "Force",
        "Ford",
        "Honda",
        "Hyundai",
        "Isuzu",
        "Jaguar",
        "Jeep",
        "Kia",
        "Land",
        "MG",
        "Mahindra",
        "Maruti",
        "Mercedes-Benz",
        "Mitsubishi",
        "Nissan",
        "OpelCorsa",
        "Renault",
        "Skoda",
        "Tata",
        "Toyota",
        "Volkswagen",
        "Volvo"
    ]
)

year = st.number_input(
    "Année",
    min_value=1990,
    max_value=2026,
    value=2018
)


km_driven = st.number_input(
    "Kilométrage",
    min_value=0,
    value=50000
)


owner = st.selectbox(
    "Propriétaire",
    [
        "First Owner",
        "Second Owner",
        "Third Owner",
        "Fourth & Above Owner",
        "Test Drive Car"
    ]
)


fuel = st.selectbox(
    "Carburant",
    [
        "CNG",
        "Diesel",
        "Electric",
        "LPG",
        "Petrol"
    ]
)


seller_type = st.selectbox(
    "Type de vendeur",
    [
        "Dealer",
        "Individual",
        "Trustmark Dealer"
    ]
)


transmission = st.selectbox(
    "Transmission",
    [
        "Automatic",
        "Manual"
    ]
)


# Création des données
data = pd.DataFrame([{
    "year": year,
    "km_driven": km_driven,
    "owner": owner,
    "fuel": fuel,
    "seller_type": seller_type,
    "transmission": transmission
}])


if st.button("Prédire le prix"):

    prediction = model.predict(data)

    st.success(
        f"Prix estimé : {prediction[0]:,.0f} DH"
    )