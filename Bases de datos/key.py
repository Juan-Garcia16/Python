import sqlite3

conexion = sqlite3.connect("Productos.db")
cursor = conexion.cursor()

'''
====================================================================================
Gracias al PRIMARY KEY no se pueden registrar datos que tenga CODIGO_P existente
====================================================================================
'''
cursor.execute("CREATE TABLE PRODUCTOS (CODIGO_P VARCHAR(20) PRIMARY KEY, NOMBRE_P VARCHAR(20), SECCION_P VARCHAR(20))")

productos = [
    ("AR1", "Leche", "Lacteos"),
    ("AR2", "Facturas", "Panaderia"),
    ("AR3", "Asado", "Carniceria")
]

cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", productos)
cursor.execute("SELECT * FROM PRODUCTOS")
datos = cursor.fetchmany(2)
print(datos)
conexion.commit()
conexion.close()