def ordenar_puntuaciones(lista_puntuaciones):
    return sorted(lista_puntuaciones, key=lambda x: x, reverse=True)

puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]
resultado = ordenar_puntuaciones(puntuaciones)

print(resultado)
