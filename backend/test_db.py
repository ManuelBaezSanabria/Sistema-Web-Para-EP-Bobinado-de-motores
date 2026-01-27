# test_db.py
import pyodbc

try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=EPBobinadoDB;'
        'Trusted_Connection=yes;'  # O usa 'UID=usuario;PWD=contraseña'
    )
    print("✅ Conexión exitosa a SQL Server")
    conn.close()
except Exception as e:
    print(f"❌ Error: {e}")