# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales
a = int(input("Introduzca un numero:"))
b = int(input("Introduzca un numero:"))
if a == b:
    print("Los numeros son iguales")
elif a > b:
    print(f"{a} es mayor que {b}")
else:
    print(f"{b} es mayor que {a}")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

c = int(input("Introduzca un numero:"))
d = int(input("Introduzca un numero:"))
operacion = input("Que operacion desea realizar respectivamente? (+, -, *, /)")

if operacion == "+":
    print(f"{c} + {d} =", c + d)
elif operacion == "-":
    print(f"{c} - {d} =", c - d)
elif operacion == "*":
    print(f"{c} * {d} =", c * d)
elif operacion == "/":
    if d == 0:
        print("No puede dividir entre 0")
    else:
        print(f"{c} / {d} =", c / d)
else:
    print("Operacion incorrecta")


# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

year = int(input("Introduzca un año: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")


# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

edad = int(input("Ingrese una edad: "))
if edad >= 65:
    print("Adulto mayor")
elif edad >= 18:
    print("Adulto")
elif edad >= 13:
    print("Adolscente")
elif edad >= 3:
    print("Niño")
elif edad > 0:
    print("Bebé")
else:
    print("Edad incorrecta")