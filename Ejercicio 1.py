def guardar_nombres_en_archivo(nombre_archivo):
    print("Introduce los nombres uno por uno. Escribe 'salir' para finalizar.")
    lista_nombres = []

    while True:
        nombre = input("Nombre: ")
        if nombre.lower() == 'salir':
            break
        lista_nombres.append(nombre)

    with open(nombre_archivo, 'w') as archivo:
        for nombre in lista_nombres:
            archivo.write(nombre + '\n')

    print(f"Los nombres han sido guardados en {nombre_archivo}")

archivo_salida = "nombres.txt"
guardar_nombres_en_archivo(archivo_salida)
