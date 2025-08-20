import os
os.system("clear")
'''
Diccionario simple:
Crea un diccionario con los nombres de 3 países como claves y sus capitales como valores. Imprime la capital de uno de ellos.
'''
# paises = {
#     "Colombia": "Bogota",
#     "Peru": "Lima",
#     "Rusia": "Moscu"
# }
# for pais in paises:
#     print(paises[pais])

'''
Agregar y eliminar claves:
Empieza con un diccionario vacío, agrega 3 pares clave-valor y luego elimina uno de ellos.
'''
# pikachu = {}
# for estadistica in range(3):
#     estadistica = input("Estadistica: ")
#     valor = int(input("Valor: "))
#     pikachu[estadistica] = valor
# print(pikachu)
# del pikachu["Ataque"]
# print(pikachu)

'''
Contar letras en una palabra:
Escribe un programa que guarde en un diccionario cuántas veces aparece cada letra en una palabra que ingrese el usuario.
'''
# cadena = input("Ingrese una palabra: ")
# conteo = {}
# for letra in cadena:
#     if letra in conteo:
#         conteo[letra] += 1 #se aumenta
#     else:
#         conteo[letra] = 1 #se agrega
# print(conteo)

'''
Invertir un diccionario:
Dado un diccionario con claves y valores, crea otro que invierta las claves con los valores.
Ejemplo: { "a": 1, "b": 2 } → { 1: "a", 2: "b" }
'''
# dic = { "a": 1, "b": 2 }
# invertido = {}
# for key in dic:
#     temp = dic[key] #valor
#     invertido[temp] = key
# print(invertido)

'''
Ejercicios intermedios
Notas de estudiantes:
Crea un diccionario donde las claves sean nombres de estudiantes y los valores una lista de 3 notas. Luego, imprime el promedio de cada estudiante.
'''
# dic = {
#     "Mateo": [4.6, 5.0, 3.1],
#     "Alejandro": [4.4, 3.0, 3.7]
# }
# for estudiante in dic:
#     notas = dic[estudiante]
#     promedio = sum(notas) / len(notas)
#     print(round(promedio, 2))

'''
Inventario de tienda:
Crea un diccionario que almacene productos como claves y la cantidad disponible como valores. Permite al usuario ingresar el nombre de un producto y la cantidad que quiere comprar, y actualiza el inventario.
'''
# productos = {
#     "pera": 3,
#     "panzana": 7,
#     "banano": 4,
#     "uvas": 15
# }
# print("Inventario actual:")
# for producto in productos:
#     print(producto, productos[producto])
    
# producto = input("Ingrese un producto: ").lower()
# cantidad = int(input(f"Ingrese cantidad a comprar de {producto}: "))

# if producto in productos and cantidad <= productos[producto]:
#     productos[producto] = productos[producto] - cantidad
#     print("Inventario despues:")
#     for producto in productos:
#         print(producto, productos[producto])
# else:
#     print("El producto no se encuentra")

'''
Palabras más frecuentes:
Escribe un programa que lea una frase y guarde en un diccionario cuántas veces aparece cada palabra.
'''
# conteo = {}
# frase = input("Ingrese una frase: ").split()
# for palabra in frase:
#     if palabra in conteo:
#         conteo[palabra] += 1
#     else:
#         conteo[palabra] = 1
# for palabra in conteo:
#     print(palabra, conteo[palabra])


'''
Fusionar diccionarios:
Dado dos diccionarios, crea un tercero que los combine. Si tienen la misma clave, suma los valores.
'''
# a = { "name": "miduev", "age": 25 }
# b = { "name": "madeval", "es_estudiante": True }
# combinacion = {}

# for key_a in a:
#     combinacion[key_a] = a[key_a]
# print(combinacion)
    
# for key_b in b:
#     if key_b in combinacion:
#         combinacion[key_b] += b[key_b]
#     else:
#         combinacion[key_b] = b[key_b]
# print(combinacion)
'''
Directorio telefónico:
Implementa un programa donde el usuario pueda:
Agregar un contacto (nombre y número).
Buscar un contacto por nombre.
Eliminar un contacto.
Ver todos los contactos.
'''
# directorio = {}
# while True:
#     print("\n--- Directorio Telefónico ---")
#     print("1. Agregar contacto")
#     print("2. Buscar contacto")
#     print("3. Eliminar contacto")
#     print("4. Ver todos los contactos")
#     print("5. Salir")
#     opcion = int(input("Selecciones su opcion: "))

