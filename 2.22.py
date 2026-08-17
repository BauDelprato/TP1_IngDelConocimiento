def precios_totales(paquetes):
    return {destino: precio * dias for destino, precio, dias in paquetes}

paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

print(precios_totales(paquetes))