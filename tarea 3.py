def main():
    tamaño = int(input("Por favor, ingrese el tamaño de los vectores: "))
    nombres = []
    longitudes = []
    for i in range(tamaño):
        nombre = input(f"Ingrese el nombre {i+1}: ")
        nombres.append(nombre)
        longitudes.append(len(nombre))
    print(f"Array1 (Nombres): {nombres}")
    print(f"Longitud (Longitudes de los nombres): {longitudes}")
if __name__ == "__main__":
    main()