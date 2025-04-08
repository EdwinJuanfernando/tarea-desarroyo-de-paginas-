def rellenar_arreglo_con_multiplos(tamaño, numero_base):
    arreglo = []
    for i in range(1, tamaño + 1):
        arreglo.append(numero_base * i)
    return arreglo

def main():
    tamaño = int(input("Por favor, ingrese el tamaño del arreglo: "))
    numero_base = int(input("Por favor, ingrese el número base: "))
    arreglo = rellenar_arreglo_con_multiplos(tamaño, numero_base)
    print("El arreglo con los múltiplos es:", arreglo)
if __name__ == "__main__":
    main()