"""
• Desarrollar un programa en Python que calcule todos los números primos gemelos hasta un 
número máximo dado por el usuario, que debe ser positivo: 
• Dos números primos se denominan gemelos si uno de ellos es igual al otro más dos 
unidades.  
• Por ejemplo, los números primos 3 y 5 forman una pareja de primos gemelos. Otros ejemplos 
de pares de primos gemelos son 5 y 7 ó 11 y 13 
• Funciones a implementar como mínimo: 
• pedir_max(): petición del número máximo  
• es_primo(): devuelve True si el número que se le pasa como argumento es primo y False si no 
lo es
10
"""
#Programa que no comento porque creo que se auto-explica con el nombre de las funciones

def pedirMax():
    max = int(input("Introduce un número máximo positivo : "))
    return max

def esPrimo(n):
    for i in range (2, n):
        if (n % i == 0):
            return False
    return True

def primosGemelos(m):
    print(f"Los números primos gemelos hasta {m} son :")

    for i in range (1, m + 1):

        if esPrimo(i) and esPrimo(i + 2):
            print(f"{i} y {i + 2}")


max = pedirMax()

while max <= 0 :
    max = pedirMax()

primosGemelos(max)