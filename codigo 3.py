def extraer_dominio(correo):
    partes = correo.split('@')
    if len(partes) != 2:
        print("Formato de correo electrónico incorrecto.")
        return None

    dominio = partes[1]

    return dominio

correo = "usuario@gmail.com"
dominio = extraer_dominio(correo)
print(dominio)