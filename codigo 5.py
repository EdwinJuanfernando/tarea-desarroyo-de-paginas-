def invertir_orden_palabras(texto):
    palabras = texto.split()

    palabras_invertidas = palabras[::-1]

    texto_invertido = ' '.join(palabras_invertidas)

    return texto_invertido

entrada = "Me gusta Python"
salida = invertir_orden_palabras(entrada)
print(salida)