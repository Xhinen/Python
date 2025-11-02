""" Ejercicio 8 - Generar un log de accesos
Escribe un programa que simule un sistema de acceso a un recurso protegido. 
El programa debe pedir al usuario un nombre de usuario y una contraseña, y verificar si son correctos.
Si el acceso es exitoso, debe registrar la fecha y hora del acceso en un archivo de log.
Si el acceso falla, debe registrar el intento fallido en el mismo archivo de log. El programa debe definir una función que realice esta tarea. """

from datetime import datetime

usuarios = {
    "jordi":"c0ntr4s3n4",
    "asires":"seguridad",
    "damdawers":"prototipo"
}

""" 
1º Verificar si existe el usuario
2º Comprobar la contraseña
3º Si user == ok: loguear un acceso exitoso
4º Si user != ok: loguear intento fallido
"""

def verify_user(user, passw):
    with open("log.txt", "a") as file:
        if user not in usuarios.keys():
            file.write(f"{datetime.now().isoformat(timespec="seconds")} Se ha intentado loguear un usuario NO EXISTENTE {user}\n")
            raise ValueError("Acceso denegado")
        if passw != usuarios[user]:
            file.write(f"{datetime.now().isoformat(timespec="seconds")} Se ha intentado loguear el usuario {user}\n")
            raise ValueError("Acceso denegado")
        
        file.write(f"{datetime.now().isoformat(timespec="seconds")} Se ha loguado EXITOSAMENTE el usuario {user}\n")


while True:
    user = input("Introduce tu usuario:\n")
    passw = input("Introduce tu password:\n")

    try:
        verify_user(user, passw)
    except Exception as e:
        print(e)