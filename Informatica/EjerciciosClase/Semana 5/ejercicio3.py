"""
• Implementar un programa en Python que:  
• Pida al usuario por teclado un número real (x) que debe estar entre -PI y PI. 
• Pida al usuario por teclado un número entero (k) que debe estar entre 1 y 100. 
• En ambos casos, si los valores están fuera de rango, se pedirán repetidamente. 
• Calcule y muestre por pantalla, con 13 decimales, el valor de cos(x) y su 
aproximación mediante la siguiente serie para el valor de k introducido por teclado: 
"""

import math

# Función para calcular cos(x)
def cos_aproximado(xn, kn):
    aproximacion = 0
    for n in range(kn):
        #Fórmula dada en el anunciado para la aproximación
        termino = ((-1) ** n) * (xn ** (2 * n)) / math.factorial(2 * n)
        aproximacion += termino
    return aproximacion

#Pedir x
x = float(input("Número x. Introduce un número en el intervalo [-π, π]: "))

#Control de errores [-π, π] :
while  x < (-math.pi) or x > math.pi:
    x = float(input("Error en el rango. Introduce un número x válido: "))

#Pedir k
k = int(input(f"Número k. Introduce un número entero en el intervalo [1, 100]: "))

#Control de errores [1, 100]: 
while k < 1 or k > 100 :
    k = int(input(f"Error. Introduce un número k válido en el intervalo [1, 100]: "))

print(f"El valor aproximado de cos(x) es {cos_aproximado(x,k)} y el real es {math.cos(x)}")