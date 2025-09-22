"""
Implementar un programa en Python que calcule el Índice de Masa 
Corporal (IMC) utilizando la siguiente fórmula :

IMC = peso / (altura **2)
"""
print("=================================================")
peso = float(input("¿Cual es tu peso en kg? "))
altura = float(input("¿Cual es tu altura en metros? "))
print("Tu índice de masa corporal es :", round(peso/(altura**2)))
print("=================================================")


