import streamlit as st
import matplotlib.pyplot as plt

PARAMETERS = {
    'hb':        {'M': (13.5, 17.5), 'F': (12.0, 15.5)},
    'wbc':       (4.0, 11.0),
    'platelets': (150, 450),
}

def classify(value, low, high, low_label, high_label):
    if value < low:
        return low_label
    elif value > high:
        return high_label
    else:
        return 'Normal'

st.title("Blood Test Interpreter")

sex = st.selectbox("Sex", ['M', 'F'])
hb = st.slider("Hemoglobin (g/dL)", 5.0, 25.0, 14.0, 0.1)
wbc = st.slider("WBC (x10^9/L)", 1.0, 30.0, 7.0, 0.1)
platelets = st.slider("Platelets (x10^9/L)", 50, 800, 250, 1)

hb_label = 'Normal'
wbc_label = 'Normal'
plt_label = 'Normal'

if st.button("Interpret"):

    hb_range = PARAMETERS['hb'][sex]
    hb_label = classify(hb, hb_range[0], hb_range[1], 'Anemia', 'Polycythemia')

    wbc_range = PARAMETERS['wbc']
    wbc_label = classify(wbc, wbc_range[0], wbc_range[1], 'Leukopenia', 'Leukocytosis')

    plt_range = PARAMETERS['platelets']
    plt_label = classify(platelets, plt_range[0], plt_range[1], 'Thrombocytopenia', 'Thrombocytosis')

    st.write(f"**Hemoglobin:** {hb_label}")
    st.write(f"**WBC:** {wbc_label}")
    st.write(f"**Platelets:** {plt_label}")

fig, axes = plt.subplots(3, 1, figsize=(8, 5))

ax = axes[0]
low, high = PARAMETERS['hb'][sex]
ax.axvspan(low, high, color='green', alpha=0.2)
ax.axvline(hb, color='green' if hb_label == 'Normal' else 'red', linewidth=3)
ax.set_xlim(0, 25)
ax.set_yticks([])
ax.set_title(f"Hemoglobin: {hb_label}")

ax = axes[1]
low, high = PARAMETERS['wbc']
ax.axvspan(low, high, color='green', alpha=0.2)
ax.axvline(wbc, color='green' if wbc_label == 'Normal' else 'red', linewidth=3)
ax.set_xlim(0, 30)
ax.set_yticks([])
ax.set_title(f"WBC: {wbc_label}")

ax = axes[2]
low, high = PARAMETERS['platelets']
ax.axvspan(low, high, color='green', alpha=0.2)
ax.axvline(platelets, color='green' if plt_label == 'Normal' else 'red', linewidth=3)
ax.set_xlim(0, 800)
ax.set_yticks([])
ax.set_title(f"Platelets: {plt_label}")

plt.tight_layout()
st.pyplot(fig)