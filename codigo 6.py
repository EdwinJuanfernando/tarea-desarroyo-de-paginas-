def detectar_palabras_clave(texto):
    textos_predefinidos = {
        "poema": "Podrá nublarse el sol eternamente;\nPodrá secarse en un instante el mar;\nPodrá romperse el eje de la tierra\nComo un débil cristal.",
        "canción": "Eres como la noche, callada y constelada.\nTu silencio es de estrella, tan lejano y sencillo.\nMe gustas cuando callas porque estás como ausente.\nDistante y dolorosa como si hubieras muerto."
    }
    
    texto_minusculas = texto.lower()
    
    for palabra_clave, texto_predefinido in textos_predefinidos.items():
        if palabra_clave in texto_minusculas:
            return texto_predefinido
    
    return "No se encontraron palabras clave correspondientes."

texto_usuario = input("Ingrese un texto: ")
resultado = detectar_palabras_clave(texto_usuario)
print(resultado)