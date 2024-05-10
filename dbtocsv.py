import pyodbc 
import csv
SERVER = 'BrucePC\SQLEXPRESS'
DATABASE = 'AdventureWorksLT2022'
connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Encrypt=no;Trusted_connection=yes;'
conn = pyodbc.connect(connectionString) 
SQL_QUERY = """
SELECT 
TOP 5 c.CustomerID, 
c.CompanyName, 
COUNT(soh.SalesOrderID) AS OrderCount 
FROM 
SalesLT.Customer AS c 
LEFT OUTER JOIN SalesLT.SalesOrderHeader AS soh ON c.CustomerID = soh.CustomerID 
GROUP BY 
c.CustomerID, 
c.CompanyName 
ORDER BY 
OrderCount DESC;
"""
cursor = conn.cursor()
cursor.execute(SQL_QUERY)
records = cursor.fetchall()
print ("CustomerID\tOrderCount\tCompanyName")
with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
     
    writer.writerow(["CustomerID", "OrderCount", "CompanyName"])
    for r in records:
        writer.writerow([r.CustomerID, r.OrderCount, r.CompanyName])
        print(f"{r.CustomerID}\t       {r.OrderCount}\t       {r.CompanyName}")



