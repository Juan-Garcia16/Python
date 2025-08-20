for i in range(cantidad_materias):
            materia = input(f"Ingrese la materia {i + 1}: ").lower()
            nota = float(input(f"Ingrese la nota de {materia}: "))
            materias_notas[materia] = nota
        sistema_estudiantes[estudiante] = materias_notas