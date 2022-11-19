import pywhatkit 
from pywhatkit.remotekit import start_server
from flask import Flask

def enviarMensaje():
    numero = str(input("Aqui el numero de telefono al que le inviaremos mensaje (con +52 O numero de pais): ")) 
    mensaje = input("¿Que le quieres decir? ")
    hora = int(input("A que hora le llegara el mensaje (24-HRS): "))
    minutos = int(input("¿En que minuto le llegara?: "))
    print("Buscando.....")
    pywhatkit.sendwhatmsg(numero, mensaje, hora, minutos)
    print("\nMensaje enviado ")
# ENVIAR UN MENSAJE DE WhattApp a las 1:30 PM
#pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30)

def enviarImagen():
    numero = input("Aqui el numero de telefono al que le inviaremos mensaje (con +52 O numero de pais): ")
    imagen = input("¿Cual es la ruta de archivo?: ")
    print("Buscando.....")
    pywhatkit.sendwhats_image(numero, imagen)
    print("\nMensaje enviado ")
# Enviar una imagen a un contacto 
#pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")

def enviarMensajeYcerrarELnavegador():
    numero = input("Aqui el numero de telefono al que le inviaremos mensaje (con +52 O numero de pais): ")
    mensaje = input("¿Que le quieres decir? ")
    hora = int(input("A que hora le llegara el mensaje (24-HRS): "))
    minutos = int(input("¿En que minuto le llegara?: "))
    mili = int(input("¿Milisegundos? "))
    segundos = int(input("¿A los cuantos segundos se cierra el navegador? "))
    print("Buscando.....")
    pywhatkit.sendwhatmsg(numero, mensaje, hora, minutos, mili,  True, segundos)
    print("\nMensaje enviado ")
# Lo mismo de enviar menasje pero ahora cierra la pestaña despues de 2 segundos 
#pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)

def enviarMensajeAunGrupoYimagen():
    clabe_grupo = input("¿Cual es el enlaze del grupo?: F76cih9tyf1DoYZhvq8T1i ")
    mensaje = input("¿Que le quieres decir?: ")
    imagen = input("¿Cual es la ruta de archivo?: ")
    print("Buscando.....")
    pywhatkit.sendwhats_image(clabe_grupo, imagen, mensaje)
    print("\nMensaje enviado ")
# Send an Image to a Group with the Caption as Hello
#pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")

def enviarMensajeAunGrupoHora():
    clabe_grupo = input("¿Cual es el enlaze del grupo?: F76cih9tyf1DoYZhvq8T1i ")
    mensaje = input("¿Que le quieres decir?: ")
    hora = int(input("A que hora le llegara el mensaje (24-HRS): "))
    segundos = int(input("¿En que minuto le llegara?: "))
    print("Buscando.....")
    pywhatkit.sendwhatmsg_to_group(clabe_grupo, mensaje, hora, segundos)
    print("\nMensaje enviado ")
# Send a WhatsApp Message to a Group at 12:00 AM
#pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)

def enviarMensajeAunGrupoahora():
    clabe_grupo = input("¿Cual es el enlaze del grupo?: F76cih9tyf1DoYZhvq8T1i ")
    mensaje = input("¿Que le quieres decir?: ")
    print("Buscando.....")
    pywhatkit.sendwhatmsg_to_group_instantly(clabe_grupo, mensaje)
    print("\nMensaje enviado ")
# Send a WhatsApp Message to a Group instantly
#pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")
while True:
    print("""
        Dime ¿Que quieres hacer?
        1. Enviar mensaje a un contacto
        2. Envair una foto a un contacto
        3. Enviar mensaje y cerrar el navegador
        4. Envair una foto a un grupo y mensaje 
        5. Envair un mensaje a un grupo a una hora especifica 
        6. Envair mensaje a un grupo ahora 
        7. salir
        """)

    opcion = int(input("Elije una opcion: "))
    if opcion == 1:
        enviarMensaje()
    elif opcion == 2:
        enviarImagen()        
    elif opcion == 3:
        enviarMensajeYcerrarELnavegador()    
    elif opcion ==4:
        enviarMensajeAunGrupoYimagen()    
    elif opcion ==5:
        enviarMensajeAunGrupoHora()   
    elif opcion ==6:
        enviarMensajeAunGrupoahora()   
    elif opcion ==7:
        break 
    else: 
        print("\n Opcion incorrecta") 
