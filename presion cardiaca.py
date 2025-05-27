# Número de días a registrar
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes","sabado", "Domingo"]

# Datos simulados de 1 semana de paciente
niveles_azucar = [130, 160, 95, 175, 160]     # mg/dL
niveles_sal = [2000, 2400, 1800, 2400, 2700]  # mg
presion_sistolica = [115, 130, 110, 125, 175]           # mmHg
presion_diastolica = [78, 79, 85,89 , 92]           # mmHg
# Definición de funciones para evaluar cada parámetro

def evaluar_azucar(azucar):
    if 70 <= azucar <= 140:
        return "Azúcar en sangre dentro del rango normal."
    else:
        return "Alerta: Azúcar en sangre fuera del rango saludable!"

def evaluar_sal(sal):
    if sal <= 2300:
        return "Consumo de sal dentro del rango normal."
    else:
        return "Alerta: Consumo de sal excede el límite saludable!"

def clasificar_presion(sist, diast):
    if sist < 120 and diast < 80:
        return "Presión arterial normal."
    elif 120 <= sist <= 129 and diast < 80:
        return "Presión arterial elevada."
    elif 130 <= sist <= 139 or 80 <= diast <= 89:
        return "Hipertensión Etapa 1."
    elif sist >= 140 or diast >= 90:
        return "Hipertensión Etapa 2."
    else:
        return "Valores de presión arterial fuera de rango esperado sesesita ser internado :("

def evaluar_presion(sist, diast):
    clasificacion = clasificar_presion(sist, diast)
    alerta = ""
    if clasificacion != "Presión arterial normal .":
        alerta = "Alerta: " + clasificacion + " Se recomienda intervención médica."
    else:
        alerta = clasificacion
    return alerta

def promedio(lista):
    return sum(lista) / len(lista)

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes","sabado","Domingo"]

azucares = []
sales = []
presiones_sist = []
presiones_diast = []

print("Ingrese los datos para cada día para ver como se encuentranlos pacientes que vienen y su estado:")

for dia in dias:
    print(f"\n{dia}:")
    azucar = float(input("  Nivel de azúcar en sangre (mg/dL): "))
    sal = float(input("  Consumo de sal (mg): "))
    sist = float(input("  Presión sistólica (mmHg): "))
    diast = float(input("  Presión diastólica (mmHg): "))

    azucares.append(azucar)
    sales.append(sal)
    presiones_sist.append(sist)
    presiones_diast.append(diast)

    print(evaluar_azucar(azucar))
    print(evaluar_sal(sal))
    print(evaluar_presion(sist, diast))

# Resultados promedio semanal
print("\n--- Resultados promedio semanal ---")
prom_azucar = promedio(azucares)
prom_sal = promedio(sales)
prom_sist = promedio(presiones_sist)
prom_diast = promedio(presiones_diast)

print(f"Promedio azúcar en sangre: {prom_azucar:.2f} mg/dL - {evaluar_azucar(prom_azucar)}")
print(f"Promedio consumo de sal: {prom_sal:.2f} mg - {evaluar_sal(prom_sal)}")
print(f"Promedio presión arterial: {prom_sist:.2f}/{prom_diast:.2f} mmHg - {evaluar_presion(prom_sist, prom_diast)}")

#Edwin