import pyodbc 
SERVER = '(local)'
DATABASE = 'master'
connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Encrypt=no;Trusted_connection=yes;'
conn = pyodbc.connect(connectionString) 
SQL_QUERY = """
SELECT * FROM DimGeography
"""
cursor = conn.cursor()
cursor.execute(SQL_QUERY)
records = cursor.fetchall()
for r in records:
    print(f"hu")
print("EJ")