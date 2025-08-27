# ==============================================
# 1. LAMBDA
# ==============================================
# Una función lambda es una función anónima (sin nombre)
# que se define en una sola línea.
# Sintaxis: lambda argumentos: expresión

# Ejemplo: función que dobla un número
doble = lambda x: x * 2
print("Lambda - Doble de 5:", doble(5))  # 10


# ==============================================
# 2. MAP
# ==============================================
# map(funcion, iterable) aplica una función a cada elemento del iterable
# y devuelve un objeto map (que se puede convertir en lista).

numeros = [1, 2, 3, 4, 5]

# Usamos lambda dentro de map
dobles = map(lambda x: x * 2, numeros)

# Convertimos el resultado a lista para verlo
print("Map - Doblar lista:", list(dobles))  # [2, 4, 6, 8, 10]


# ==============================================
# 3. FILTER
# ==============================================
# filter(funcion, iterable) selecciona los elementos que cumplan
# con la condición de la función.

# Queremos los números pares de la lista
pares = filter(lambda x: x % 2 == 0, numeros)
print("Filter - Pares en la lista:", list(pares))  # [2, 4]


# ==============================================
# 4. GENERADORES
# ==============================================
# Un generador es una función que usa 'yield' en lugar de 'return'.
# Devuelve valores de uno en uno, bajo demanda, sin guardar todo en memoria.

def generador_pares(n):
    """Genera los primeros n números pares usando yield"""
    for i in range(n):
        yield i * 2  # Suspende la función y devuelve el valor

# Ejemplo de uso con for
print("Generador con for:")
for numero in generador_pares(5):
    print(numero, end=" ")  # 0 2 4 6 8
print()


# ==============================================
# 5. USO DE next() CON GENERADORES
# ==============================================
# La función next() obtiene el siguiente valor del generador manualmente.

gen = generador_pares(3)  # Generará 0, 2, 4

print("Generador con next():")
print(next(gen))  # 0
print(next(gen))  # 2
print(next(gen))  # 4
# Si llamamos de nuevo: next(gen) → da un StopIteration (ya no hay más)


# ==============================================
# 6. GENERADOR INFINITO
# ==============================================
# Los generadores pueden ser infinitos, ya que entregan valores bajo demanda.

def generador_infinito_pares():
    """Generador infinito de números pares"""
    n = 0
    while True:   # ciclo sin fin
        yield n
        n += 2

# Ejemplo de uso
print("Generador infinito (primeros 5 pares):")
gen_inf = generador_infinito_pares()
for _ in range(5):
    print(next(gen_inf), end=" ")  # 0 2 4 6 8
print()
