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
productos = {
    "Pera": 3,
    "Manzana": 7,
    "Banano": 4,
    "Uvas": 15
}
print("Inventario actual:")
for producto in productos:
    print(producto, productos[producto])
producto = input("Ingrese un producto: ")
cantidad = int(input(f"Ingrese cantidad a comprar de {producto}: "))
if producto in productos:
    productos[productos] = productos[producto] - cantidad

print("Inventario despues:")
for producto in productos:
    print(producto, productos[producto])



'''
Palabras más frecuentes:
Escribe un programa que lea una frase y guarde en un diccionario cuántas veces aparece cada palabra.
'''

'''
Fusionar diccionarios:
Dado dos diccionarios, crea un tercero que los combine. Si tienen la misma clave, suma los valores.
'''