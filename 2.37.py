def analizar_tendencias(hashtags, tendencias, cantidad_minima):
    hashtags_validos = []

    for hashtag, frecuencia in tendencias:
        if frecuencia > cantidad_minima:
            hashtags_validos.append(hashtag)

    return hashtags_validos


hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]

tendencias = [
    ("#verano", 120),
    ("#moda", 80),
    ("#tecnologia", 150)
]

resultado = analizar_tendencias(hashtags, tendencias, 100)

print(resultado)