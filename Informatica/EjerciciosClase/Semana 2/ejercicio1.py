"""
IMC = peso / (altura^2)
"""
IMC = 0
print("================================================= ")
peso = float(input("Cual es tu peso en kg ? :"))


if peso <= 0 :
    print("Error, el peso tiene que ser mayor que 0.")
    print("================================================= ")


else: 
    altura = float(input("Introduce tu altura en metros :"))

if altura <= 0 :
    print("Error, la altura tiene que ser mayor que cero")
    print("================================================= ")


else:
    IMC = peso / (altura**2)
    print(f"Tu Índice de Masa Corporal es : {IMC:.2f}")

    if IMC < 18.5 :
        print("Tu estado es BAJO PESO")
    elif 18.5 < IMC < 24.99 :
        print("Tu estado es NORMAL")
    elif 25.0 < IMC < 29.99 :
        print("Tu estado es SOBREPESO")
    else :
        print("Tu estado es OBESIDAD")
print("================================================= ")

