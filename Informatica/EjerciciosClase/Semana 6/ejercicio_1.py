#Suma fracciones - Semana 6 - Ejercico 1

def pedir_fraccion(orden):
    #Numerador
    n = int(input(f"Introduzca el numerador de la {orden} fracción: "))
    while n <=0 :
        n = int(input(f"El dato tiene que ser mayor que cero, vuelve a intentarlo: "))
    
    #Denominador
    d = int(input(f"Introduzca el denaminador de la {orden} fracción: "))
    while d <=0 :
        d = int(input(f"El dato tiene que ser mayor que cero, vuelve a intentarlo: "))

    print() #Salto de línea

    return n, d


def sumarFracciones(n1, d1, n2, d2):
    #Suma de Fracciones sin simplificar: 
    """
    n1/d1 + n2/d2 = (n1*d2 + d1*n2) / d1*d2
    """
    numerador = (n1*d2 + d1*n2)
    denominador = d1*d2

    return numerador, denominador

def MCD(a,b):
    #Método de Nicómano
    while a != b :
        if a > b:
            a = a - b
        if b > a :
            b = b - a
    
    return a


def simplificarFraccion(nf, df):
    max_com_div = MCD(nf, df)

    return int(nf / max_com_div) , int(df / max_com_div)

#función que encapsula el programa principal
def main():
    print("========================================================== ")
    num1,den1 = pedir_fraccion("primera")
    num2,den2 = pedir_fraccion("segunda")
    num_suma,den_suma = sumarFracciones(num1,den1,num2,den2)
    num_final, den_final = simplificarFraccion(num_suma,den_suma)

    if num_final == num_suma: #si el mcd es 1
        print("\nAviso: la suma NO se ha podido simplificar.")
    else:
        print("\nAviso: la suma se ha simplificado.")

    if den_final == 1: #si no es una fraccion
        print(f"\nEl resultado de sumar {num1}/{den1} + {num2}/{den2} es {num_final}")
    else:
        print(f"\nEl resultado de sumar {num1}/{den1} + {num2}/{den2} es {num_final}/{den_final}")

#programa principal
if __name__ == "__main__":
    main()
