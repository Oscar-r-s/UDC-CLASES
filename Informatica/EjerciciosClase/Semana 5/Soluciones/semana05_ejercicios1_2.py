#Combinaciones

#funcion que pide por teclado un número mayor que el argumento
def pedir_numero (min):
    num = int(input(f"Introduce un valor mayor o igual que {min}: "))
    while num<min:
        num = int(input("Error en el rango. Introduce el número: "))
    return num

#Función que calcula el factorial de n
def factorial (n):
    factorial = 1
    for indice in range(2,n+1):
        factorial = factorial*indice
    return factorial

#Programa principal
print("Número k. ",end="")
k = pedir_numero(int("1"))
print("Número n. ",end="")
n = pedir_numero(k)

combinaciones = factorial(n)//(factorial(k)*factorial(n-k))

print(f"Las combinaciones de {n} elementos tomadas de {k} en {k} son: {combinaciones}")

