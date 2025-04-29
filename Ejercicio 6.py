def leer_empleados(nombre_archivo):

    empleados = []     
    empleado = {}      

    with open(nombre_archivo, "r", encoding="utf8") as file:
        for linea in file:
            linea = linea.strip() 
            if not linea:
                if empleado:
                    empleados.append(empleado)
                    empleado = {}
                continue
            if linea.startswith("Nombre:"):
                empleado["nombre"] = linea.split(":", 1)[1].strip()
            elif linea.startswith("Edad:"):
                edad_texto = linea.split(":", 1)[1].strip()
                edad_valor = edad_texto.split()[0]  
                empleado["edad"] = int(edad_valor)
            elif linea.startswith("Salario:"):
                salario_texto = linea.split(":", 1)[1].strip().replace("$", "")
                empleado["salario"] = float(salario_texto)
    if empleado:
        empleados.append(empleado)
    return empleados

lista_empleados = leer_empleados("empleados2.txt")

if lista_empleados:
    total_salario = sum(empleado["salario"] for empleado in lista_empleados)
    promedio_salario = total_salario / len(lista_empleados)
    print("Lista de empleados:")
    print(lista_empleados)
    print(f"\nSalario promedio: ${promedio_salario:.2f}")
else:
    print("No se encontraron datos de empleados en el archivo.")
