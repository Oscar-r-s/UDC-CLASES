# =============================
# IMPORTS
# =============================
import time
from copy import deepcopy

import numpy as np
import vtkplotlib as vpl
from stl import mesh
import PyQt6.QtCore

"""
NOTA PARA EL PROFESOR :
Dentro de la función cargar_modelo el segundo argumento recibe un valor predeterminado porque esa
es la ubcación donde yo he guardado los archivos STL, pero para poder observar el programa funcionando
correctamente es necesario que se cambie por la ubicación donde se tengas los archivos STL dependiendo
de la persona que quiera ejecutar el programa.
"""

# =============================
# DEFINO LAS FUNCIONES DE ROTACION, DE PINTAR EJES, Y DE PINTAR LAS PIEZAS
# =============================

def rot_x(angle: float) -> np.ndarray:
    m = np.identity(4)
    c, s = np.cos(angle), np.sin(angle)
    m[1, 1], m[1, 2] = c, -s
    m[2, 1], m[2, 2] = s, c
    return m

def rot_y(angle: float) -> np.ndarray:
    m = np.identity(4)
    c, s = np.cos(angle), np.sin(angle)
    m[0, 0], m[0, 2] = c, s
    m[2, 0], m[2, 2] = -s, c
    return m

def rot_z(angle: float) -> np.ndarray:
    c, s = np.cos(angle), np.sin(angle)
    m = np.identity(4)
    m[0:3, 0:3] = [[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]]
    return m

def translate(dx=0.0, dy=0.0, dz=0.0) -> np.ndarray:
    m = np.identity(4)
    m[0:3, 3] = [dx, dy, dz]
    return m

def pintar_ejes():
    vpl.plot(np.array([[0, 0, 0], [3, 0, 0]]), color=(0, 255, 0), line_width=5, label="X")
    vpl.plot(np.array([[0, 0, 0], [0, 3, 0]]), color=(0, 0, 255), line_width=5, label="Y")
    vpl.plot(np.array([[0, 0, 0], [0, 0, 3]]), color=(255, 0, 0), line_width=5, label="Z")

Colores_Piezas = [
    (20, 70, 90),      # base
    (90, 200, 200),   # brazo 1
    (235, 220, 200),  # brazo 2
    (50, 60, 70),     # garra
    (230, 120, 110),  # lata
]

def paint(parts):
    actors = [vpl.mesh_plot(p, color=c) for p, c in zip(parts, Colores_Piezas)]
    fig = vpl.gcf()
    fig.update()
    fig.show(block=False)
    time.sleep(0.01)
    for a in actors:
        fig.remove_plot(a)

# =============================
# CARGA DE MODELOS
# =============================
def cargar_modelo(*nombres_pieza, path="Informatica/PRACTICA/Piezas/"):
    return tuple(mesh.Mesh.from_file(path + nombre) for nombre in nombres_pieza)

# =============================
# PUESTA EN ESCENA
# =============================
def puesta_en_escena():
    vpl.QtFigure()
    fig = vpl.gcf()
    fig.setWindowState(PyQt6.QtCore.Qt.WindowState.WindowMaximized)
    fig.vl.setContentsMargins(0, 0, 0, 0)
    vpl.view(camera_position=(2.4, 1.4, 2.4), focal_point=(0, 0, 0))

    pintar_ejes()

    # Cinta fija
    cinta_fix = deepcopy(cinta)
    cinta_fix.transform(translate(0, -0.018, 0.2))
    vpl.mesh_plot(cinta_fix, color=(128, 128, 128))

# =============================
# ANIMACIÓN ROTACIÓN 0º -> 90º
# =============================
def ida():
    for i in range(steps + 1):
            a = ang_max * i / steps
            Ry = rot_y(a)

            parts = []
            for p in (base_0, b1_0, b2_0, garra_0):
                q = deepcopy(p)
                q.transform(Ry)
                parts.append(q)

            lata_c = deepcopy(lata_0)
            lata_c.transform(translate(0.0, -0.007, 0.0))
            parts.append(lata_c)

            paint(parts)

    time.sleep(0.4)
    
