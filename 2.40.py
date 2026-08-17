def ranking_estudiantes(estudiantes):
    ranking = []

    for id_estudiante, materias in estudiantes.items():
        notas = []

        for calificaciones in materias.values():
            notas.extend(calificaciones)

        promedio = sum(notas) / len(notas)

        ranking.append((id_estudiante, promedio))

    ranking.sort(key=lambda x: x[1], reverse=True)

    return ranking


estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

resultado = ranking_estudiantes(estudiantes)

print(resultado)