def limpiar_frase(frase: str) -> str:
    """Funcion que quita signos de puntuacion, pasa a minusculas y deja un espacio entre palabras."""
    signos = ".,;:!?¿¡"
    limpia = ""
    for letra in frase:
        if letra not in signos:
            limpia += letra
    palabras = limpia.lower().split()
    return " ".join(palabras)


def contar_vocales(texto: str) -> int:
    """Funcion que acepta una cadena y devuelve cuantas vocales tiene."""
    contador = 0
    for letra in texto.lower():
        if letra in "aeiou":
            contador += 1
    return contador


def vocales_por_palabra(frase: str) -> dict:
    """Funcion que devuelve un diccionario con cada palabra limpia y sus vocales."""
    frase_limpia = limpiar_frase(frase)
    palabras = frase_limpia.split()
    conteo = dict()
    for palabra in palabras:
        conteo[palabra] = contar_vocales(palabra)
    return conteo


def contar_palabras(frase: str) -> dict:
    """Funcion que cuenta cuantas veces aparece cada palabra en minusculas."""
    palabras = frase.lower().split()
    conteo = dict()
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo


def agrupar_por_longitud(palabras: list) -> dict:
    """Funcion que agrupa una lista de palabras en un diccionario segun su largo."""
    grupos = dict()
    for palabra in palabras:
        largo = len(palabra)
        if largo in grupos:
            grupos[largo].append(palabra)
        else:
            grupos[largo] = [palabra]
    return grupos