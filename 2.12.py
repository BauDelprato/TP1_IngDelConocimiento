productos = [
    ("laptop", 1200, 5),
    ("mouse", 25, 50),
    ("teclado", 100, 30)
]

def producto_mas_caro(productos):
    mas_caro = productos[0]

    for producto in productos:
        if producto[1] > mas_caro[1]:
            mas_caro = producto

    return mas_caro

print(producto_mas_caro(productos))