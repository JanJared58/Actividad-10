empleados = [
    {"nombre": "Juan Pérez", "edad": 30, "salario": 50000},
    {"nombre": "María López", "edad": 25, "salario": 55000},
    {"nombre": "Carlos García", "edad": 35, "salario": 60000}
]

def escribir_empleados(empleados, archivo_salida):

    with open(archivo_salida, "w", encoding="utf8") as file:
        file.write("=== Datos de Empleados ===\n")
        file.write("==========================\n\n")
        for empleado in empleados:
            file.write("Empleado:\n")
            file.write("---------\n")
            file.write(f"Nombre: {empleado['nombre']}\n")
            file.write(f"Edad: {empleado['edad']} años\n")
            file.write(f"Salario: ${empleado['salario']:.2f}\n")
            file.write("\n")

escribir_empleados(empleados, "empleados.txt")
print("Los datos se han guardado en 'empleados.txt'.")
