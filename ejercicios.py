#FORMA TRADICIONAL
# def pares(limite):
#     pares = []
#     for i in range(limite):
#         pares.append((i+1) * 2)
#     return pares

# print(pares(10))

#FORMA CON GENERADORES (MAS EFICIENTE)
# def generar_pares(n):
#     """Genera los primeros n números pares utilizando un generador"""
#     for i in range(n):
#         yield i * 2

# # Ejemplo de uso
# pares = generar_pares(5)
# print(next(pares))
# print(next(pares))
# print(next(pares))
# print(next(pares))
# print(next(pares))

#Doble un numero utilizando map y función Lambda.
# numeros = [2, 3, 5, 6]
# num_doblado = list(map(lambda x: x*2, numeros))
# print(num_doblado)

def generador_pares(n):
    """Genera los primeros n números pares usando yield"""
    for i in range(n):
        yield i * 2  # Suspende la función y devuelve el valor
        
prueba = generador_pares(4)
print(type(prueba))

