def obtener_precio_usuario():
    entrada = input("Enter the item's price:\n")
    """El usuario debe ingresar un precio"""
    return float(entrada)
precio = obtener_precio_usuario()
print(precio)