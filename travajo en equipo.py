# =========================================
# Sistema de Monitoreo de Crecimiento Infantil
# =========================================

# Tabla de tallas promedio (OMS)
tallas_estandar = {
    0: 49.5, 1: 54.7, 2: 58.4, 3: 61.4, 4: 63.9, 5: 65.9, 6: 66.7,
    7: 68.5, 8: 69.8, 9: 71.0, 10: 72.2, 11: 73.2, 12: 75.0,
    13: 76.7, 14: 77.0, 15: 78.9, 16: 80.0, 17: 81.1, 18: 81.7,
    19: 83.0, 20: 83.8, 21: 84.5, 22: 85.2, 23: 85.9, 24: 86.4
}

# Valores de referencia simulados (solo para peso y craneo)
referencia_oms = {
    edad: {
        "peso": (5 + edad * 0.2, 8 + edad * 0.2),
        "craneo": (40 + edad * 0.1, 47 + edad * 0.1)
    }
    for edad in range(0, 25)
}

# Lista de los 22 departamentos de Guatemala
departamentos_gt = [
    "Alta Verapaz", "Baja Verapaz", "Chimaltenango", "Chiquimula", "El Progreso",
    "Escuintla", "Guatemala", "Huehuetenango", "Izabal", "Jalapa", "Jutiapa",
    "Petén", "Quetzaltenango", "Quiché", "Retalhuleu", "Sacatepéquez", "San Marcos",
    "Santa Rosa", "Sololá", "Suchitepéquez", "Totonicapán", "Zacapa"
]

# Clase Niño/a
class Nino:
    def __init__(self, edad, peso, talla, craneo, departamento, genero):
        self.edad = edad
        self.peso = peso
        self.talla = talla
        self.craneo = craneo
        self.departamento = departamento
        self.genero = genero  # Masculino o Femenino

    def clasificar(self, valor, indicador):
        if indicador == "talla":
            if self.edad not in tallas_estandar:
                return "Desconocido"
            promedio = tallas_estandar[self.edad]
            diferencia = valor - promedio
            if abs(diferencia) < 0.1:
                return "Ideal"
            elif diferencia < 0:
                return f"Bajo ({round(abs(diferencia), 1)} cm por debajo)"
            else:
                return f"Sobre ({round(diferencia, 1)} cm por encima)"
        else:
            min_ref, max_ref = referencia_oms[self.edad][indicador]
            if valor < min_ref:
                return "Bajo"
            elif valor > max_ref:
                return "Sobre"
            else:
                return "Dentro"

    def clasificacion_completa(self):
        return {
            "peso": self.clasificar(self.peso, "peso"),
            "talla": self.clasificar(self.talla, "talla"),
            "craneo": self.clasificar(self.craneo, "craneo")
        }

# Lista para almacenar los datos
datos = []

# Función para ingresar un niño o niña
def agregar_nino():
    print("\n--- Ingreso de nuevo niño o niña ---")
    try:
        print("Seleccione el género:")
        print("1. Masculino")
        print("2. Femenino")
        opcion_genero = input("Opción (1 o 2): ").strip()
        if opcion_genero == "1":
            genero = "Masculino"
        elif opcion_genero == "2":
            genero = "Femenino"
        else:
            raise ValueError("Opción de género no válida.")

        edad = int(input("Edad (0-24 meses): "))
        if edad < 0 or edad > 24:
            raise ValueError("Edad fuera de rango")

        peso = float(input("Peso (kg): "))
        talla = float(input("Talla (cm): "))
        craneo = float(input("Perímetro craneal (cm): "))

        print("\nSeleccione el departamento:")
        for i, dep in enumerate(departamentos_gt, 1):
            print(f"{i}. {dep}")
        opcion_dpto = int(input("Número del departamento (1-22): "))
        if 1 <= opcion_dpto <= 22:
            dpto = departamentos_gt[opcion_dpto - 1]
        else:
            raise ValueError("Número de departamento fuera de rango.")

        n = Nino(edad, peso, talla, craneo, dpto, genero)
        datos.append(n)

        print("\n✅ Datos ingresados correctamente.")
        clasificacion = n.clasificacion_completa()
        print("📋 Clasificación individual:")
        print(f"  Género: {genero}")
        print(f"  Peso:   {clasificacion['peso']}")
        print(f"  Talla:  {clasificacion['talla']}")
        print(f"  Cráneo: {clasificacion['craneo']}")

    except Exception as e:
        print(f"⚠️ Error al ingresar datos: {e}")

# Función para generar informe por departamento
def generar_informes():
    if not datos:
        print("⚠️ No hay datos ingresados.")
        return

    print("\n📊 Informe por departamento:")
    departamentos = set(n.departamento for n in datos)
    for dpto in departamentos:
        niños_dpto = [n for n in datos if n.departamento == dpto]
        print(f"\nDepartamento: {dpto}")
        for indicador in ["peso", "talla", "craneo"]:
            conteo = {"Bajo": 0, "Dentro": 0, "Ideal": 0, "Sobre": 0}
            total = len(niños_dpto)
            for n in niños_dpto:
                clasif = n.clasificacion_completa()[indicador]
                if clasif.startswith("Bajo"):
                    conteo["Bajo"] += 1
                elif clasif.startswith("Sobre"):
                    conteo["Sobre"] += 1
                elif clasif == "Dentro":
                    conteo["Dentro"] += 1
                elif clasif == "Ideal":
                    conteo["Ideal"] += 1
            print(f"  {indicador.capitalize()}: "
                  f"Bajo {conteo['Bajo']*100/total:.0f}%, "
                  f"Dentro {conteo['Dentro']*100/total:.0f}%, "
                  f"Ideal {conteo['Ideal']*100/total:.0f}%, "
                  f"Sobre {conteo['Sobre']*100/total:.0f}%")

# Menú interactivo principal
def menu():
    while True:
        print("\n📌 MENÚ PRINCIPAL")
        print("1. Ingresar nuevo niño o niña")
        print("2. Generar informe por departamento")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_nino()
        elif opcion == "2":
            generar_informes()
        elif opcion == "3":
            print("👋 Saliendo del programa.")
            break
        else:
            print("⚠️ Opción no válida.")

# Iniciar programa
menu()


#Rodrigo,Darwin.Edwin