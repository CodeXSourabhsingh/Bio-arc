# Bio-arc

Bio-arcs is a Python learning repo focused on biology and healthcare problem solving.

I rebuild the same core logic across four syntax layers: raw Python, class-based Python, ETL/data processing, and Streamlit app development. Each arc starts as a simple script and evolves into a more structured, interactive, and portfolio-ready solution.

This repo is a learning ladder, not a finished product. The V1-V3 versions are the practice reps; the V4 versions are the polished examples that show the progression clearly.

---

## What This Repo Is

A structured practice log for closing the syntax gap.

Every arc begins as a bare dict/if-else script and ends as a deployed Streamlit app. Each layer re-types the previous layer's core logic in a more expressive syntax. The goal is not to build the perfect architecture; the goal is to build repetition, fluency, and confidence.

This is not a product. It is a progression of problem-solving exercises across several biology-focused domains.

---

## The V1 → V4 Pattern

Each arc follows the same four-layer structure. The logic stays the same; the syntax becomes richer and more structured each time.

| Layer | What it is | Syntax focus |
|-------|------------|--------------|
| V1 | Bare script — dict + if/else | dicts, conditionals, loops |
| V2 | Class-based version | classes, __init__, methods |
| V3 | ETL pipeline | Pandas, MySQL, file I/O |
| V4 | Streamlit app | UI, session state, matplotlib |

The rule: V4 re-types V1's core logic. Every layer reinforces the previous one. That repetition is the point.

---

## The Arcs

### Arc 1 — Blood Group Compatibility

- V1: Dict lookup for ABO/Rh compatibility
- V2: BloodGroup class with can_donate_to() and can_receive_from()
- V3: CSV of blood types → validate → MySQL
- V4: Streamlit app with donor/recipient dropdowns

### Arc 2 — Blood Test Interpreter

- V1: Hemoglobin, WBC, and platelets → Low/Normal/High per parameter
- V2: BloodTest class with interpret() method
- V3: Patient CBC CSV → classify → MySQL
- V4: Streamlit app with sliders and matplotlib chart

### Arc 3 — Glucose & Diabetes Risk

- V1: Fasting + post-meal glucose → Normal/Prediabetic/Diabetic
- V2: GlucoseProfile class with risk scoring
- V3: Glucose logs CSV → classify + trend → MySQL
- V4: Streamlit app with matplotlib trend visualization

### Arc 4 — Pharmacokinetics Dosage

- V1: Weight + half-life + target level → calculated dose
- V2: DrugDose class with calculate() method
- V3: Drug parameters CSV → dose per patient → MySQL
- V4: Streamlit app

---

## Project Structure

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
├── arc4_dosage/
│   └── (same structure)
└── ...
```

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.13+ | Core runtime |
| Pandas | Tabular data and ETL |
| NumPy | Numeric operations |
| MySQL | Data persistence |
| Streamlit | Interactive UIs |
| Matplotlib | Charts and visualization |

---

## Portfolio Pieces

Two arcs are polished enough to serve as portfolio examples:

- Blood Test Interpreter (Arc 2 V4)
- Glucose Risk Calculator (Arc 3 V4)

The other two remain practice reps. Not every exercise needs to become a product.

---

## Why This Repo Exists

Three months into self-teaching, the syntax gap became the bottleneck. I already had enough domain understanding and logic-building ability to think in systems, but I still lacked the vocabulary and fluency to express those ideas cleanly in code.

The fix was simple: type every block from memory, across multiple domains, and across multiple syntax layers.

This repo is the visible trace of that process.

---

## What This Repo Demonstrates

This repo shows a progression from:

- basic Python logic
- object-oriented structure
- data pipeline thinking
- interactive healthcare dashboards

It demonstrates my ability to take domain rules, translate them into code, and evolve that code from simple logic into user-facing tools.

---

## Running a File

```bash
# V1-V3
python arc1_blood_groups/Blood_V1.py

# V4 (Streamlit)
streamlit run arc1_blood_groups/Blood_V4.py
```

---

## Author

Sourabh Singh — Python ETL & Bioinformatics Developer

- GitHub: @CodeXSourabhsingh
- LinkedIn: sourabh-singh-7b124934

---

## License

MIT
