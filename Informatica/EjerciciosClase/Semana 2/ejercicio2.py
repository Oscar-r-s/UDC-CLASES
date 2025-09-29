"""
Ejercicio 2
• Queremos hacer un encargo de pegatinas a una empresa que nos ha 
dado un presupuesto de 0.09 euros por pegatina. La empresa nos 
ofrece un descuento del 8% si la cantidad de pegatinas es superior a 
500 y un descuento del 12% si la cantidad es mayor de 1000.  

• Pedir por teclado una cantidad de pegatinas y mostrar por pantalla el 
precio total con dos decimales. Se deberá controlar que el dato de 
entrada sea correcto (positivo mayor que cero)
"""

print("================================================= ")
pegatinas = int(input("Introduce el número de pegatinas : "))

coste_pegatinas = 0.09

precio = 0

if 0 <= pegatinas :
    precio = pegatinas * coste_pegatinas

    if pegatinas > 500:
        precio = (92/100)*precio
        print('Aplicando un 8% de descuento : ')

    elif pegatinas > 1000 :
        precio = (88/100)*precio
        print('Aplicando un 8% de descuento : ')

    
    print(f"El precio de {pegatinas} pegatinas es de {precio:.2f} euros")

else : 
    print("Error, el número de pegatinas tiene que ser positivo")

print("================================================= ")
