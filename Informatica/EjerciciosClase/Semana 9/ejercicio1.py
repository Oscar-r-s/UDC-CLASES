import numpy as np

#PIDO LAS DIMENSIONES DE LA MATRIZ
def pedirDimensionesMatriz():

    filas = int(input("Número de filas de la matriz (>0):"))
    while filas < 1:
        filas = int(input("Número de filas de la matriz(>0):"))

    columnas = int(input("Numero de columnas de la matriz(>0): "))
    while columnas < 1:    
        columnas = int(input("Numero de columnas de la matriz(>0): "))

    return filas,columnas


#Pido los elementos de la matriz
def pedirElementosMatriz(matriz):
    #Obtengo las dimensiones de la matriz que se me ha pasado
    dimensiones_matriz = matriz.shape

    #Declaro el número de filas y columnas
    filas = dimensiones_matriz[0]
    columnas = dimensiones_matriz[1]

    #Pido un valor para cada elemento de la matriz
    for i in range(filas):
        for j in range(columnas):
            elemento = int(input(f"Introduce un valor para matriz[{i},{j}]: "))
            matriz[i,j] = elemento

def imprimirMatriz(mx):
    for row in mx:
        print(row)

def main():
    #DECLARO UNA MATRIZ CON LAS DIMENSIONES PEDIDAS
    rows, columns = pedirDimensionesMatriz()
    matrix = np.empty((rows,columns), dtype=np.int64)

    pedirElementosMatriz(matrix)

    print("Matriz Original")
    print(matrix)

    print("---Triangular Superior---")
    triangular_superior = np.triu(matrix)
    imprimirMatriz(triangular_superior)

    print("---Triangular Inferior---")
    triangular_inferior = np.tril(matrix)
    imprimirMatriz(triangular_inferior)


if __name__ == "__main__":
    main()



