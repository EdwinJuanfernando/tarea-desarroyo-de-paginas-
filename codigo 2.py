def eliminar_espacios_repetidos(cadena):
    palabras = cadena.split()
    cadena_limpia = ' '.join(palabras)
    return cadena_limpia
entrada = "Hola     mundo     en Python"
salida = eliminar_espacios_repetidos(entrada)
print(salida)