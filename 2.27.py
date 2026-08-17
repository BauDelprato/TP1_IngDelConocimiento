def estadisticas_ventas(ventas):
    return {
        "total": sum(ventas),
        "promedio": sum(ventas) / len(ventas),
        "mes_mayores_ventas": ventas.index(max(ventas)) + 1
    }

ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]

print(estadisticas_ventas(ventas_mensuales))