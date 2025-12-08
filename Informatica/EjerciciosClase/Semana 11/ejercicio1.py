"""
Dada una tabla de densidades típicas de materiales en kg/m³ almacenadas en un 
diccionario ({nombre_material: densidad}), escribir un programa que: 
• Muestre por pantalla la tabla de materiales y sus densidades. El listado se 
definirá como un diccionario inicial con estos elementos: acero     7850.0 
aluminio  2700.0 
cobre     8960.0 
hormigon  2400.0 
agua      1000.0 
• Pregunte al usuario por un material y devuelva su volumen en m³. 
• Si el material existe, calcule y muestre la masa (m = densidad · volumen). 
• Si el material no está en el diccionario, mostrar un mensaje indicándolo.

"""

def imprimirDiccionario(diccionario):
    claves = diccionario.keys()
    for i in claves:
        print(f"{i:15s}{diccionario[i]} kg/m3") #El ".15s" lo que hace es rellenar 15 espacios en blanco

def preguntarMaterial(dicc):
    material = input("¿Qué material quieres? : ")
    while material not in dicc:
        material = input("Error, no existe. ¿Qué material quieres? : ")
    volumen = int(input("¿Qué volumen en m3? : "))
    while volumen < 0 :
        volumen = int(input("El volumen tiene que ser positivo. ¿Qué volumen en m3? : "))
        

    return material, volumen

def calculoMasa(dicc, mater, vol):

    return dicc[mater] * vol

def main():
    materiales_y_densidades = {
    "acero" : 7850.0,
    "aluminio": 2700.0,
    "cobre": 8960.0,
    "hormigón": 2400.0,
    "agua": 1000.0
    }

    print("##################################")
    print("------- Densidades Típicas -------")
    imprimirDiccionario(materiales_y_densidades)
    print("------------------------------------")

    material, volumen = preguntarMaterial(materiales_y_densidades)

    print(f"La masa de {volumen} m3 de {material} es de {calculoMasa(materiales_y_densidades, material, volumen)} kg")
    print("##################################")


if __name__ == "__main__":
    main()