#     if opcion == 1:
#         nombre = input("Ingrese el nombre: ").lower()
#         numero = int(input("Ingrese el numero: "))
#         directorio[nombre] = numero
#         print(f"Contacto '{nombre}' agregado")
#     elif opcion == 2:
#         nombre = input("Ingrese nombre a buscar: ").lower()
#         if nombre in directorio:
#             print(f"{nombre}: {directorio[nombre]}")
#         else:
#             print("Contacto no encontrado.")
#     elif opcion == 3:
#         nombre = input("Ingrese nombre a eliminar: ").lower()
#         if nombre in directorio:
#             del directorio[nombre]
#         else:
#             print("Contacto no encontrado.")
#     elif opcion == 4:
#         if directorio:
#             print("\n\tTodos los contactos:")
#             for nombre, numero in directorio.items():
#                 print(f"{nombre}: {numero}")
#         else:
#             print("Directorio vacio")
#     elif opcion == 5:
#         print("Saliendo del programa")
#         break
#     else:
#         print("Opcion no valida, intente de nuevo")
            
'''
Sistema de calificaciones (extendido):
Crea un programa donde el usuario pueda agregar estudiantes y sus notas en distintas materias. El programa debe permitir:
Consultar todas las materias de un estudiante.
Consultar el promedio de cada estudiante.
Ver qué estudiante tiene el promedio más alto.
'''
# sistema_estudiantes = {}
# while True:
#     print("\n--- Sistema de Calificaciones ---")
#     print("1. Agregar Estudiante")
#     print("2. Consultar materias")
#     print("3. Consultar promedio")
#     print("4. Promedio mas alto")
#     print("5. Salir")
#     opcion = int(input("Selecciones su opcion: "))
    
#     if opcion == 1:
#         materias_notas = {}
#         estudiante = input("Ingrese nombre del estudiante: ").lower()
#         cantidad_materias = int(input(f"Cuantas materias lleva {estudiante}?: "))
#         for i in range(cantidad_materias):
#             materia = input(f"Ingrese la materia {i + 1}: ").lower()
#             nota = float(input(f"Ingrese la nota de {materia}: "))
#             materias_notas[materia] = nota
#         sistema_estudiantes[estudiante] = materias_notas
        
#     elif opcion == 2:
#         if sistema_estudiantes:
#             estudiante = input("De que estudiante desea ver las materias?: ").lower()
#             if estudiante in sistema_estudiantes:
#                 materias = list(sistema_estudiantes[estudiante].keys())
#                 print(f"\nMaterias de {estudiante}: ", " | ".join(materias))
#             else:
#                 print("\nEl estudiante no fué encontrado")
#         else:
#             print("No hay estudiantes registrados")
            
#     elif opcion == 3:
#         if sistema_estudiantes:
#             estudiante = input("De que estudiante desea ver el promedio?: ").lower()
#             if estudiante in sistema_estudiantes:
#                 notas = list(sistema_estudiantes[estudiante].values())
#                 promedio = sum(notas) / len(notas)
#                 print(f"\nPromedio de {estudiante}: {promedio}")
#         else:
#             print("No hay estudiantes regristrados")
    
#     #la cagué en no pensar en esto desde el principio
#     elif opcion == 4:
#         if sistema_estudiantes:
#             promedio_mayor = 0
#             for estudiante in sistema_estudiantes:
#                 notas = list(sistema_estudiantes[estudiante].values())
#                 promedio = sum(notas) / len(notas)
#                 if promedio > promedio_mayor:
#                     promedio_mayor = promedio
#                     estudiante_promedio_mayor = estudiante
#             print(f"El promedio mayor lo tiene {estudiante_promedio_mayor} con {round(promedio_mayor, 2)}")
#         else:
#             print("\nNo hay estudiantes regristrados")
#     elif opcion == 5:
#         print("\nSaliendo del programa")
#         break
#     else:
#         print("\nOpcion invalida, intentelo de nuevo")
         
'''
Diccionario anidado (JSON-like):
Crea un diccionario que represente un usuario en una red social con esta estructura:
usuario = {
    "nombre": "Juan",
    "edad": 20,
    "amigos": ["Ana", "Luis", "Pedro"],
    "publicaciones": [
        {"texto": "Hola mundo", "likes": 10},
        {"texto": "Aprendiendo Python", "likes": 25}
    ]
}
Luego, imprime:
El nombre del usuario.
Su primer amigo.
El texto de su segunda publicación.
El total de "likes" que tienen todas sus publicaciones.
'''
usuario = {
    "nombre": "Juan",
    "edad": 20,
    "amigos": ["Ana", "Luis", "Pedro"],
    "publicaciones": [
        {"texto": "Hola mundo", "likes": 10},
        {"texto": "Aprendiendo Python", "likes": 25}
    ]
}
print(f"Nombre de usuario: {usuario['nombre']}")
print(f"Primer amigo: {usuario['amigos'][0]}")
print(f"Texto segunda publicacion: {usuario['publicaciones'][1]['texto']}")
publicaciones = usuario["publicaciones"]
total_likes = 0
for i in range(len(publicaciones)):
    total_likes += publicaciones[i]["likes"]
print(f"Total de likes: {total_likes}")