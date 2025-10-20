"""
Implementa un programa en Python que pida al usuario por teclado dos números 
enteros n y k que cumplan n ≥ k ≥ 1, calcule las combinaciones de n elementos 
tomados de k en k y muestre el resultado por pantalla: 
"""

#Función que calcula el factorial de un número
def factorial(n):

    factorial = n
    num_i = 0

    for i in range(1, n):
        #Si n = 5 esta variable por cada iteración sería : 4, 3, 2, 1. 
        num_i = n-i
        #Actualizo el valor de la variable factorial
        factorial = factorial * num_i
    
    return factorial

#Funcion que calcula las combinaciones utilizando la fórmula del enunciado
def combinaciones (kn,mn):
    return (factorial(mn)) / (factorial(kn) * factorial(mn-kn))

def entrada_datos(): 
    #Pedir k
    k = int(input("Número k. Introduce un número mayor o igual que 1: "))

    #Control de errores
    while k<1 :
        k = int(input("Error en el rango. Introduce un número k válido: "))

    #Pedir n
    n = int(input(f"Número n. Introduce un número mayor o igual {k}: "))

    #Control de errores
    while n<k :
        n = int(input(f"Error en el rango. Introduce un número n válido, mayor que {k}: "))

    return n, k

n,k = entrada_datos()

#El número de combinaciones de n y k almacenado en una variable
numero_combinaciones = combinaciones(k,n)

print(f"Las combinaciones de {k} elementos tomadas de {n} en {n} son : {numero_combinaciones}")