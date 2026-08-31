import cv2
import numpy as np
import random

W = 1000
H = 500

personaje = cv2.imread("personaje.png")
personaje = cv2.resize(personaje, (80, 80))

ancho_p = personaje.shape[1]
alto_p = personaje.shape[0]

x, y = 50, 350
speed = 20

lado = 60

tx = random.randint(0, W - lado)
ty = random.randint(0, H - lado)

ex = random.randint(0, W - lado)
ey = -lado
vel_enemigo = 15

puntos = 0
vidas = 3


def hay_colision(xA, yA, anchoA, altoA, xB, yB, anchoB, altoB):
    solapan_en_x = (xA < xB + anchoB) and (xB < xA + anchoA)
    solapan_en_y = (yA < yB + altoB) and (yB < yA + altoA)
    return solapan_en_x and solapan_en_y


while True:
    img = np.full((H, W, 3), 255, dtype=np.uint8)

    img[y:y+alto_p, x:x+ancho_p] = personaje

    cv2.rectangle(img, (tx, ty), (tx+lado, ty+lado), (0, 200, 255), -1)
    cv2.rectangle(img, (ex, ey), (ex+lado, ey+lado), (0, 0, 255), -1)

    cv2.putText(img, "Puntos: " + str(puntos), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    cv2.putText(img, "Vidas: " + str(vidas), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

    cv2.imshow("Juego v2", img)

    tecla = cv2.waitKey(100) & 0xFF

    if tecla == ord("q"):
        break
    elif tecla == ord("d"):
        x = x + speed
    elif tecla == ord("a"):
        x = x - speed
    elif tecla == ord("w"):
        y = y - speed
    elif tecla == ord("s"):
        y = y + speed

    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x > W - ancho_p:
        x = W - ancho_p
    if y > H - alto_p:
        y = H - alto_p

    ey = ey + vel_enemigo
    if ey > H:
        ey = -lado
        ex = random.randint(0, W - lado)

    if hay_colision(x, y, ancho_p, alto_p, tx, ty, lado, lado):
        puntos = puntos + 1
        tx = random.randint(0, W - lado)
        ty = random.randint(0, H - lado)

    if hay_colision(x, y, ancho_p, alto_p, ex, ey, lado, lado):
        vidas = vidas - 1
        ex = random.randint(0, W - lado)
        ey = -lado

    if vidas == 0:
        final = np.full((H, W, 3), 255, dtype=np.uint8)
        cv2.putText(final, "Fin del juego", (330, 230), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)
        cv2.putText(final, "Puntos: " + str(puntos), (400, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow("Juego v2", final)
        cv2.waitKey(3000)
        break

cv2.destroyAllWindows()
