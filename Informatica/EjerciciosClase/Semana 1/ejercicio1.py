"""
Implementar un programa en Python que calcule el Índice de Masa 
Corporal (IMC) utilizando la siguiente fórmula :

IMC = peso / (altura **2)
"""
print("=================================================")

#Datos que se le piden al usuario 
peso = float(input("¿Cual es tu peso en kg? "))
altura = float(input("¿Cual es tu altura en metros? "))

#Fórmula a aplicar para calcular el IMC
IMC = peso/(altura**2)

#Mostrar al usuario el resultado por pantalla, redondeando los decimales
print('Tu índice de masa corporal es :', round(IMC))
print("=================================================")


