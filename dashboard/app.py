import streamlit as st
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.predict_risk import predict_risk
from src.multilingual_alerts import generate_alert
from src.filter_maintenance import recommend_maintenance

st.set_page_config(
    page_title="JalRakshak AI",
    page_icon="💧"
)

st.title("💧 JalRakshak AI")

st.write(
    "AI Powered Water Quality Monitoring System"
)

st.subheader("Water Parameters")

ph = st.number_input(
    "pH",
    min_value=0.0,
    max_value=14.0,
    value=7.0
)

tds = st.number_input(
    "TDS",
    value=300
)

turbidity = st.number_input(
    "Turbidity",
    value=2
)

do = st.number_input(
    "Dissolved Oxygen",
    value=6
)

if st.button("Predict Risk"):

    risk = predict_risk(
        ph,
        tds,
        turbidity,
        do
    )

    st.success(
        f"Risk Level: {risk}"
    )

    alerts = generate_alert(risk)

    st.subheader("Alerts")

    st.write(alerts["English"])
    st.write(alerts["Hindi"])
    st.write(alerts["Marathi"])

    st.subheader(
        "Maintenance Recommendation"
    )

    recommendations = recommend_maintenance(
        tds,
        turbidity
    )

    for rec in recommendations:
        st.write("✅", rec)
