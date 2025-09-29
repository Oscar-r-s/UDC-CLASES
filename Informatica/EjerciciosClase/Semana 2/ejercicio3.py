"""
Realizar un programa en Python que pida al usuario un número entero 
por teclado de 3 cifras e indique si es capicúa
"""
print("================================================= ")
numero = input("Introduce un número de 3 cifras : ")

digits = []

if int(numero) < 0 :
    print("Números negativos no son válidos")

else :
    for num in numero :
        digits.append(num)

    if len(digits) > 3:
        print("Número inválido por ser mayor de 3 cifras")

    else :
        if digits[0] == digits[2]:
            print("El número SÍ es capicúa")
        else :
            print("El número NO es capicúa")

print("================================================= ")
