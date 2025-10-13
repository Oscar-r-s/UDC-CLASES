"""
• Realizar un programa en Python que pida al usuario por teclado un número 
entero n mayor que 0 y menor que 10. Si n no verifica las condiciones 
solicitadas, debe volver a pedirse las veces que sea necesario.  
• Calcule y muestre por pantalla el superfactorial (sf) de n: 
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

superFactorial = 1

#Número que se pide para hacer el superfactorial
print("============================================= ")
n = int(input("Introduce un número mayor que 0 y menor que 10 : "))

while n<=0 or n>10 :
    print("============================================= ")
    n = int(input("Error en el rango. Introduce un número mayor que 0 y menor que 10 : "))

for i in range(1, n +1 ):
    superFactorial = superFactorial * factorial(i)

print(f"El superfactorial de {n} vale : {superFactorial}")
print("============================================= ")




