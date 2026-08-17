def actualizar(inventario, ventas):
    return [i - v for i, v in zip(inventario, ventas)]

inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]

print(actualizar(inventario, ventas))