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

# ROTACIÓN EN EL EJE Y
def rotate_y(angle):
    matrix = numpy.identity(4)
    matrix[0, 0:3] = [numpy.cos(angle), 0.0, numpy.sin(angle)]
    matrix[2, 0:3] = [-numpy.sin(angle), 0.0, numpy.cos(angle)]
    return matrix

#ROTACIÓN EN EL EJE Z
def rotate_z(angle):
    matrix = numpy.identity(4)
    matrix[0:3, 0:3] = [
    [numpy.cos(angle), -numpy.sin(angle), 0.0],
    [numpy.sin(angle), numpy.cos(angle), 0.0],
    [0.0, 0.0, 1.0],
    ]
    return matrix


#CARGO MIS MODELOS
base = mesh.Mesh.from_file("Informatica/PRACTICA/Piezas/base.stl")
brazo1 = mesh.Mesh.from_file("Informatica/PRACTICA/Piezas/brazo1.stl")
brazo2 = mesh.Mesh.from_file("Informatica/PRACTICA/Piezas/brazo2.stl")
cinta = mesh.Mesh.from_file("Informatica/PRACTICA/Piezas/cinta.stl")
garra = mesh.Mesh.from_file("Informatica/PRACTICA/Piezas/garra.stl")
lata = mesh.Mesh.from_file("Informatica/PRACTICA/Piezas/lata.stl")


#Ventana de visualización y posción de cámara
vpl.QtFigure()
vpl.gcf().vl.setContentsMargins(0, 0, 0, 0)
vpl.view(camera_position=(1.2, 0.7, 1.2), focal_point=(0.0, 0.0, 0.0))

pinta_ejes()

""" --- POSICIÓN Y ROTACIÓN DEL BRAZO 1 ---"""
Rz1 = rotate_z(numpy.radians(82.0))
brazo1_copia = deepcopy(brazo1)
brazo1_copia.transform(Rz1)
T = numpy.identity(4)
T[0:3, 3] = [0.39, 0.0, 0.0]

""" --- POSICIÓN Y ROTACIÓN DEL BRAZO 2 ---"""
Rz2 = rotate_z(numpy.radians(-160.0))
brazo2_copia = deepcopy(brazo2)
brazo2_copia.transform(Rz1 @ T @ Rz2)

""" --- POSICIÓN DE LA GARRA ---"""
Rz3 = rotate_z(numpy.radians(0)) #Elimino ?
garra_copia = deepcopy(garra)
T_garra = numpy.identity(4)
T_garra[0:3, 3] = [0.125, 0.01, 0.0]    #[0.125(x)  , 0.01(y), 0.0(z)] Fui probando valores hasta que los agujeron encajaron
# Traslación extra hacia el extremo del brazo2 
garra_copia.transform(T_garra)

""" --- POSICIÓN DE LA LATA ---"""
lata_copia = deepcopy(lata)
T_lata = numpy.identity(4)
T_lata[0:3, 3] = [0.0, 0.0, 0.5]    #[0.125(x)  , 0.01(y), 0.0(z)] Fui probando valores hasta que los agujeron encajaron
lata_copia.transform(T_lata)


#Dibujar los modelos en su posición inicial
vpl.mesh_plot(base, color=(0.59, 0.43, 0.59))
vpl.mesh_plot(brazo1_copia, color=(0.59, 0.43, 0.59))
vpl.mesh_plot(brazo2_copia, color=(0.59, 0.63, 0.47))
vpl.mesh_plot(garra_copia, color=(0, 0.5, 1))
vpl.mesh_plot(cinta, color=(0.3, 0.3, 0.6))
vpl.mesh_plot(lata_copia, color=(0.9, 0.2, 0.2))

vpl.show()

