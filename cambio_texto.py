def invertir(d: dict) -> dict:
    """Funcion que intercambia las claves por los valores en un diccionario nuevo."""
    nuevo = dict()
    for clave, valor in d.items():
        nuevo[valor] = clave
    return nuevo


def filtrar_por_valor(d: dict, minimo: float) -> dict:
    """Funcion que devuelve un diccionario solo con los valores mayores o iguales al minimo."""
    nuevo = dict()
    for clave, valor in d.items():
        if valor >= minimo:
            nuevo[clave] = valor
    return nuevo


def sumar_valores(d: dict):
    """Funcion que suma todos los valores numericos de un diccionario."""
    total = 0
    for clave, valor in d.items():
        total += valor
    return total