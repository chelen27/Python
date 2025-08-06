"""Escriba un programa para validar si los datos de acceso (usuario y contraseña) se encuentran en el diccionario.
Validar a solo 3 intentos erroneos de contraseña utilizando ciclo while."""

usuarios = {
    "Aye": "2711", 
    "Mila": "2906", 
    "Sofi": "0305"
}

usuario = input("Ingrese su usuario: ")

if usuario in usuarios :
    intentos = 0
    while intentos < 3:
        contraseña = input("Ingrese su contraseña: ")
        if contraseña == usuarios[usuario]:
            print("Acceso permitido ✅")
            break
        else: 
            intentos = intentos + 1
            print("Acceso denegado 🔒")


if intentos == 3 :
    print("Demasiados intentos. Usuario bloqueado")
