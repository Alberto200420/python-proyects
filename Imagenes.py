#PROGRAMA PARA HACER QUE LAS IMAGENES PESEN MENOS 
from PIL import Image
imagen = Image.open('paisajes.jpg')       #----- ABRIENDO IMAGEN
imagen = imagen.convert('RGB')            #----- comvirtiendolo 
imagen.save('NEW.jpg', quality=30)        #----- Guardando en nuevo archivo 
print('Imagen combertida')