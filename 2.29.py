def promedios(notas):
    return {nombre: sum(calificaciones) / len(calificaciones)
            for nombre, calificaciones in notas}

notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]

print(promedios(notas_estudiantes))