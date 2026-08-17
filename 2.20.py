def configurar_app(**configuraciones):
    return configuraciones

ajustes = configurar_app(modo_oscuro=True, idioma="es", notificaciones=False)

print(ajustes)
