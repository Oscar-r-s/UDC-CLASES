import numpy
import vtkplotlib as vpl
from stl import mesh
from copy import deepcopy
import time
import PyQt6.QtCore

# -----------------------------
# FUNCIONES
# -----------------------------
def pinta_ejes():
    vpl.plot(numpy.array([[0, 0, 0], [3, 0, 0]]), color=(0, 255, 0), line_width=5.0, label="X")
    vpl.plot(numpy.array([[0, 0, 0], [0, 3, 0]]), color=(0, 0, 255), line_width=5.0, label="Y")
    vpl.plot(numpy.array([[0, 0, 0], [0, 0, 3]]), color=(255, 0, 0), line_width=5.0, label="Z")

def rotate_y(angle):
    mat = numpy.identity(4)
    mat[0,0:3] = [numpy.cos(angle), 0.0, numpy.sin(angle)]
    mat[2,0:3] = [-numpy.sin(angle), 0.0, numpy.cos(angle)]
    return mat

def rotate_z(angle):
    mat = numpy.identity(4)
    mat[0:3,0:3] = [
        [numpy.cos(angle), -numpy.sin(angle), 0.0],
        [numpy.sin(angle),  numpy.cos(angle), 0.0],
        [0.0, 0.0, 1.0],
    ]
    return mat

def paint(maquina):
    actores = []
    for pieza in maquina:
        actores.append(vpl.mesh_plot(pieza))
    fig = vpl.gcf()
    fig.update()
    fig.show(block=False)
    time.sleep(0.01)
    for a in actores:
        fig.remove_plot(a)

# -----------------------------
# CARGAR MODELOS
# -----------------------------
base = mesh.Mesh.from_file("Informatica/PRACTICA/Piezas/base.stl")
brazo1 = mesh.Mesh.from_file("Informatica/PRACTICA/Piezas/brazo1.stl")
brazo2 = mesh.Mesh.from_file("Informatica/PRACTICA/Piezas/brazo2.stl")
cinta = mesh.Mesh.from_file("Informatica/PRACTICA/Piezas/cinta.stl")
garra = mesh.Mesh.from_file("Informatica/PRACTICA/Piezas/garra.stl")
lata = mesh.Mesh.from_file("Informatica/PRACTICA/Piezas/lata.stl")

# -----------------------------
# POSICIONAR PIEZAS
# -----------------------------
vpl.QtFigure()
vpl.view(camera_position=(1.2,0.7,1.2), focal_point=(0,0,0))

pinta_ejes()

"""--- POSICIÓN FIJA DE LA CINTA ---"""
vpl.mesh_plot(cinta, color=(0.3, 0.3, 0.6))

# Brazo1
Rz1 = rotate_z(numpy.radians(82.0))
brazo1_copia = deepcopy(brazo1)
brazo1_copia.transform(Rz1)
T = numpy.identity(4)
T[0:3,3] = [0.39,0.0,0.0]

# Brazo2
Rz2 = rotate_z(numpy.radians(-160.0))
brazo2_copia = deepcopy(brazo2)
brazo2_copia.transform(Rz1 @ T @ Rz2)

# Garra
garra_copia = deepcopy(garra)
T_garra = numpy.identity(4)
T_garra[0:3,3] = [0.125,0.01,0.0]
garra_copia.transform(T_garra)

# Lata
lata_copia = deepcopy(lata)
T_lata = numpy.identity(4)
T_lata[0:3, 3] = [0.0, 0.0, 0.5]    
lata_copia.transform(T_lata)

# -----------------------------
# GUARDAR COPIAS ORIGINALES PARA ANIMACIÓN
# -----------------------------
base_orig = deepcopy(base)
b1_orig   = deepcopy(brazo1_copia)
b2_orig   = deepcopy(brazo2_copia)
garra_orig = deepcopy(garra_copia)
cinta_orig = deepcopy(cinta)
lata_orig  = deepcopy(lata_copia)

# -----------------------------
# ANIMACIÓN ROTACIÓN EN Y
# -----------------------------
n_steps = 100
angle_max = numpy.radians(-90.0)
angle_lata = numpy.radians(90.0)  # Rotación final de la lata

# Animar 0 -> 90°
for step in range(n_steps+1):
    ang_max = angle_max * step/n_steps
    Ry = rotate_y(ang_max)

    base_c = deepcopy(base_orig)
    b1_c = deepcopy(b1_orig)
    b2_c = deepcopy(b2_orig)
    garra_c = deepcopy(garra_orig)
    lata_c = deepcopy(lata_orig)

    # Aplicar rotación Y a todo el conjunto menos a la Lata (posición 0 en la cinta)
    base_c.transform(Ry)
    b1_c.transform(Ry)
    b2_c.transform(Ry)
    garra_c.transform(Ry)

    paint([base_c,b1_c,b2_c,garra_c, lata_c])

time.sleep(0.4)

"""--- #Animar Extensión y contracción del brazo --- 
# Suponiendo que Ry es la matriz de 90° en Y ya aplicada a todo el conjunto
# -----------------------------
# Animar extensión y contracción de los brazos
# -----------------------------
n_steps_ext = 50
for step in range(n_steps_ext+1):
    ang_ext = numpy.radians(40.0 * step / n_steps_ext)  # ángulo de extensión

    # Brazo1: posición tras rotar 90° en Y
    brazo1_c = deepcopy(b1_orig)  # usar la copia final tras rotación 90° en Y
    Rz_ext1 = rotate_z(-ang_ext)
    brazo1_c.transform(Rz_ext1)

    # Brazo2: aplicar extensión relativa al brazo1
    brazo2_c = deepcopy(b2_orig)
    T_b2 = numpy.identity(4)
    T_b2[0:3, 3] = [0.39, 0.0, 0.0]  # traslación relativa
    Rz_ext2 = rotate_z(2 * ang_ext)
    brazo2_c.transform(Rz_ext1 @ T_b2 @ Rz_ext2)

    # La garra y la lata permanecen fijas durante la extensión
    paint([base_orig, brazo1_c, brazo2_c, garra_orig, lata_orig, cinta_orig])
 --- """
time.sleep(0.4)

# Animar 90° -> 0°
lata_rot = deepcopy(lata_orig)
for step in range(n_steps+1):
    ang_max = angle_max * (1 - step/n_steps)
    ang_l = angle_lata * step/n_steps
    Ry = rotate_y(ang_max)
    Ry_2 = rotate_y(ang_l)


    base_c = deepcopy(base_orig)
    b1_c = deepcopy(b1_orig)
    b2_c = deepcopy(b2_orig)
    garra_c = deepcopy(garra_orig)
    lata_c = deepcopy(lata_orig)


    base_c.transform(Ry)
    b1_c.transform(Ry)
    b2_c.transform(Ry)
    garra_c.transform(Ry)
    lata_c.transform(Ry_2)
    


    paint([base_c,b1_c,b2_c,garra_c,lata_c])

# Escena final en posición inicial
paint([base_orig,b1_orig,b2_orig,garra_orig])

vpl.show()