# Taller lenguaje de programación

Juego en OpenCV que aplica la función `hay_colision` de la teoría de colisiones en 2D.

## Instalar

Desde la carpeta del repo:

**Windows**

```
py -m pip install -r requirements.txt
```

**macOS / Linux**

```
python3 -m pip install -r requirements.txt
```

## Ejecutar

Importante: hay que ejecutarlo **parado dentro de la carpeta del repo**, porque el juego carga `personaje.png` con ruta relativa.

**Windows**

```
cd ruta\a\taller-lenguaje-de-progra
py juego_v2.py
```

**macOS / Linux**

```
cd ruta/a/taller-lenguaje-de-progra
python3 juego_v2.py
```

En VS Code basta con abrir la carpeta del repo (File > Open Folder) y darle Run.

## Cómo se juega

| Tecla | Acción |
|-------|--------|
| `W` | arriba |
| `A` | izquierda |
| `S` | abajo |
| `D` | derecha |
| `Q` | salir |

- Cuadrado **amarillo**: tesoro, suma un punto y reaparece en otro lugar.
- Cuadrado **rojo**: enemigo, cae desde arriba y resta una vida.
- Se gana llegando a **50 puntos**. Con 3 vidas perdidas se termina la partida.

Las teclas se leen sobre la ventana del juego, no sobre la terminal: hay que hacer clic en la ventana primero.

## Dificultad

Cada 10 puntos se sube de nivel: cae un enemigo más y todos bajan más rápido.

| Nivel | Puntos | Enemigos | Velocidad |
|-------|--------|----------|-----------|
| 1 | 0 - 9 | 1 | 15 |
| 2 | 10 - 19 | 2 | 18 |
| 3 | 20 - 29 | 3 | 21 |
| 4 | 30 - 39 | 4 | 24 |
| 5 | 40 - 49 | 5 | 27 |

Para cambiar el balance se tocan estas dos líneas de `juego_v2.py`:

```python
vel_enemigo = 15 + nivel * 3
while len(enemigos) < 1 + nivel:
```

Y `vidas = 3` cerca del inicio si se quiere más margen.

## Si algo falla

**`The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Cocoa support`**

Está instalado `opencv-python-headless`, que no abre ventanas. Se arregla así:

```
py -m pip uninstall opencv-python-headless
py -m pip install opencv-python
```

**`(-215:Assertion failed) !ssize.empty() in function 'resize'`**

No encontró `personaje.png`, o sea que la terminal no está parada en la carpeta del repo. Revisar con `cd` que estés dentro de `taller-lenguaje-de-progra`.

**`ModuleNotFoundError: No module named 'cv2'`**

Falta instalar las dependencias, o estás usando un intérprete de Python distinto al que las instaló. En VS Code se cambia con Ctrl+Shift+P > "Python: Select Interpreter".
