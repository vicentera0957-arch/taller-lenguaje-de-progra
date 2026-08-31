import cv2
import numpy as np

W = 1000
H = 500


personaje = cv2.imread("personaje.png")
personaje = cv2.resize(personaje, (100,100))

# Inicio personaje
x,y = 50,350
speed = 25

tesoro = cv2.imread("tesoro.jpg")
tesoro = cv2.resize(tesoro, (100,100))

# Inicio tesoro
tx, ty = 600, 250

while True:
    img = np.full((H, W, 3), 255, dtype=np.uint8)
    print("teoria")
    # Personaje a la imagen
    img[y:y+personaje.shape[0], x:x+personaje.shape[1]] = personaje
    
    img[ty:ty+tesoro.shape[0], tx:tx+tesoro.shape[1]] = tesoro
    
    cv2.circle(img, (x+personaje.shape[1], y), 2, (0,0,255), 2)
    cv2.imshow("Juevo v1", img)

    if (cv2.waitKey(500) & 0xFF) == ord("q"):
        break
    elif (cv2.waitKey(500) & 0xFF) == ord("d"):
        x = x + speed
    elif (cv2.waitKey(500) & 0xFF) == ord("a"):
        x = x - speed
    elif (cv2.waitKey(500) & 0xFF) == ord("w"):
        y = y - speed
    elif (cv2.waitKey(500) & 0xFF) == ord("s"):
        y = y + speed
       
    c1 = y, x
    c2 = y, x + personaje.shape[1]
    c3 = y + personaje.shape[0], x
    c4 = y + personaje.shape[0], x + personaje.shape[1]
    
    if ((c4[0] > ty and c4[0] < ty + tesoro.shape[0]) or (c2[0] > ty and c2[0] < ty + tesoro.shape[0])) and ((c1[1] > tx and c1[1] < tx + tesoro.shape[1]) or (c3[1] > tx and c3[1] < tx + tesoro.shape[1])):
        print("Colision")