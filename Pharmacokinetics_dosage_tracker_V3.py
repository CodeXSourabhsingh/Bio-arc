import pandas as pd
from Pharmacokinetics_dosage_tracker_V2 import PK_Dosage
import mysql.connector
from config import MYSQL_USER,MYSQL_HOST,MYSQL_PASSWORD,MYSQL_DATABASE

df = pd.read_csv('pk_patients.csv')

valid_drug = df['drug'].isin(PK_Dosage.VD_TABLE.keys())
valid_numbers = (
    pd.to_numeric(df['weight'], errors='coerce').gt(0) &
    pd.to_numeric(df['half_life'], errors='coerce').gt(0) &
    pd.to_numeric(df['target'], errors='coerce').gt(0)
)
is_valid = valid_drug & valid_numbers
bad_rows = df[~is_valid]
if len(bad_rows) > 0:
    print('BAD ROWS:')
    print(bad_rows)
    exit()
else:
    print('all valid')

records = []
for index, row in df.iterrows():
    patient = PK_Dosage(row['weight'], row['half_life'], row['target'], row['drug'])
    
    records.append({
        'patient_id':       int(row['patient_id']),
        'weight':           float(row['weight']),
        'half_life':        float(row['half_life']),
        'target':           float(row['target']),
        'drug':             row['drug'],
        'vd':               float(patient.vd()),
        'loading_dose':     float(patient.ld()),
        'maintenance_dose': float(patient.md()),
        'steady_state':     float(patient.steady_state()),
    })

print("Records:", len(records))

conn = mysql.connector.connect(
    host=MYSQL_HOST, user=MYSQL_USER,
    password=MYSQL_PASSWORD, database=MYSQL_DATABASE
)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pk_dose_results (
        patient_id INT,
        weight FLOAT,
        half_life FLOAT,
        target FLOAT,
        drug VARCHAR(50),
        vd FLOAT,
        loading_dose FLOAT,
        maintenance_dose FLOAT,
        steady_state FLOAT
    )
""")

cursor.execute("TRUNCATE TABLE pk_dose_results")

insert_sql = """INSERT INTO pk_dose_results
(patient_id, weight, half_life, target, drug, vd, loading_dose, maintenance_dose, steady_state)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

for r in records:
    cursor.execute(insert_sql, (
        r['patient_id'], r['weight'], r['half_life'], r['target'], r['drug'],
        r['vd'], r['loading_dose'], r['maintenance_dose'], r['steady_state']
    ))

conn.commit()
cursor.close()
conn.close()

print("Loaded. Check MySQL.")