from utilidades import comprobar_numero

def comprobar_longitud(contrasena):
    return len(contrasena) >= 8

contrasena = "Hola1234"
print(contrasena)
print(comprobar_longitud(contrasena))
print(comprobar_numero(contrasena))