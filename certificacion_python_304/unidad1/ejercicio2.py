try:
    alumnos=["emyli","carlos","america","luis","sdana"]
    calificaciones=["6.0","7.0","8.3","6.7","8.0"]
    print("alumno:",alumnos[1])
    print("calificaciones:",calificaciones[1])
    print("alumno:",alumnos[3])
    print("calificaciones:",calificaciones[3])
except IndexError:
    print("no se encontro el alumno o la calificacion")