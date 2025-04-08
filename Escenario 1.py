def clasifica_evaluaciones(n):
    import numpy as np
    calificaciones = []
    for i in range(n):
        calificacion = int(input("Ingrese la calificación del cliente {}: ".format(i+1)))
        calificaciones.append(calificacion)
    counts = np.array([calificaciones.count(i) for i in range(1,6)])
    print("Respuestas:")
    print("Excelente: {}".format(counts[4]))
    print("Muy Buena: {}".format(counts[3]))
    print("Buena: {}".format(counts[2]))
    print("Regular: {}".format(counts[1]))
    print("Malo: {}".format(counts[0]))
    calif_max = np.argmax(counts)+1
    print("Más frecuente: {}".format(calif_max))
    promedio = np.mean(calificaciones)
    print("Promedio: {:.2f}".format(promedio))
    count_menor_promedio = 0
    for i in range(n):
        if calificaciones[i] < promedio:
            count_menor_promedio += 1
    porcentaje_menor_promedio = (count_menor_promedio/n) * 100
    print("Porcentaje menor al promedio: {:.2f}%".format(porcentaje_menor_promedio))