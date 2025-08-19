"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

def count_carnivore_dinosaur_eggs(eggs) -> int:
    pares = [egg for egg in eggs if egg % 2 == 0]
    return sum(pares)

egg_list = [3, 4, 7, 5, 8, 2, 4]
print(count_carnivore_dinosaur_eggs(egg_list))