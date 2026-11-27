def limpiar_frase(frase: str) -> str:
    """Elimina signos de puntuacion, convierte a minusculas y deja un solo espacio entre palabras."""
    signos = ".,;:!?¿¡"
    texto_limpio = ""
    for caracter in frase:
        if caracter not in signos:
            texto_limpio += caracter
    palabras = texto_limpio.lower().split()
    return " ".join(palabras)


def contar_vocales(texto: str) -> int:
    """Cuenta cuantas vocales (a, e, i, o, u) contiene una cadena sin distinguir mayusculas."""
    contador = 0
    for caracter in texto.lower():
        if caracter in "aeiou":
            contador += 1
    return contador


def vocales_por_palabra(frase: str) -> dict:
    """Devuelve un diccionario con cada palabra limpia y su cantidad de vocales."""
    frase_limpia = limpiar_frase(frase)
    palabras = frase_limpia.split()
    resultado = dict()
    for palabra in palabras:
        resultado[palabra] = contar_vocales(palabra)
    return resultado


def contar_palabras(frase: str) -> dict:
    """Devuelve un diccionario con la frecuencia de cada palabra en minusculas."""
    palabras = frase.lower().split()
    conteo = dict()
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo


def agrupar_por_longitud(palabras: list) -> dict:
    """Agrupa una lista de palabras en un diccionario segun su longitud."""
    grupos = dict()
    for palabra in palabras:
        largo = len(palabra)
        if largo in grupos:
            grupos[largo].append(palabra)
        else:
            grupos[largo] = [palabra]
    return grupos