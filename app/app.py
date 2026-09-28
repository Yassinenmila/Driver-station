import streamlit as st
import pandas as pd
import joblib

df = pd.read_csv('data/cleaned_cars.csv')


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
    df["brand"].unique().tolist()
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
    "Propriétaire",df["owner"].unique().tolist()
)


fuel = st.selectbox(
    "Carburant",df["fuel"].unique().tolist()
    
)


seller_type = st.selectbox(
    "Type de vendeur",
    df["seller_type"].unique().tolist()
)


transmission = st.selectbox(
    "Transmission",
    df["transmission"].unique().tolist()
)


data = pd.DataFrame([{
    "year": year,
    "km_driven": km_driven,
    "owner": owner,
    "fuel": fuel,
    "seller_type": seller_type,
    "transmission": transmission,
    "brand":brand
}])


if st.button("Prédire le prix"):

    prediction = model.predict(data)

    st.success(
        f"Prix estimé : {prediction[0]:,.0f} DH"
    )