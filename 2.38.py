suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}


def actualizar_suscripcion(**kwargs):
    usuario = kwargs["usuario"]
    suscripcion = kwargs["suscripcion"]

    if usuario not in suscripciones:
        suscripciones[usuario] = []

    suscripciones[usuario].append(suscripcion)

    return suscripciones


resultado = actualizar_suscripcion(
    usuario="Luis",
    suscripcion="mensual",
    auto_renovacion=True
)

print(resultado)