# =============================
# EXTENSIÓN Y CONTRACCIÓN
# =============================
def extender_y_contraer():
    Rx = rot_y(np.radians(-90.0))
    T_end = translate(0.39, 0, 0)
    R_garra_ini = rot_z(np.radians(80.0))
    delta_garra = np.radians(-45.0)

    for reverse in (False, True):
        if(not reverse): 
            iterable = range(steps)
        else:
            iterable = reversed(range(steps))

        for step in iterable:
            ang = step * 40.0 / steps
            Rg = rot_z(delta_garra * step / steps)

            Rz1 = rot_z(np.radians(82.0 - ang))
            Rz2 = rot_z(np.radians(-160.0 + 2.0 * ang))

            M1 = Rz1
            M2 = T_end @ Rz2

            base_ext = deepcopy(base)
            base_ext.transform(Rx)


            b1_c = deepcopy(brazo1)
            b1_c.transform(Rx @ M1)

            b2_c = deepcopy(brazo2)
            b2_c.transform(Rx @ M1 @ M2)

            g_c = deepcopy(garra)
            g_c.transform(Rx @ M1 @ M2 @ T_end @ R_garra_ini @ Rg)

            l_c = deepcopy(lata_inicio)
            if reverse:
                T_lata_offset = np.identity(4)
                T_lata_offset[0:3, 3] = [0.20, -0.0125, -0.655]

                l_c.transform(T_lata_offset)

                l_c.transform(
                    Rx
                    @ M1
                    @ M2
                    @ T_end
                    @ R_garra_ini
                    @ Rg
                )

            paint([base_ext, b1_c, b2_c, g_c, l_c])

    time.sleep(0.4)

# =============================
# ANIMACIÓN ROTACIÓN 90º -> 0º
# =============================
def vuelta():
    ang_lata = np.radians(90.0)

    for i in range(steps + 1):
        a = ang_max * (1 - i / steps)
        al = ang_lata * i / steps

        Ry = rot_y(a)
        Ry_l = rot_y(al)

        parts = []
        for p in (base_0, b1_0, b2_0, garra_0):
            q = deepcopy(p)
            q.transform(Ry)
            parts.append(q)

        lata_c = deepcopy(lata_0)
        lata_c.transform(Ry_l @ translate(0.0, -0.0055, -0.458))
        parts.append(lata_c)

        paint(parts)

# =============================
# ESCENA FINAL ESTÁTICA
# =============================
def escena_final():
    # Escena final
    R_final = rot_y(np.radians(90))
    for p in (b1_inicio, b2_inicio, garra_inicio, lata_inicio):
        p.transform(R_final)

    vpl.mesh_plot(base_0, color=Colores_Piezas[0])
    vpl.mesh_plot(b1_0, color=Colores_Piezas[1])
    vpl.mesh_plot(b2_0, color=Colores_Piezas[2])
    vpl.mesh_plot(garra_0, color=Colores_Piezas[3])
    #-------------------------------------------------
    #Corregir la posición final de la lata
    #-------------------------------------------------
    lata_inicio.transform(translate(-0.456, 0.0, 0.0))
    vpl.mesh_plot(lata_inicio, color=Colores_Piezas[4])
    vpl.show()

# =============================
# CARGA DE MODELOS STL Y POSICIONES INICIALES DE LAS PIEZAS
# =============================
base, brazo1, brazo2, cinta, garra, lata = cargar_modelo("base.stl","brazo1.stl","brazo2.stl","cinta.stl","garra.stl","lata.stl")

b1_inicio = deepcopy(brazo1)
b1_inicio.transform(rot_z(np.radians(82.0)))

b2_inicio = deepcopy(brazo2)
b2_inicio.transform(rot_z(np.radians(82.0)) @ translate(0.39, 0, 0) @ rot_z(np.radians(-160.0)))

garra_inicio = deepcopy(garra)
garra_inicio.transform(translate(0.125, 0.01, 0.0))

lata_inicio = deepcopy(lata)
lata_inicio.transform(translate(-0.065, 0.0, 0.72))

# Copias base para animación
base_0 = deepcopy(base)
b1_0 = deepcopy(b1_inicio)
b2_0 = deepcopy(b2_inicio)
garra_0 = deepcopy(garra_inicio)
lata_0 = deepcopy(lata_inicio)

# =============================
# CONSTANTES COMUNES A TODAS LAS FUNCONES
# =============================
steps = 100
ang_max = np.radians(-90.0)

def main():
    puesta_en_escena()
    ida()
    extender_y_contraer()
    vuelta()
    escena_final()

if __name__ == "__main__":
    main()
