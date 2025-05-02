import streamlit as st
import pandas as pd
from datetime import date

# === Page Setup ===
st.set_page_config(
    page_title="Bitcoin Price Predictor",
    page_icon="📈",
    layout="centered"
)

# === Title ===
st.title("🤖 Bitcoin Price Predictor")
st.markdown("An interactive tool to forecast future Bitcoin prices based on historical and market data. *(Work in Progress)*")

st.markdown("---")

# === Prediction Section ===
st.subheader("📅 Select Prediction Date")

future_date = st.date_input("Choose a future date", value=date.today())

st.markdown("")

if st.button("🔒 Predict"):
    st.info("🚧 Prediction logic coming soon. The model will be integrated once finalized.")

st.markdown("---")

# === Navigation Link ===
st.markdown("🔄 Want to analyze trends instead? Go to the [Bitcoin Market Dashboard](https://bitcoin-market-dashboard.streamlit.app/)")

# === Footer ===
st.markdown("---")
st.caption("Created by Marc Seger | [GitHub](https://github.com/Marc-Seger) | [Portfolio](https://marc-seger.github.io/portfolio)")
