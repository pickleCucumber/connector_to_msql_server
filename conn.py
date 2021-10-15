import pyodbc 
import pandas as pd

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=Server;'
                      'Database=Database;'
                      'Trusted_Connection=yes;')
 #read
df = pd.read_sql_query('SELECT * FROM datatable)

print(df)
print(type(df))
'''''''''''
#write
cursor = conn.cursor()
cursor.execute('''
                INSERT INTO product (product_id, product_name, price)
                VALUES
                (5,'Chair',120),
                (6,'Tablet',300)
                ''')
conn.commit()
'''''''''''''
