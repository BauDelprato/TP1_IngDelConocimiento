def analizar_encuestas(encuestas):
    return {
        pregunta: {r: respuestas.count(r) for r in set(respuestas)}
        for pregunta, respuestas in encuestas.items()
    }

encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

print(analizar_encuestas(encuestas))