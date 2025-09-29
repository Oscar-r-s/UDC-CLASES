"""
Programa que calcula el área y longitud de una circunferencia.
"""
import math

#Entrada de datos
radio = float(input("Introduce el radio: "))

#Cálculos
area = math.pi * radio **2
longitud = 2 * math.pi * radio

#Salida de datos
print(f"El area vale {area:.2f} y la longitud {longitud:.2f}")