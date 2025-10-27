

def factorial(n):

    factorial = n
    num_i = 0

    for i in range(1, n):
        #Si n = 5 esta variable por cada iteración sería : 4, 3, 2, 1. 
        num_i = n-i
        #Actualizo el valor de la variable factorial
        factorial = factorial * num_i
    
    return factorial

def esPrimo(n):
    for i in range (2, n):
        if (n % i == 0):
            return "no es primo"
    return "es primo"

def es_numero_perfecto(numero):
    if numero <= 1:
        return "no es perfecto"  # Los números perfectos son mayores que 1
    
    suma_divisores = 0
    for i in range(1, int(numero**0.5) + 1):
        if numero % i == 0:
            suma_divisores += i
            if i != 1 and i != numero / i: # Evita sumar el número o duplicar la raíz cuadrada
                suma_divisores += numero / i

    if suma_divisores == numero :
        return "es perfecto"
    else:
        return "no es perfecto"

def pedirNum_Mayor_Cero():
    n = int(input("Introduce un número mayor que cero : "))
    while n < 0 :
        n = int(input("Error. Introduce un número mayor que cero : "))

    return n

def funcionEscogida(e):
    if e == 1 :
        print("Has escogido Calcular el Factorial")
    elif e == 2 :
        print("Has escogido Comprobar Primo")
    elif e == 3 :
        print("Has escogido Comprobar perfecto")
    elif e == 4 :
        print("Has escogido Salir")
    
    print()

def pedirOpcion():
    op = int(input("Escoge una de las opciones anteriores : "))
    while op < 1 or op > 4 :
        op = int(input("Opción incorrecta. Vuelva a intentarlo : "))
    
    return op

def ejecucion(eleccion):
    #Escoge la primera opción
        if eleccion == 1 :
            num = pedirNum_Mayor_Cero()
            print(f"El factorial de {num} vale {factorial(num)}")
            print("========================================================== ")

        #Escoge la segunda opción
        elif eleccion == 2 :
            num = pedirNum_Mayor_Cero()
            print(f"El número {num} {esPrimo(num)}")
            print("========================================================== ")

        #Escoge la tercera opción
        elif eleccion == 3 :
            num = pedirNum_Mayor_Cero()
            print( f"El número {num} {es_numero_perfecto(num)}")
            print("========================================================== ")




def main():

    print("""
====================================================================== 
1- Calcular factorial 
2- Comprobar primo 
3- Comprobar perfecto 
4- Salir 
""")

    opcion = pedirOpcion()

    funcionEscogida(opcion)
    
    ejecucion(opcion)


if __name__ == "__main__":
    main()

