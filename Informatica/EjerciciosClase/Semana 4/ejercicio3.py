"""
• Implementar un programa en Python que:  
• Pida al usuario un número entero mayor que 0 (k) por teclado. Si k no es mayor que 
    0, debe volver a pedirse las veces que sea necesario.  
• Pida al usuario un número real (x) por teclado.  
• Calcule y muestre por pantalla, con 13 decimales, el valor de cos(x) y su 
    aproximación mediante la siguiente serie para el valor de k introducido por teclado:  
"""

import math

# Función para calcular cos(x) usando su serie
def cos_aproximado(x, k):
    aproximacion = 0
    for n in range(k):
        termino = ((-1) ** n) * (x ** (2 * n)) / math.factorial(2 * n)
        aproximacion += termino
    return aproximacion

# Pedir número entero mayor que 0
k = int(input("Introduce un número entero mayor que 0 (k): "))

#Control de errores
while k<=0:
    print("=============================================")
    k = int(input("Error en el rango. Introduce un número entero mayor que 0 (k): "))

# Pedir número real
x = float(input("Introduce un número real (x): "))
   

# Calcular valores
valor_real = math.cos(x)
valor_aprox = cos_aproximado(x, k)

# Mostrar resultados con 13 decimales
print(f"El valor de cos({x:.6f}) real es {valor_real:.13f}, y el aproximado es {valor_aprox:.13f}.")
print("=============================================")


