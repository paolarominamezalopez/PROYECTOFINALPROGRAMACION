import os
from procesamiento_nlp import limpiar_frase, contar_vocales, vocales_por_palabra, contar_palabras, agrupar_por_longitud
from conteo_base import promedio_sin_extremos, es_primo, suma_digitos, interseccion, eliminar_duplicados, segundo_mayor, aplanar
from cambio_texto import invertir, filtrar_por_valor, sumar_valores

while True:
    archivo = input("Escribe el nombre del archivo .txt: ")
    if not archivo.endswith(".txt") or not os.path.exists(archivo):
        print("Archivo no permitido: no existe o no es .txt.")
    else:
        with open(archivo, "r", encoding="utf-8") as file:
            texto = file.read()
        if texto.strip() == "":
            print("Archivo no permitido: el archivo esta vacio.")
        else:
            break

limpia = limpiar_frase(texto)
print(limpia, contar_vocales(texto), vocales_por_palabra(texto), contar_palabras(limpia), agrupar_por_longitud(limpia.split()))
print(promedio_sin_extremos([1, 2, 3, 4, 100]), es_primo(7), suma_digitos(1234), interseccion([1, 2, 2, 3, 4], [2, 4, 5]), eliminar_duplicados([1, 2, 2, 3, 1]), segundo_mayor([10, 5, 20, 20]), aplanar([[1, 2], [3], [4, 5, 6]]), invertir({"a": 1, "b": 2, "c": 1}), filtrar_por_valor({"a": 3, "b": 8, "c": 5}, 5), sumar_valores({"a": 10, "b": 20, "c": 5}))