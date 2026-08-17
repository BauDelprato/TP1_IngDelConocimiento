def publicar(usuario, texto, **kwargs):
    return {"usuario": usuario, "texto": texto, **kwargs}

print(publicar(
    "Juan",
    "Mi primer post!",
    etiquetas=["#hola", "#primerPost"],
    visibilidad="publica",
    likes=100
))