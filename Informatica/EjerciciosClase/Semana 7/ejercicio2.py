"""
El programa debe hacer lo siguiente: 

▪Lea por teclado un número entero positivo (n) menor que 30. Este número representará la dimensión de los vectores. 
▪Lea por teclado n números reales y almacénelo en una lista. Estos números representarán los elementos del primer vector. 
▪Lea por teclado n números reales y almacénelo en otra lista. Estos números representarán los elementos del segundo vector. 
▪Muestre por pantalla el resultado del producto escalar de los dos vectores con dos decimales.

"""

v1 = []
v2 = []

def pedirVectores ():

    dimension = int(input("Introduce la dimensión de los vectores (MAX 30) : "))

    while dimension < 1 or dimension >= 30 :
        dimension = int(input("Error, número incorrecto, vuelve a intentarlo : "))

    #Pedir primer y segundo vector en un String, por ejemplo : "1 2 3 4" y "5 6 7 8"
    print("Primer Vector")
    vector_1_STR = input("Introduce las componentes del vector 1 separadas por espacios : ")

    print("Segundo Vector")
    vector_2_STR = input("Introduce las componentes del vector 2 separadas por espacios : ")

    #Separar el String en una Lista : ["1", "2", "3", "4"] y ["5", "6", "7", "8"]
    vector_1 = vector_1_STR.split(" ")
    vector_2 = vector_2_STR.split(" ")

    #Pasar los elementos de la lista a números : [1, 2, 3, 4] y [5, 6, 7, 8]
    vector_1 = list(map(float, vector_1))
    vector_2 = list( map(float, vector_2))

    #Añade los valores de los vectores a las variables globales v1 y v2
    v1.extend(vector_1)
    v2.extend(vector_2)

def productoEscalar(V1, V2):
    resultado = 0

    if len(V1) != len(V2) :
        print("Error. Los vectores no tienen la misma dimensión.")

        return "NO EXISTE"
    else:
        #Cálculo del producto escalar 
        for i in range(len(V1)):
            resultado += V1[i] * V2[i]
    
    
    return resultado

def main():

    pedirVectores()

    print(f"Vector 1 : {v1}")
    print(f"Vector 2 : {v2}")

    print(f"El producto escalar vale : {productoEscalar(v1, v2)}")

if __name__ == "__main__":
    main()