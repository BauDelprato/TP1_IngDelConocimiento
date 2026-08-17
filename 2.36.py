inventario = {
    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}


def actualizar_inventario(**kwargs):
    tienda = kwargs["tienda"]

    for producto, cantidad in kwargs.items():
        if producto != "tienda":
            inventario[tienda][producto] += cantidad

    return inventario[tienda]


resultado = actualizar_inventario(
    tienda="Tienda A",
    producto_1=10,
    producto_2=-5
)

print(resultado)