import os
os.system("clear")
# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")

# for i in range(2, 21):
#     if i % 2 == 0:
#         print(i)
for i in range(2, 21, 2):
    print(i)
    
# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
numeros = [10, 20, 30, 40, 50]
suma = 0
for i in numeros:
    suma += i
media = suma / len(numeros)
print("La media es:", media)
        
# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
numeros = [15, 5, 25, 10, 20]
maximo = numeros[0]
for i in numeros:
    if i > maximo:
        maximo = i
print("El valor maximo es:", maximo)

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
palabras_largas = [palabra for palabra in palabras if len(palabra) > 5]
print(palabras_largas)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra = input("Ingrese una letra: ").lower()
count = 0
for palabra in palabras:
    if palabra[0] == letra:
        count += 1
print(f"{count} palabras empiezan por la letra {letra}")
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# letra = input("Introduce una letra: ").lower()  # Convertimos la letra a minúscula
# contador = 0
# for palabra in palabras:
#   if palabra.lower().startswith(letra):  # Comparamos en minúsculas
#     contador += 1
# print(f"Hay {contador} palabras que empiezan con la letra {letra}")
