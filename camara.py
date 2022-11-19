import cv2 as cv

capturar = cv.VideoCapture(0)
if not capturar.isOpened():
    print("No se encontro camara")
    exit()

while True:
    _, camara = capturar.read()
    cv.imshow("En directo", camara)
    if cv.waitKey(1) == ord("x"):
        break

capturar.relesase()
cv.destroyAllWindows()