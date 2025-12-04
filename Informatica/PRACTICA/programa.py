import numpy
# Para mostrar la escena.
import vtkplotlib as vpl
# Para cargar los modelos 3D.
from stl import mesh
# Rotación en Y
from copy import deepcopy
#PyQt6
import PyQt6.QtCore


def pinta_ejes():
    vpl.plot(numpy.array([[0, 0, 0], [3, 0, 0]]), color=(0, 255, 0), line_width=5.0, label="X")
    vpl.plot(numpy.array([[0, 0, 0], [0, 3, 0]]), color=(0, 0, 255), line_width=5.0, label="Y")
    vpl.plot(numpy.array([[0, 0, 0], [0, 0, 3]]), color=(255, 0, 0), line_width=5.0, label="Z")

# Creamos la ventana de visualización.
vpl.QtFigure()

"""
------------------------ CARGAR UN MODELO ------------------------
"""

"""
# Cargamos un modelo.
modelo = mesh.Mesh.from_file("Informatica/PRACTICA/Piezas/base.stl")

# Lo añadimos a la ventana.
vpl.mesh_plot(modelo)

# Pintamos los ejes (solo para ayudar a visualizar)
pinta_ejes()

# Ponemos la cámara donde nos interesa.
vpl.gcf().vl.setContentsMargins(0, 0, 0, 0)
vpl.view(camera_position=(0.6, 0.35, 0.6), focal_point=(0.0, 0.0, 0.0))

# Visualizamos la ventana (la figura se borra al cerrarla).
vpl.show()
"""

"""
------------------------ ROTACION EN Y ------------------------

"""
def rotate_y(angle):
    matrix = numpy.identity(4)
    matrix[0, 0:3] = [numpy.cos(angle), 0.0, numpy.sin(angle)]
    matrix[2, 0:3] = [-numpy.sin(angle), 0.0, numpy.cos(angle)]
    return matrix

"""
def rotate_y(angle):
    matrix = numpy.identity(4)
    matrix[0, 0:3] = [numpy.cos(angle), 0.0, numpy.sin(angle)]
    matrix[2, 0:3] = [-numpy.sin(angle), 0.0, numpy.cos(angle)]
    return matrix
vpl.QtFigure()
vpl.gcf().vl.setContentsMargins(0, 0, 0, 0)
vpl.view(camera_position=(0.6, 0.35, 0.6), focal_point=(0.0, 0.0, 0.0))
pinta_ejes()
# Calculamos la matriz de transformación para rotar la pieza 45º en Y.
Rx = numpy.identity(4)
Ry = rotate_y(numpy.radians(45))
Rz = numpy.identity(4)
T = numpy.identity(4)
Mt = T @ Rz @ Ry @ Rx
# Copiamos el modelo para no modificar sus coordenadas originales.
copia = deepcopy(modelo)
# Aplicamos la matriz de transformación.
copia.transform(Mt)
vpl.mesh_plot(copia)
vpl.show()
"""

"""
------------------------ CARGAR VARIOS MODELOS ------------------------
"""

#vpl.QtFigure()
#vpl.gcf().vl.setContentsMargins(0, 0, 0, 0)
#vpl.view(camera_position=(1.2, 0.7, 1.2), focal_point=(0.0, 0.0, 0.0))
#pinta_ejes()
base = mesh.Mesh.from_file("Informatica/PRACTICA/Piezas/base.stl")
brazo1 = mesh.Mesh.from_file("Informatica/PRACTICA/Piezas/brazo1.stl")
brazo2 = mesh.Mesh.from_file("Informatica/PRACTICA/Piezas/brazo2.stl") 
# Esta vez, ponemos colores a las piezas para distinguirlas mejor.
""" vpl.mesh_plot(base, color=(0.59, 0.43, 0.59))
vpl.mesh_plot(brazo1, color=(0.59, 0.43, 0.59))
vpl.mesh_plot(brazo2, color=(0.59, 0.63, 0.47)) """
#vpl.show()

"""
------------------------ ENSAMBLAR MODELOS ------------------------
"""

def rotate_z(angle):
    matrix = numpy.identity(4)
    matrix[0:3, 0:3] = [
    [numpy.cos(angle), -numpy.sin(angle), 0.0],
    [numpy.sin(angle), numpy.cos(angle), 0.0],
    [0.0, 0.0, 1.0],
    ]
    return matrix

""" vpl.QtFigure()
vpl.gcf().vl.setContentsMargins(0, 0, 0, 0)
vpl.view(camera_position=(1.2, 0.7, 1.2), focal_point=(0.0, 0.0, 0.0))
pinta_ejes()
Rz1 = rotate_z(numpy.radians(82.0))
brazo1_copia = deepcopy(brazo1)
brazo1_copia.transform(Rz1)
T = numpy.identity(4)
T[0:3, 3] = [0.39, 0.0, 0.0]
Rz2 = rotate_z(numpy.radians(-160.0))
brazo2_copia = deepcopy(brazo2)
brazo2_copia.transform(Rz1 @ T @ Rz2)
vpl.mesh_plot(base, color=(0.59, 0.43, 0.59))
vpl.mesh_plot(brazo1_copia, color=(0.59, 0.43, 0.59))
vpl.mesh_plot(brazo2_copia, color=(0.59, 0.63, 0.47))
vpl.show() """

"""
ANIMACIÓN
"""

def paint(maquina):
    lista = []
    for pieza in maquina:
        lista.append(vpl.mesh_plot(pieza))
    figure = vpl.gcf()
    figure.update()
    figure.show(block=False)
    for pieza in lista:
        figure.remove_plot(pieza)

vpl.QtFigure()
vpl.gcf().setWindowState(PyQt6.QtCore.Qt.WindowState.WindowMaximized)
vpl.gcf().vl.setContentsMargins(0, 0, 0, 0)
vpl.view(camera_position=(2.4, 1.4, 2.4), focal_point=(0.0, 0.0, 0.0))
pinta_ejes()
Rx = numpy.identity(4)
Ry = numpy.identity(4)
Rz = numpy.identity(4)
n_steps = 100

for step in range(n_steps):
    ang = step * 40.0 / n_steps
    # Movemos el brazo1
    brazo1_copia = deepcopy(brazo1)
    T = numpy.identity(4)
    Rz = rotate_z(numpy.radians(82.0 - ang))
    Mt_brazo1 = T @ Rz @ Ry @ Rx
    brazo1_copia.transform(Mt_brazo1)
    # Movemos el brazo2
    brazo2_copia = deepcopy(brazo2)
    T = numpy.identity(4)
    T[0:3, 3] = [0.39, 0.0, 0.0]
    Rz = rotate_z(numpy.radians(-160.0 + 2.0 * ang))
    Mt_brazo2 = T @ Rz @ Ry @ Rx
    brazo2_copia.transform(Mt_brazo1 @ Mt_brazo2)
    paint([base, brazo1_copia, brazo2_copia])


