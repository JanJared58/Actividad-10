import re

def validar_telefono(numero):
   
    patron = r"^\+(?:\d{2}-\d{4}-\d{4}|\d{2}\s\d{4}\s\d{4})$"
    return re.match(patron, numero) is not None

def main():
    numero = input("Introduce un número de teléfono (+XX-XXXX-XXXX o +XX XXXX XXXX): ")
    if validar_telefono(numero):
        print("El número de teléfono es válido.")
    else:
        print("El número de teléfono NO es válido.")

if __name__ == "__main__":
    main()
