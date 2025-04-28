def cargar_estudiantes(nombre_archivo):
    lista_estudiantes = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split(',')
            if len(datos) < 7: 
                continue
            estudiante = {
                "nombre": datos[0],
                "edad": int(datos[1]),
                "calificaciones": list(map(float, datos[2:7]))
            }
            lista_estudiantes.append(estudiante)
    return lista_estudiantes

def guardar_estudiantes(nombre_archivo, lista_estudiantes):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for estudiante in lista_estudiantes:
    
            linea = f'{estudiante["nombre"]},{estudiante["edad"]},'
            linea += ",".join(str(calif) for calif in estudiante["calificaciones"])
            archivo.write(linea + "\n")

archivo = "estudiantes.txt"
estudiantes = cargar_estudiantes(archivo)

print("Datos de estudiantes:")
for estudiante in estudiantes:
    print(estudiante)

nombre_modificar = "María"
for estudiante in estudiantes:
    if estudiante["nombre"] == nombre_modificar:
        estudiante["edad"] = 22
        estudiante["calificaciones"][0] = 10.0 
        print(f"\nActualización realizada para {nombre_modificar}:")
        print(estudiante)
        break
else:
    print(f"\nNo se encontró el estudiante con nombre {nombre_modificar}.")

guardar_estudiantes(archivo, estudiantes)
print(f"\nCambios guardados en {archivo}.")
