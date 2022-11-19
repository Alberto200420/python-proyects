def encriptar(texto):                            #Funcion encriptar(variable)
    print("Texto encriptado pa ")                #Resultado cuande se solicite la funcion  
    textoFinal = ''
    for letra in texto:
        cambio = ord(letra)                      # 'ord' Recibe la letra y La combierte en un numero espesifico 
        cambio += 10                             # Sumando para que cambie completamente el correspondiente
        textoFinal += chr(cambio)                # 'chr' Recibe el numero y La combierte en la letra que corresponde
    return textoFinal

def desencriptar(texto):
    print("Texto desencriptado pa eres hacker ")
    textoFinal = ''
    for letra in texto:
        cambio = ord(letra)
        cambio -= 10
        textoFinal += chr(cambio)
    return textoFinal

def encriptarArchivo(rutaDeArchivo):
    archivo = open(rutaDeArchivo, "r")             #'r' solo lee lo que hay en un archivo .txt 
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)
    archivo = open(rutaDeArchivo, "w")             #'w' remplaza cualquier contenido existente  Se crea archivo 'texto.txt' el 'a' te permite agregar texto al archivo 
    archivo.write(textoEncriptado)                 #Se guarda lo que va a ir escrito en el archivo 
    archivo.close()

def desencriptarArchivo(rutaDeArchivo):
    archivo = open(rutaDeArchivo, "r")             #'r' solo lee lo que hay en un archivo .txt 
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)
    archivo = open(rutaDeArchivo, "w")             #'w' remplaza cualquier contenido existente  Se crea archivo 'texto.txt' el 'a' te permite agregar texto al archivo 
    archivo.write(textoDesencriptado)              #Se guarda lo que va a ir escrito en el archivo 
    archivo.close() 

while True:
    respuestaDoE = input("\nPon la letra 'E' para encriptar o pon la letra 'D' para desencriptar: ")
    rutaDeArchivo = input("\nIngresa la ruta de archivo: ")

    if respuestaDoE == 'E' or respuestaDoE == 'e':                            
        encriptarArchivo(rutaDeArchivo)

    elif respuestaDoE == "D" or respuestaDoE == 'd':                          
        desencriptarArchivo(rutaDeArchivo)

    repetir = input("\n¿Quieres volver a encriptar o desencriptar algo? Y/N ") 
    if repetir is not 'Y':
        break