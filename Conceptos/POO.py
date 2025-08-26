"""
===============================================
INTRODUCCIÓN A LA PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
===============================================

La POO es un paradigma de programación que organiza el código
en "clases" y "objetos".

- CLASE: Es como un molde o plantilla que define cómo será un objeto.
- OBJETO: Es una instancia concreta de una clase (es decir, algo real
  creado a partir del molde).

Conceptos principales:
----------------------
1. **Clases y objetos**
2. **Atributos** (datos o propiedades que tiene un objeto)
3. **Métodos** (funciones dentro de una clase)
4. **Encapsulamiento** (ocultar o proteger datos)
5. **Herencia** (reutilizar código de una clase en otra)
6. **Polimorfismo** (un mismo método se comporta diferente
   dependiendo de la clase que lo implemente)
"""

# ==============================
# 1. Clase y objeto
# ==============================
class Persona:
    """
    Clase general que representa una persona.
    Tiene atributos como nombre y edad.
    """
    def __init__(self, nombre, edad):
        # Atributos: definen el estado del objeto
        self.nombre = nombre
        self.edad = edad
    
    # Método: define una acción del objeto
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."


# Crear un objeto (instancia de la clase Persona)
persona1 = Persona("Juan", 20)
print(persona1.saludar())   # Uso del método


# ==============================
# 2. Encapsulamiento
# ==============================
class CuentaBancaria:
    """
    Ejemplo de encapsulamiento.
    Usamos atributos "privados" (convención: __atributo).
    """
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # privado
    
    # Métodos para acceder de forma controlada
    def depositar(self, cantidad):
        self.__saldo += cantidad
    
    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes.")
    
    def mostrar_saldo(self):
        return f"Saldo actual: {self.__saldo}"


cuenta = CuentaBancaria("Ana", 1000)
cuenta.depositar(500)
print(cuenta.mostrar_saldo())
cuenta.retirar(2000)  # Intento inválido


# ==============================
# 3. Herencia
# ==============================
class Estudiante(Persona):  # Estudiante hereda de Persona
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Reutiliza constructor de Persona
        self.carrera = carrera
    
    def saludar(self):
        # Sobreescritura (modificamos el comportamiento del método padre)
        return f"Soy {self.nombre}, estudio {self.carrera}."


est1 = Estudiante("Laura", 22, "Ingeniería")
print(est1.saludar())  # Polimorfismo en acción


# ==============================
# 4. Polimorfismo
# ==============================
class Profesor(Persona):
    def __init__(self, nombre, edad, area):
        super().__init__(nombre, edad)
        self.area = area
    
    def saludar(self):
        return f"Soy el profesor {self.nombre}, enseño {self.area}."


# Función que recibe cualquier objeto de tipo Persona o derivados
def presentar(persona):
    print(persona.saludar())


# Usamos polimorfismo
presentar(est1)
profe = Profesor("Carlos", 45, "Matemáticas")
presentar(profe)

"""
Resumen:
--------
- Las CLASES son plantillas para crear objetos.
- Los OBJETOS tienen ATRIBUTOS (datos) y MÉTODOS (acciones).
- El ENCAPSULAMIENTO permite proteger datos sensibles.
- La HERENCIA permite reutilizar y extender clases.
- El POLIMORFISMO permite que un mismo método funcione de
  manera diferente en distintas clases.
"""
