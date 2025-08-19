print("Prueba 1")
print("Prueba", "separado", "por", "Parametros")
print("Prueba", "separado", "por", "Parametros", sep="-", end=" ") #Separacion y final definidos por parametro 
print("Continuacion linea anterior")

l = [1,2,3,4,5]
l.extend([4])
print(l)
l.extend(range(5,8))
print(l) 