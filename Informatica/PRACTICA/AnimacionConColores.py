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

def rotate_x(angle):
    mat = numpy.identity(4)
    mat[1, 1] = numpy.cos(angle)
    mat[1, 2] = -numpy.sin(angle)
    mat[2, 1] = numpy.sin(angle)
    mat[2, 2] = numpy.cos(angle)
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
    # -----------------------------
    # DEFINO LOS COLORES DE LAS PIEZAS
    colores_piezas_diccionario = {
        "COLOR_base" : [20, 70, 90],
        "COLOR_brazo_1" : [90, 200, 200],
        "COLOR_brazo_2" : [235, 220, 200],
        "COLOR_garra" : [50, 60, 70],
        "COLOR_lata" : [230, 120, 110]
    }

    colores_piezas_lista_de_tuplas = []

    for rgb in colores_piezas_diccionario.values():
        rgb_tuple = tuple(rgb)
        colores_piezas_lista_de_tuplas.append(rgb_tuple)
    # -----------------------------
    actores = []
    contador_color_lista_tuplas = 0
    for pieza in maquina:
        actores.append(vpl.mesh_plot(pieza, color = colores_piezas_lista_de_tuplas[contador_color_lista_tuplas]))
        contador_color_lista_tuplas += 1
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
vpl.gcf().setWindowState(PyQt6.QtCore.Qt.WindowState.WindowMaximized)
vpl.gcf().vl.setContentsMargins(0, 0, 0, 0)
vpl.view(camera_position=(2.4, 1.4, 2.4), focal_point=(0.0, 0.0, 0.0))

pinta_ejes()

"""--- POSICIÓN FIJA DE LA CINTA ---"""
# Copia de la cinta para no modificar el original
cinta_copia = deepcopy(cinta)
"""--- FIN POSICIÓN FIJA DE LA CINTA ---"""

# Crear matriz de traslación
T_cinta = numpy.identity(4)
T_cinta[0:3, 3] = [0, -0.018, 0.2]  # cambiar dx, dy, dz según el eje que quieras mover

# Aplicar la traslación
cinta_copia.transform(T_cinta)

# Dibujar la cinta en su nueva posición
vpl.mesh_plot(cinta_copia, color=(0.3, 0.3, 0.6))

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
T_lata[0:3, 3] = [-0.065, 0.0, 0.72] #Posicion de la lata para que coincida con la garra
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

    #Desplazamiento de la lata respecto al extremo de la garra
    T_lata_offset = numpy.identity(4)
    T_lata_offset[0:3, 3] = [0.0, -0.007, 0.0]

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

    lata_c.transform(T_lata_offset)

    paint([base_c,b1_c,b2_c,garra_c, lata_c])

time.sleep(0.4)

""" --- EXTENSIÓN --- """

Rx = rotate_y(numpy.radians(-90.0))  # rotación global
Ry = numpy.identity(4)
Rz = numpy.identity(4)
n_steps = 100

# La base permanece rotada a 90º
R_base = rotate_y(ang_max)
base_copia = deepcopy(base)
base.transform(R_base)

# Traslación y rotación inicial de la garra
T_garra_local = numpy.identity(4)
T_garra_local[0:3, 3] = [0.39, 0.0, 0.0]  # posición al final del brazo2
R_garra_inicial = rotate_z(numpy.radians(80.0))  # inclinación inicial +45°


# Ángulo total que la garra debe rotar negativamente
delta_garra = numpy.radians(-45.0)

for step in range(n_steps):
    ang = step * 40.0 / n_steps
    garra_step_angle = (delta_garra * (step / n_steps) ) # rotación progresiva de la garra + Número por correccion
    R_garra_anim = rotate_z(garra_step_angle)

    # Brazo1
    brazo1_copia = deepcopy(brazo1)
    T1 = numpy.identity(4)
    Rz1 = rotate_z(numpy.radians(82.0 - ang))
    Mt_brazo1 = T1 @ Rz1 @ Ry @ numpy.identity(4)
    brazo1_copia.transform(Rx @ Mt_brazo1)

    # Brazo2
    brazo2_copia = deepcopy(brazo2)
    T2 = numpy.identity(4)
    T2[0:3, 3] = [0.39, 0.0, 0.0]
    Rz2 = rotate_z(numpy.radians(-160.0 + 2.0 * ang))
    Mt_brazo2 = T2 @ Rz2 @ Ry @ numpy.identity(4)
    brazo2_copia.transform(Rx @ Mt_brazo1 @ Mt_brazo2)

    # Garra: traslación al extremo del brazo2 + rotación inicial + rotación progresiva
    garra_copia = deepcopy(garra)
    garra_copia.transform(Rx @ Mt_brazo1 @ Mt_brazo2 @ T_garra_local @ R_garra_inicial @ R_garra_anim)


    paint([base, brazo1_copia, brazo2_copia, garra_copia, lata_copia])


