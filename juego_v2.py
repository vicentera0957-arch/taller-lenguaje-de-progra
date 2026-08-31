import cv2
import numpy as np
import random

W = 1000
H = 500

personaje = cv2.imread("33670451.png")
personaje = cv2.resize(personaje, (80, 80))

ancho_p = personaje.shape[1]
alto_p = personaje.shape[0]

x, y = 50, 350
speed = 20

lado = 60
meta = 50

tx = random.randint(0, W - lado)
ty = random.randint(0, H - lado)

puntos = 0
vidas = 3

enemigos = [[random.randint(0, W - lado), -lado]]
vel_enemigo = 15


def hay_colision(xA, yA, anchoA, altoA, xB, yB, anchoB, altoB):
    solapan_en_x = (xA < xB + anchoB) and (xB < xA + anchoA)
    solapan_en_y = (yA < yB + altoB) and (yB < yA + altoA)
    return solapan_en_x and solapan_en_y


def pantalla_final(texto, color):
    final = np.full((H, W, 3), 255, dtype=np.uint8)
    cv2.putText(final, texto, (320, 230), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 4)
    cv2.putText(final, "Puntos: " + str(puntos), (400, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    cv2.imshow("Juego v2", final)
    cv2.waitKey(4000)


while True:
    nivel = puntos // 10
    vel_enemigo = 15 + nivel * 3

    while len(enemigos) < 1 + nivel:
        enemigos.append([random.randint(0, W - lado), -random.randint(lado, 500)])

    img = np.full((H, W, 3), 255, dtype=np.uint8)

    img[y:y+alto_p, x:x+ancho_p] = personaje

    cv2.rectangle(img, (tx, ty), (tx+lado, ty+lado), (0, 200, 255), -1)

    for e in enemigos:
        cv2.rectangle(img, (e[0], e[1]), (e[0]+lado, e[1]+lado), (0, 0, 255), -1)

    cv2.putText(img, "Puntos: " + str(puntos) + " / " + str(meta), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    cv2.putText(img, "Vidas: " + str(vidas), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
    cv2.putText(img, "Nivel: " + str(nivel + 1), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

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

    for e in enemigos:
        e[1] = e[1] + vel_enemigo
        if e[1] > H:
            e[0] = random.randint(0, W - lado)
            e[1] = -random.randint(lado, 250)

    if hay_colision(x, y, ancho_p, alto_p, tx, ty, lado, lado):
        puntos = puntos + 1
        tx = random.randint(0, W - lado)
        ty = random.randint(0, H - lado)

    for e in enemigos:
        if hay_colision(x, y, ancho_p, alto_p, e[0], e[1], lado, lado):
            vidas = vidas - 1
            e[0] = random.randint(0, W - lado)
            e[1] = -random.randint(lado, 250)

    if puntos >= meta:
        pantalla_final("Ganaste", (0, 150, 0))
        break

    if vidas <= 0:
        pantalla_final("Fin del juego", (0, 0, 200))
        break

cv2.destroyAllWindows()
