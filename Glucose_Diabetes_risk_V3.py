import pandas as pd
from Glucose_Diabetes_risk_V2 import GD_risk
import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

df = pd.read_csv('glucose_patient.csv')

valid_numbers = (
    pd.to_numeric(df['fg'], errors='coerce').notnull() &
    pd.to_numeric(df['pmg'], errors='coerce').notnull()
)
is_valid = valid_numbers
bad_row = df[~is_valid]

if len(bad_row) > 0:
    print("BAD ROW:")
    print(bad_row)
    exit()
else:
    print("All valid. Continuing.")

records = []

for index, row in df.iterrows():
    patient = GD_risk(row['fg'], row['pmg'])
    fg_label = patient.FG_check()
    pmg_label = patient.PMG_check()

    if fg_label == 'Diabetic' or pmg_label == 'Diabetic':
      final_label = 'Diabetic'
    elif fg_label == 'PreDiabetic' or pmg_label == 'PreDiabetic':
      final_label = 'PreDiabetic'
    else:
     final_label = 'Normal'

    records.append({
        'patient_id': int(row['patient_id']),
        'fg':         float(row['fg']),
        'fg_label':   fg_label,
        'pmg':        float(row['pmg']),
        'pmg_label':  pmg_label,
        'final_label': final_label
    })

print("Records:", len(records))

conn = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS glucose_risk_results (
        patient_id INT,
        fg FLOAT,
        fg_label VARCHAR(50),
        pmg FLOAT,
        pmg_label VARCHAR(50),
        final_label VARCHAR(50)
    )
""")

cursor.execute("TRUNCATE TABLE glucose_risk_results")

insert_sql = """INSERT INTO glucose_risk_results
(patient_id, fg, fg_label, pmg, pmg_label, final_label)
VALUES (%s, %s, %s, %s, %s, %s)"""

for r in records:
    cursor.execute(insert_sql, (
        r['patient_id'],
        r['fg'],
        r['fg_label'],
        r['pmg'],
        r['pmg_label'],
        r['final_label']
    ))

conn.commit()
cursor.close()
conn.close()

print("Loaded. Check MySQL.")