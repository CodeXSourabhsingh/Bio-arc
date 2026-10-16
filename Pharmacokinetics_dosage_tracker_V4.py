import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Pharmacokinetics Dosage Tracker", layout="centered")

st.title("Pharmacokinetics Dosage Tracker")
st.write("Estimate loading dose, maintenance dose, and drug clearance from weight, half-life, and target concentration.")

VD_TABLE = {
    'Warfarin':     0.14,
    'Digoxin':      7.0,
    'Theophylline': 0.5,
    'Gentamicin':   0.25,
    'Metformin':    1.0,
}

drug = st.selectbox("Drug", list(VD_TABLE.keys()))
weight = st.slider("Patient weight (kg)", 30.0, 150.0, 70.0, 0.5)
half_life = st.slider("Drug half-life (hours)", 1.0, 72.0, 40.0, 0.5)
target = st.slider("Target plasma concentration (mg/L)", 0.1, 5.0, 2.0, 0.1)

if st.button("Calculate"):

    vd = weight * VD_TABLE[drug]
    ld = vd * target
    k = 0.693 / half_life
    md = k * vd * target * 12
    ss = 5 * half_life

    st.divider()
    st.subheader("Calculated Doses")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Volume of Distribution", f"{vd:.2f} L")
        st.metric("Loading Dose", f"{ld:.2f} mg")
    with col2:
        st.metric("Maintenance Dose (12h)", f"{md:.2f} mg")
        st.metric("Steady State", f"{ss:.1f} hours")

    st.subheader("Concentration Decay")

    t = np.linspace(0, 5 * half_life, 100)
    C = target * np.exp(-k * t)

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(t, C, color='steelblue', linewidth=2, label='Plasma concentration')
    ax.axhline(y=target, color='grey', linestyle='--', linewidth=1, label=f'Target: {target} mg/L')
    ax.axvline(x=ss, color='orange', linestyle=':', linewidth=1, label=f'Steady state: {ss:.0f}h')

    ax.set_xlabel("Time (hours)")
    ax.set_ylabel("Concentration (mg/L)")
    ax.set_title(f"{drug} — {weight} kg, half-life {half_life}h")
    ax.legend()
    ax.grid(alpha=0.3)

    st.pyplot(fig)