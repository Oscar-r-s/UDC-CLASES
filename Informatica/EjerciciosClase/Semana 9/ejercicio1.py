import numpy as np

#PIDO LAS DIMENSIONES DE LA MATRIZ
filas = int(input("Número de filas de la matriz (>0):"))
while filas < 1:
    filas = int(input("Número de filas de la matriz(>0):"))

columnas = int(input("Numero de columnas de la matriz(>0): "))
while columnas < 1:    
    columnas = int(input("Numero de columnas de la matriz(>0): "))


#DECLARO UNA MATRIZ CON LAS DIMENSIONES PEDIDAS
matriz = np.empty((filas,columnas), dtype=np.int64)

#Pido los elementos de la matriz
for i in range(filas):
    for j in range(columnas):
        elemento = int(input(f"Introduce un valor para matriz[{i},{j}]: "))
        matriz[i,j] = elemento

print("Matriz Original")
print(matriz)

print("---Triangular Superior---")
print(np.triu(matriz))

print("---Triangular Inferior---")
print(np.tril(matriz))

