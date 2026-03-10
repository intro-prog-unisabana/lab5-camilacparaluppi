def promedio_estudiante(calificaciones):
    return sum(calificaciones) / len(calificaciones)
calificaciones = [85, 92, 78]
prom = promedio_estudiante(calificaciones)
print(float(prom))