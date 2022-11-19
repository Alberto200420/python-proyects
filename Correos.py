#PROGRAMA PARA MANDAR CORREOS MASIVOS

from email.message import (EmailMessage,)  # Libreria que viene con python para embiar email
import ssl  # Libreria Seguridad SSL que viene con python
import smtplib
import imghdr  # Libreria lectura de archivos que viene con python
import csv

print("Software creado por el de la silla todos los derechos reservados prohibida la distribución ")

emailEmisor = input("\n¿Cual es el correo que va a enviar los correos? ")  # Necesitas la contraseña del correo
emailContraseña = input("\n¿Cual es la contraseña? (Contraseña generada por google URL = myaccount.google.com/u/1/apppasswords llenas datos y te da contraseña, si ya la tienes no generes otra contraseña): ")
# Contraseña generada por google URL = myaccount.google.com/u/1/apppasswords llenas datos y te da contraseña 
emailResepor = input("\n¿Cual es la ruta de archivo de los correos? ")
asunto = input("\nTITULO DEL CORREO: ")
foto = input("\nFoto que adjuntaras con el correo 'jpg o png' RUTA DE ARCHIVO!!: ")
foto2 = input("\nLa otra foto que adjuntaras con el correo 'jpg o png' RUTA DE ARCHIVO!!: ")
cuerpo = input("\n¿Que pondras en el cuerpo del correo? ")

lista_de_correos = []
with open(emailResepor) as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        printe = ", ".join(row)
        lista_de_correos.append(printe)

for usuario in lista_de_correos:
    em = EmailMessage()  # Con esta funcion puedo definir el emisor
    em["form"] = emailEmisor
    em["to"] = usuario
    em["subject"] = asunto
    em.set_content(cuerpo)

    with open(foto, "rb") as file:  # rb = Read byts 'as file' representa open(foto, 'rb')
        file_data = file.read()  # Leer archivo .read
        file_tipo = imghdr.what(file.name)  # Libreria 'imghdr' lee el tipo de archivo que es
        file_nombre = file.name  # Obteniendo el nombre del archivo
    em.add_attachment(file_data, subtype=file_tipo, maintype="image")  # AÑADIENDO EL ARHIVO A EL CORREO , filename=file_nombre2 | filename=file_nombre

    with open(foto2, "rb") as files:
        file_data2 = files.read()
        file_tipo2 = imghdr.what(files.name)
        file_nombre2 = files.name
    em.add_attachment(file_data2, subtype=file_tipo2, maintype="image")

    # -- CREANDO SEGURIDAD DE ENVIO ENTRE 2 SISTEMAS
    contexto = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=contexto) as smtp:
        smtp.login(emailEmisor, emailContraseña)
        smtp.sendmail(emailEmisor, usuario, em.as_string())

print("\nCorreo enviado, viste que fácil era?")