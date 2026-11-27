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