def tiene_extension_correcta(nombre_archivo, extension=".pdf"):
    return nombre_archivo.endswith(extension)
archivo1 = "documento.jpg"
archivo2 = "imagen.jpg"

resultado1 = tiene_extension_correcta(archivo1)
resultado2 = tiene_extension_correcta(archivo2)

print(f"{archivo1}: {resultado1}")  # Salida: documento.pdf: True
print(f"{archivo2}: {resultado2}")  # Salida: imagen.jpg: False