import streamlit as st
import matplotlib.pyplot as plt

parameters = {
    'FG': (100, 126),
    'PMG': (140, 200)
}

def classify (value,low,high):
    if value < low:
        return 'Normal'
    elif value > high :
        return 'PreDiabetic'
    else:
        return 'Diabetic'
def classify_fg (fg):
    if fg < 100 :
        return 'Normal'
    elif fg < 126 :
        return 'PreDiabetic'
    else:
        return 'Diabetic'
def classify_pmg(pmg):
    if pmg < 140 :
        return 'Normal'
    elif pmg < 200:
        return 'PreDiabetic'
    else:
        return 'Diabetic'

st.title("Glucose & Diabetes Simulator")

fg = st.slider("Fasting Glucose (mg/dL)", 50, 250, 95, 1)
pmg = st.slider("Post-Meal Glucose (mg/dL)", 80, 350, 130, 1)

if st.button("Check Risk"):

    fg_tier = classify_fg(fg)
    pmg_tier = classify_pmg(pmg)

    # Hierarchy: worst tier wins
    if fg_tier == 'Diabetic' or pmg_tier == 'Diabetic':
        final = 'Diabetic'
    elif fg_tier == 'PreDiabetic' or pmg_tier == 'PreDiabetic':
        final = 'PreDiabetic'
    else:
        final = 'Normal'

    st.write(f"*Fasting Glucose:* {fg_tier}")
    st.write(f"*Post-Meal Glucose:* {pmg_tier}")

    if final == 'Diabetic':
        st.error(f"*Final: {final}*")
    elif final == 'PreDiabetic':
        st.warning(f"*Final: {final}*")
    else:
        st.success(f"*Final: {final}*")

    fig, axes = plt.subplots(2, 1, figsize=(8, 5))
    ax = axes[0]
    ax.axvspan(0, 100, color='green', alpha=0.25)
    ax.axvspan(100, 126, color='gold', alpha=0.35)
    ax.axvspan(126, 250, color='red', alpha=0.25)
    ax.axvline(fg, color='black', linewidth=3)
    ax.set_xlim(0, 250)
    ax.set_yticks([])
    ax.set_title(f"Fasting Glucose: {fg_tier} ({fg} mg/dL)")

    ax = axes[1]
    ax.axvspan(0, 140, color='green', alpha=0.25)
    ax.axvspan(140, 200, color='gold', alpha=0.35)
    ax.axvspan(200, 350, color='red', alpha=0.25)
    ax.axvline(pmg, color='black', linewidth=3)
    ax.set_xlim(0, 350)
    ax.set_yticks([])
    ax.set_title(f"Post-Meal Glucose: {pmg_tier} ({pmg} mg/dL)")

    plt.tight_layout()
    st.pyplot(fig)         
