<<<<<<< HEAD
def revisar_datos_texto(texto):
    print("\n--- REPORTE DE ESTADISTICAS BASICAS ---")

    total_caracteres = len(texto)

    caracteres_sin_espacios = 0
    for caracter in texto:
        if caracter not in " \n":
            caracteres_sin_espacios += 1

    texto_sin_signos = ""
    for caracter in texto:
        if caracter in ".,;:!¡?¿":
            texto_sin_signos += " "
        else:
            texto_sin_signos += caracter

    palabras = texto_sin_signos.split()
    cantidad_palabras = len(palabras)

    cantidad_oraciones = 0
    for caracter in texto:
        if caracter in ".!?":
            cantidad_oraciones += 1

    if cantidad_oraciones == 0 and cantidad_palabras > 0:
        cantidad_oraciones = 1

    letras_en_palabras = 0
    for palabra in palabras:
        letras_en_palabras += len(palabra)

    if cantidad_palabras > 0:
        promedio_letras_palabra = letras_en_palabras / cantidad_palabras
    else:
        promedio_letras_palabra = 0

    if cantidad_oraciones > 0:
        promedio_palabras_oracion = cantidad_palabras / cantidad_oraciones
    else:
        promedio_palabras_oracion = 0

    print("Total  palabras:", cantidad_palabras)
    print("Caracteres con espacios:", total_caracteres)
    print("Caracteres sin espacios:", caracteres_sin_espacios)
    print("Total de oraciones:", cantidad_oraciones)
    print("Promedio de palabra:", round(promedio_letras_palabra, 2), "letras")
    print("Promedio de oracion:", round(promedio_palabras_oracion, 2), "palabras")
=======
def promedio_sin_extremos(numeros: list) -> float:
    """Funcion que calcula el promedio de una lista quitando el numero mayor y el menor."""
    if len(numeros) < 3:
        return sum(numeros) / len(numeros)
    copia = numeros.copy()
    copia.remove(max(copia))
    copia.remove(min(copia))
    return sum(copia) / len(copia)


def es_primo(n: int) -> bool:
    """Funcion que devuelve True si el numero es primo y False si no lo es."""
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def suma_digitos(n: int) -> int:
    """Funcion que recibe un entero positivo y devuelve la suma de sus digitos."""
    suma = 0
    for digito in str(n):
        suma += int(digito)
    return suma


def interseccion(a: list, b: list) -> list:
    """Funcion que devuelve los elementos repetidos entre dos listas sin duplicados."""
    resultado = []
    for elemento in a:
        if elemento in b and elemento not in resultado:
            resultado.append(elemento)
    return resultado


def eliminar_duplicados(lista: list) -> list:
    """Funcion que devuelve una lista nueva sin elementos repetidos."""
    nueva = []
    for elemento in lista:
        if elemento not in nueva:
            nueva.append(elemento)
    return nueva


def segundo_mayor(numeros: list):
    """Funcion que devuelve el segundo numero mas grande de la lista o None si no hay."""
    unicos = []
    for num in numeros:
        if num not in unicos:
            unicos.append(num)
    if len(unicos) < 2:
        return None
    ordenados = sorted(unicos, reverse=True)
    return ordenados[1]


def aplanar(lista: list) -> list:
    """Funcion que recibe una lista de listas y junta todos sus elementos en una sola."""
    resultado = []
    for sublista in lista:
        for elemento in sublista:
            resultado.append(elemento)
    return resultado
>>>>>>> 0140ca6149a52af34ea7ab67bb26e05270710377
