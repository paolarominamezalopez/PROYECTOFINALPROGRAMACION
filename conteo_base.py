def promedio_sin_extremos(numeros: list) -> float:
    """Calcula el promedio de una lista excluyendo el valor maximo y el minimo."""
    if len(numeros) < 3:
        return sum(numeros) / len(numeros)
    copia = numeros.copy()
    copia.remove(max(copia))
    copia.remove(min(copia))
    return sum(copia) / len(copia)


def es_primo(n: int) -> bool:
    """Devuelve True si n es un numero primo y False en caso contrario."""
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def suma_digitos(n: int) -> int:
    """Recibe un numero entero positivo y devuelve la suma de sus digitos."""
    suma = 0
    for digito in str(n):
        suma += int(digito)
    return suma


def interseccion(a: list, b: list) -> list:
    """Devuelve los elementos que estan en ambas listas sin duplicados y en el orden de a."""
    resultado = []
    for elemento in a:
        if elemento in b and elemento not in resultado:
            resultado.append(elemento)
    return resultado


def eliminar_duplicados(lista: list) -> list:
    """Devuelve una nueva lista sin elementos repetidos conservando el orden original."""
    nueva = []
    for elemento in lista:
        if elemento not in nueva:
            nueva.append(elemento)
    return nueva


def segundo_mayor(numeros: list):
    """Devuelve el segundo valor mas grande de la lista sin contar repetidos, o None si no existe."""
    unicos = []
    for num in numeros:
        if num not in unicos:
            unicos.append(num)
    if len(unicos) < 2:
        return None
    ordenados = sorted(unicos, reverse=True)
    return ordenados[1]


def aplanar(lista: list) -> list:
    """Recibe una lista de listas y devuelve una sola lista con todos los elementos en orden."""
    resultado = []
    for sublista in lista:
        for elemento in sublista:
            resultado.append(elemento)
    return resultado