""" --- FIN DE LA EXTENSIÓN --- """

""" ---  CONTRACCIÓN DEL BRAZO --- """
for step in reversed(range(n_steps)):
    ang = step * 40.0 / n_steps
    garra_step_angle = (delta_garra * (step / n_steps))
    R_garra_anim = rotate_z(garra_step_angle)

    #Desplazamiento de la lata respecto al extremo de la garra
    T_lata_offset = numpy.identity(4)
    T_lata_offset[0:3, 3] = [0.13, -0.02, 0.065]

    brazo1_copia = deepcopy(brazo1)
    T1 = numpy.identity(4)
    Rz1 = rotate_z(numpy.radians(82.0 - ang))
    Mt_brazo1 = T1 @ Rz1 @ Ry @ numpy.identity(4)
    brazo1_copia.transform(Rx @ Mt_brazo1)

    brazo2_copia = deepcopy(brazo2)
    T2 = numpy.identity(4)
    T2[0:3, 3] = [0.39, 0.0, 0.0]
    Rz2 = rotate_z(numpy.radians(-160.0 + 2.0 * ang))
    Mt_brazo2 = T2 @ Rz2 @ Ry @ numpy.identity(4)
    brazo2_copia.transform(Rx @ Mt_brazo1 @ Mt_brazo2)

    garra_copia = deepcopy(garra)
    garra_copia.transform(Rx @ Mt_brazo1 @ Mt_brazo2 @ T_garra_local @ R_garra_inicial @ R_garra_anim)

    lata_copia = deepcopy(lata)
    lata_copia.transform(Rx @ Mt_brazo1 @ Mt_brazo2 @ T_garra_local @ R_garra_inicial @ R_garra_anim @ T_lata_offset)

    paint([base, brazo1_copia, brazo2_copia, garra_copia, lata_copia])

"""--- FIN DE LA CONTRACCIÓN DEL BRAZO ---"""

time.sleep(0.4)

# Animar 90° -> 0°
lata_rot = deepcopy(lata_orig)
for step in range(n_steps+1):
    ang_max = angle_max * (1 - step/n_steps)
    ang_l = angle_lata * step/n_steps
    Ry = rotate_y(ang_max)
    Ry_2 = rotate_y(ang_l)

    #Desplazamiento de la lata respecto al extremo de la garra
    T_lata_offset = numpy.identity(4)
    T_lata_offset[0:3, 3] = [0.0, -0.0055, -0.458]

    base_c = deepcopy(base_orig)
    b1_c = deepcopy(b1_orig)
    b2_c = deepcopy(b2_orig)
    garra_c = deepcopy(garra_orig)
    lata_c = deepcopy(lata_orig)


    base_c.transform(Ry)
    b1_c.transform(Ry)
    b2_c.transform(Ry)
    garra_c.transform(Ry)
    lata_c.transform(Ry_2 @ T_lata_offset)

    
    paint([base_c,b1_c,b2_c,garra_c,lata_c])

# Escena final en posición inicial
R_final = rotate_y(numpy.radians(90))

brazo1_copia.transform(R_final)
brazo2_copia.transform(R_final)
garra_copia.transform(R_final)
lata_copia.transform(R_final)

#Posición final de las piezas
vpl.mesh_plot(base_copia, color=(20, 70, 90))
vpl.mesh_plot(brazo1_copia, color=(90, 200, 200))
vpl.mesh_plot(brazo2_copia, color=(235, 220, 200))
vpl.mesh_plot(garra_copia, color=(50, 60, 70))
vpl.mesh_plot(lata_copia, color=(230, 120, 110))
vpl.show()