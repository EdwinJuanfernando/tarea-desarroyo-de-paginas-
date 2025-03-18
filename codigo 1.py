def extraer_palabras(oracion):
    oracion_limpia = oracion.strip()

    palabras = oracion_limpia.split()

    if len(palabras) == 0:
        print("La oración está vacía.")
        return

    primera_palabra = palabras[0]

    ultima_palabra = palabras[-1]

    print(f"Primera palabra: {primera_palabra}, Última palabra: {ultima_palabra}")
oracion = "Python es un lenguaje poderoso y versátil"
extraer_palabras(oracion)
