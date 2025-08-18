###
# EJERCICIOS (while)
###
import os
os.system("clear")

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
num = 10
while num > 0:
    print(num)
    num -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
num = 1
suma_pares = 0
while num <= 20:
    if num % 2 == 0:
        suma_pares += num
    num += 1
print("suma de pares =", suma_pares)

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")
i = 1
factorial = 1
num = int(input("Ingrese un numero entero positivo: "))

while i <= num:
    factorial *= i
    i += 1

print(f"El factorial de {num} es:", factorial)

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")
password = ""

while len(password) < 8:
    password = input("Ingrese contrasena con al menos 8 caracters\n")
    if len(password) < 8:
        print("Debe tener al menos 8 caracteres, pruebe de nuevo")

print("Contrasena valida")

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")
num = int(input("Ingrese un numero"))
i = 1
while i <= 10:
    print(f"{num} * {i} =", num * i)
    i += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")
n = int(input("Introduce un número entero positivo N: "))
print("Los números primos menores o iguales que N:")
numero = 2
while numero <= n:
  es_primo = True  # Asumimos que el número es primo hasta que se demuestre lo contrario
  divisor = 2
  while divisor * divisor <= numero:  # Optimizamos: no es necesario probar divisores hasta numero
    if numero % divisor == 0:
      es_primo = False  # Si encontramos un divisor, no es primo
      break  # Salimos del bucle interior
    divisor += 1
  if es_primo:
    print(numero)

  numero += 1
