def leer_nombres_de_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            lista_nombres = archivo.read().splitlines() 
        return lista_nombres
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no se encontró.")
        return []

archivo_entrada = "nombres.txt"
nombres = leer_nombres_de_archivo(archivo_entrada)

if nombres:
    print("Lista de nombres:")
    print(nombres)
