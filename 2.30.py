def configurar_perfiles(usuarios, **kwargs):
    return {usuario: list(kwargs.values()) for usuario in usuarios}

usuarios = ["Ana", "Luis", "María"]

print(configurar_perfiles(
    usuarios,
    idioma="es",
    modo_oscuro=True,
    notificaciones=False
))