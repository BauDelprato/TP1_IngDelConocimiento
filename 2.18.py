ventas_diarias = [200, 450, 300, 400, 350, 500, 600]

def calcular_ventas(lista_ventas):
    total = 0
    promedio = 0

    for venta in lista_ventas:
        total += venta
        promedio += venta

    promedio = promedio / len(lista_ventas)

    return total, promedio

print( calcular_ventas(ventas_diarias))