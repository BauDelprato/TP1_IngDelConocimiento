def crear_perfil(nombre, edad, email, **kwargs):
    perfil = {
        "nombre": nombre,
        "edad": edad,
        "email": email,
    }
    perfil.update(kwargs)
    return perfil


resultado = crear_perfil(
    nombre="Luis", edad=25, email="juan@mail.com", ciudad="Mendoza"
)
print(resultado)