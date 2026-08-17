def reservar(reservas, fecha, huesped, habitacion, precio):
    if any(h == habitacion for _, h, _ in reservas.get(fecha, [])):
        return "Habitación no disponible"

    reservas.setdefault(fecha, []).append((huesped, habitacion, precio))
    return "Reserva realizada"


reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}

print(reservar(reservas, "2024-08-15", "Pedro", 103, 200))
print(reservas)