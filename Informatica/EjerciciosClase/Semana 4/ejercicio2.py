"""
• Implementa un programa en Python que muestre por pantalla una escalera hecha 
con números. El número de escalones será pedido por teclado al usuario (mínimo 1). 
"""

#Pedir un número entero al usuario
print("============================================= ")
n = int(input("Introduce un número entero mayor que 0 : "))

#Detección de errores
while n<=0 :
    print("============================================= ")
    n = int(input("Error en el rango. Introduce un número mayor que 0 : "))

#Array que va a almacenar la serie de números desde 1 a n
numeros = []

#Imprimir el array por cada iteración / actualización del array números
for i in range(1, n+1):
    numeros.append(i)
    print(numeros)

print("============================================= ")