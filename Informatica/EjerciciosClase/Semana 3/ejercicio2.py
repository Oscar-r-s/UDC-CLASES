"""
• Desarrollar un programa en Python que calcule el factorial de un número n que 
se pedirá al usuario por teclado 
• El número n pedirá de forma repetida hasta que esté en el rango correcto 
(mayor que 0) 
• El factorial de un número n se calcula como: 
factorial = n*(n-1)*(n-2)*....*1 
• Es obligatorio el uso de for y range para resolver el ejercicio
"""

n = int(input("Introduce un número entero positivo: "))

factorial = n
num_i = 0

while n<=0 :
    print("Error en el rango")
    n = int(input("Introduce un número entero positivo: "))


for i in range(1, n):
    #Si n = 5 esta variable por cada iteración sería : 4, 3, 2, 1. 
    num_i = n-i
    #Actualizo el valor de la variable factorial
    factorial = factorial * num_i

print(factorial)