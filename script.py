import json, os
from usuario import Usuario
from datetime import datetime



lista = []

try:
    with open('usuarios.txt') as usuarios:
        for line in usuarios:
            try:
                usuario = json.loads(line)
                nuevo_usuario = Usuario(usuario["nombre"], usuario["apellido"], usuario["email"], usuario["genero"])
                lista.append(nuevo_usuario)
            except Exception as e:
                fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                mensaje_error = str(e)
                linea_error = f"{fecha_hora}  !Error al procesar la linea! : {mensaje_error}\n"
                with open("error.log", "a+") as log:
                    log.write(linea_error)
                    log.close

except FileNotFoundError:
    print("No se encontro el archivo")


                