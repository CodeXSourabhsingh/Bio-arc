import pandas as pd
from Blood_CBC_V2 import CBC_Analyzer
import mysql.connector
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

df = pd.read_csv(r'C:\Users\HP\OneDrive\Documents\python learning\pandas learning\cbc_patients.csv')

# ---------- VALIDATE ----------
valid_sex = df['sex'].isin(['M', 'F'])
valid_numbers = (
    pd.to_numeric(df['hb'], errors='coerce').notnull() &
    pd.to_numeric(df['wbc'], errors='coerce').notnull() &
    pd.to_numeric(df['platelets'], errors='coerce').notnull()
)
is_valid = valid_sex & valid_numbers
bad_rows = df[~is_valid]

if len(bad_rows) > 0:
    print("BAD ROWS:")
    print(bad_rows)
    exit()
else:
    print("All valid. Continuing.")

records = []

for index, row in df.iterrows():
    patient = CBC_Analyzer(row['sex'], row['hb'], row['wbc'], row['platelets'])
    records.append({
        'patient_id':      row['patient_id'],
        'sex':             row['sex'],
        'hb':              row['hb'],
        'hb_label':        patient.hb_check(),
        'wbc':             row['wbc'],
        'WBC_label':       patient.WBC_check(),
        'platelets':       row['platelets'],
        'Platelets_label': patient.Platelets_check(),
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
CREATE TABLE IF NOT EXISTS CBC_result (
    patient_id INT,
    sex VARCHAR(1),
    hb FLOAT,
    hb_label VARCHAR(60),
    wbc FLOAT,
    wbc_label VARCHAR(60),
    platelets FLOAT,
    platelets_label VARCHAR(60)
)
""")

cursor.execute("TRUNCATE TABLE CBC_result")

insert_sql = """INSERT INTO CBC_result
(patient_id, sex, hb, hb_label, wbc, wbc_label, platelets, platelets_label)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""

for r in records:
    cursor.execute(insert_sql, (
        r['patient_id'], r['sex'], r['hb'], r['hb_label'],
        r['wbc'], r['WBC_label'], r['platelets'], r['Platelets_label']
    ))

conn.commit()
cursor.close()
conn.close()

print("Loaded. Check MySQL.")