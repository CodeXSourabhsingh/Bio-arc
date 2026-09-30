# Bio-arc

🧬 bio-arcs

Practice arcs that become portfolio pieces.

4 biology arcs. Each built as 4 syntax layers. Same logic, progressively richer wrapper. The point is the reps — not the architecture.

---

📋 What This Repo Is

A structured practice log for closing the syntax gap. Every arc starts as a bare dict/if-else script and ends as a deployed Streamlit app. Each layer re-types the previous layer's core logic.

Not a portfolio. Not a product. A ladder.

The polished versions (V4) become portfolio pieces. The rest (V1-V3) are the reps that made V4 possible.

---

🎯 The V1 → V4 Pattern

Every arc uses the same four-layer structure. Same core logic, different syntax wrapper each day.

| Layer | What it is | Syntax focus |
|-------|-----------|--------------|
| V1 | Bare script — dict + if/else | dict, conditionals, loops |
| V2 | Class-based version | classes, __init__, methods |
| V3 | ETL pipeline | Pandas, MySQL, file I/O |
| V4 | Streamlit app | UI, session state, matplotlib |

The rule: V4 re-types V1's core. Every layer reinforces the previous. That's the rep.

---

🧪 The Arcs

Arc 1 — Blood Group Compatibility

· V1: Dict lookup for ABO/Rh compatibility
· V2: BloodGroup class with can_donate_to() and can_receive_from()
· V3: CSV of blood types → validate → MySQL
· V4: Streamlit with donor/recipient dropdowns

Arc 2 — Blood Test Interpreter

· V1: Hemoglobin, WBC, platelets → Low/Normal/High per parameter
· V2: BloodTest class with interpret() method
· V3: Patient CBC CSV → classify → MySQL
· V4: Streamlit with sliders + matplotlib chart

Arc 3 — Glucose & Diabetes Risk

· V1: Fasting + post-meal glucose → Normal/Prediabetic/Diabetic
· V2: GlucoseProfile class with risk scoring
· V3: Glucose logs CSV → classify + trend → MySQL
· V4: Streamlit + matplotlib trend chart

Arc 4 — Pharmacokinetics Dosage

· V1: Weight + half-life + target level → recommended dose
· V2: DrugDose class with calculate() method
· V3: Drug parameters CSV → dose per patient → MySQL
· V4: Streamlit app

---

📁 Project Structure

```text
bio-arcs/
├── README.md
├── arc1_blood_groups/
│   ├── Blood_V1.py
│   ├── Blood_V2.py
│   ├── Blood_V3.py
│   └── Blood_V4.py
├── arc2_blood_tests/
│   ├── BloodTest_V1.py
│   ├── BloodTest_V2.py
│   ├── BloodTest_V3.py
│   └── BloodTest_V4.py
├── arc3_glucose/
│   └── (same structure)
└── arc4_dosage/
    └── (same structure)
```

---

🧰 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.13+ | Core runtime |
| Pandas | Tabular data and ETL |
| NumPy | Numeric operations |
| MySQL | Data persistence |
| Streamlit | Interactive UIs |
| Matplotlib | Charts and visualization |

---

🏆 Portfolio Pieces

Two arcs get polished into portfolio pieces:

· Blood Test Interpreter (Arc 2 V4)
· Glucose Risk Calculator (Arc 3 V4)

The other two stay as practice reps. Not everything needs to be a product.

---

🧠 Why This Repo Exists

3 months into self-teaching, the syntax gap became the bottleneck. Architecture was already senior-level. Vocabulary wasn't.

The fix: type every block from memory, across multiple domains, at multiple syntax layers. No copy-paste. No shortcuts. Same logic, richer wrapper, four times per domain.

This repo is the visible trace of that process.

---

🚀 Running a File

```bash
# V1-V3
python arc1_blood_groups/Blood_V1.py

# V4 (Streamlit)
streamlit run arc1_blood_groups/Blood_V4.py
```

---

Author

Sourabh Singh — Python ETL & Bioinformatics Developer

· GitHub: @CodeXSourabhsingh
· LinkedIn: sourabh-singh-7b124934

---

License

MIT
