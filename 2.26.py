def registro_empleado(nombre, edad, salario, **kwargs):
    return {"nombre": nombre, "edad": edad, "salario": salario, **kwargs}

print(registro_empleado(
    "Ana", 30, 3000,
    direccion="Calle Falsa 123",
    telefono="123456789"
))