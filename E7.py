import re

patron = r'^[A-Za-z]+@[A-Za-z]+\.[A-Za-z]{3}$'

emails = [
    "usuario@dominio.com",   
    "Juan@Empresa.net",      
    "user123@dominio.org",   
    "usuario@dominio.co",    
    "usuario@dominio.comm"   
]

for email in emails:
    if re.match(patron, email):
        print(f"{email} es válido")
    else:
        print(f"{email} no es válido")
