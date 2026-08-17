def calcular_goles_temporada(**resultados_partidos):
    goles_anotados = sum(goles[0] for goles in resultados_partidos.values())
    goles_recibidos = sum(goles[1] for goles in resultados_partidos.values())
    return goles_anotados, goles_recibidos

resultados = {
    "Equipo_A": (3, 2),
    "Equipo_B": (1, 1),
    "Equipo_C": (4, 0)
}

anotados, recibidos = calcular_goles_temporada(**resultados)

print(f"Total de goles anotados: {anotados}")
print(f"Total de goles recibidos: {recibidos}")
