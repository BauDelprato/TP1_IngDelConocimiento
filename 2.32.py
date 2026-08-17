def simular_ventas(*ventas):
    return sum(cantidad * precio for producto, cantidad, precio in ventas)

print(simular_ventas(
    ("Producto A", 10, 15.0),
    ("Producto B", 5, 25.0),
    ("Producto C", 3, 50.0)
))