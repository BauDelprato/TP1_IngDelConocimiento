def simular_mercado(precios_diarios, operaciones):
    beneficio_total = 0
    precio_compra = 0

    for operacion, dia in operaciones:
        precio = precios_diarios[dia]

        if operacion == "compra":
            precio_compra = precio

        elif operacion == "venta":
            beneficio_total += precio - precio_compra

    return beneficio_total


precios_diarios = [100, 105, 102, 110, 108]

operaciones = [
    ("compra", 0),
    ("venta", 3),
    ("compra", 2),
    ("venta", 4)
]

resultado = simular_mercado(precios_diarios, operaciones)

print("Beneficio total:", resultado)