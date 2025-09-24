"""
• Implementar un programa en Python que pida un importe 
en euros al usuario (sin céntimos) y le diga el número 
mínimo de billetes de cada tipo (500€, 200€, 100€, 50€, 
20€, 10€, 5€) y de monedas también de cada tipo (2€, 1€) 
que hacen falta para llevar dicho importe en la cartera 

• Si no hacen falta billetes o monedas de un tipo 
determinado se indicará 0 billetes / monedas de dicho 
tipo. 
8

"""

def cuantos_billetes():

    #Declaro los billetes y las monedas existentes, de mayor a menor
    billetes = [500, 200, 100, 50, 20, 10, 5]
    monedas = [2,1]

    #Importe que se le pide al usuario
    importe = int(input("Introduce una cantidad entera de euros : "))

    #La cantidad 'restante' que nos queda por clasificar
    restante = importe

    #Por cada billete en 'billetes'; La cantidad de billetes es lo que queda (restante) tras hacer division entera. Restante es el resto
    for b in billetes :
        cantidad = restante // b
        restante = restante % b
        print(f"Billetes de {b}: {cantidad}")

    for m in monedas :
        cantidad = restante // m
        restante = restante % m
        print(f"Monedas de {m}: {cantidad}")

cuantos_billetes()








