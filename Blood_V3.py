import pandas as pd 
from Blood_V2 import Blood_group
import mysql.connector
from config import MYSQL_HOST,MYSQL_USER,MYSQL_PASSWORD,MYSQL_DATABASE

df = pd.read_csv('blood_type.csv')
df['blood_type'].isin(Blood_group.ALL_TYPES)
bad_rows = df[~df['blood_type'].isin(Blood_group.ALL_TYPES)]
if len(bad_rows)>0:
    print("BAD ROW: ")
    print(bad_rows)
    exit
else:
    print('ALL 8 valid. continuing')

df['blood_type'].tolist() 
records = []

for donor in Blood_group.ALL_TYPES:
    for recipeint in Blood_group.ALL_TYPES:
        if recipeint in Blood_group(donor).can_donate_to():
            records.append({'donor':donor,
                            'recipeint':recipeint,
                            'compatible': True})
        else:
            records.append({'donor': donor,
                            'recipeint': recipeint,
                            'compatible': False})
            
print(len(records))            

mysql = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE,
)
cursor = mysql.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS blood_compatibility (
        donor VARCHAR(3) NOT NULL,
        recipeint VARCHAR(3) NOT NULL,
        compatible BOOLEAN NOT NULL
    )
""")

cursor.execute("truncate table blood_compatibility")

for r in records:
    cursor.execute(
        "INSERT INTO blood_compatibility (donor, recipeint, compatible) VALUES (%s, %s, %s)",
        (r['donor'], r['recipeint'], r['compatible']),
    )

mysql.commit()
cursor.close()
mysql.close()












