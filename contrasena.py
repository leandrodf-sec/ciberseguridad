from utilidades import comprobar_numero

def comprobar_longitud(contrasena):

    return len(contrasena) >= 12

def comprobar_mayuscula(contrasena):
    return any(c.isupper() for c in contrasena)

contrasena = "Hola1234"
print(contrasena)
print(comprobar_longitud(contrasena))
print(comprobar_numero(contrasena))
print(comprobar_mayuscula(contrasena))