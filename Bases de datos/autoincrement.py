import sqlite3

conexion = sqlite3.connect("MISPRODUCTOS.db")
cursor = conexion.cursor()

#cursor.execute("CREATE TABLE PRODUCTOS(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(20), SECCION VARCHAR(20))")

productos = [
    ('Leche', 'Lacteo'),
    ('Pan', 'Panaderia'),
    ('Gaseosa', 'Bebida')
]

#Se para NULL para ID
cursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?)", productos)
cursor.execute("SELECT * FROM PRODUCTOS")
consulta = cursor.fetchall()
print(consulta)
conexion.commit()
conexion.close()