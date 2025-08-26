import sqlite3

'''
(LEER)Filtrado con clausula WHERE por atributos
'''
# conexion = sqlite3.connect("MISPRODUCTOS.db")
# cursor = conexion.cursor()
# #Clausula where para filtrar
# cursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='Bebida'")
# productos = cursor.fetchall()
# print(productos)

# conexion.commit()
# conexion.close()

'''
(ACTUALIZAR)Cambiar 'Bebida' por 'Bebidas'
'''
# conexion = sqlite3.connect("MISPRODUCTOS.db")
# cursor = conexion.cursor()
# #cursor.execute("UPDATE PRODUCTOS SET SECCION='Bebidas' WHERE SECCION='Bebida'")
# cursor.execute("SELECT * FROM PRODUCTOS")
# productos = cursor.fetchall()
# print(productos)
# conexion.commit()
# conexion.close()

'''
(ELIMINAR)
'''
conexion = sqlite3.connect("MISPRODUCTOS.db")
cursor = conexion.cursor()

#cursor.execute("DELETE FROM PRODUCTOS WHERE ID=4")
cursor.execute("SELECT * FROM PRODUCTOS")
productos = cursor.fetchall()
print(productos)
conexion.commit()
conexion.close()