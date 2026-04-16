"""
Funciones I.
Aproximación del valor de cos(x) mediante la serie de Taylor.
Usando funciones.
"""

import math

def pedir_real(min, max):
    valor = float(input(f"Introduce un número real entre {min} y {max}: "))
    while valor<min or valor>max:
        valor = float(input(f"Valor no válido, debe estar entre {min} y {max}: "))
    return valor

def pedir_entero(min,max):
    valor = int(input(f"Introduce un número entero entre {min} y {max}: "))
    while valor<min or valor>max:
        valor = int(input(f"Valor no válido, debe estar entre {min} y {max}: "))
    return valor

#Función que calcula el factorial de n
def factorial (n):
    factorial = 1
    for indice in range(2,n+1):
        factorial = factorial*indice
    return factorial

# Cálculo de la serie de Taylor
def coseno_taylor (x,k):
    cos = 0.0

    for n in range(k+1):
        numerador = (-1)**n * x**(2*n)

        # El divisor es el factorial de 2n
        factor = factorial(2*n) 

        cos += numerador/factor
    
    return cos

#PROGRAMA PRINCIPAL

# Leemos el valor de x
print("Primero necesito el valor de x para calcular su coseno.")
x = pedir_real(-3.14,3.14)
print()

# Leemos el valor de k (iteraciones)
print("Ahora necesito el valor de k para la precisión del cálculo.")
k = pedir_entero(1,100)
print()

# Calculamos el coseno
coseno = coseno_taylor(x,k)

# Imprimimos el resultado
print(f"El valor aprox. de cos(x) es {coseno:.13f} y el real es {math.cos(x):.13f}")