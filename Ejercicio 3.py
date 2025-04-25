with open("numeros.txt", "r") as archivo:
    
    numeros = [int(linea.strip()) for linea in archivo]


suma = sum(numeros)


print(f"La suma total es: {suma}")

