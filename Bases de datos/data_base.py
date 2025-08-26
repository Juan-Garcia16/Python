import sqlite3

conexion = sqlite3.connect("MiBase.db") #primera conexion
cursor = conexion.cursor() #Con el fin de ejecutar sentencias SQL y obtener resultados de consultas SQL,
#cursor.execute("CREATE TABLE USUARIOS(NOMBRE VARCHAR(50), EDAD INTEGER, SEXO VARCHAR(50))")
#cursor.execute("INSERT INTO USUARIOS VALUES('Juan', 20, 'Masculino')")
#cursor.execute("INSERT INTO USUARIOS VALUES('Maria', 17, 'Femenino')")

#cursor.execute("SELECT * FROM USUARIOS") #consulta
# usuarios = cursor.fetchone() #para guardar los datos, devuelve TUPLA
# print(usuarios)

usuarios = [
    ("Mateo", 24, "Masculino"),
    ("David", 19, "Tapasco"),
    ("Alejandro", 21, "Cuenca")
]

#cursor.executemany("INSERT INTO USUARIOS VALUES(?,?,?)", usuarios) #insertar varios registros
cursor.execute("SELECT * FROM USUARIOS")
consulta = cursor.fetchall()
print(consulta)

conexion.commit() #para que siempre se guarden los cambios
conexion.close()