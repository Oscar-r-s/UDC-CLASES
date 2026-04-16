# Primos gemelos

# funcion que pide por teclado un número positivo
def leer_positivo():
    num = int(input("Introduce el numero máximo (>0):"))
    while num <= 0:
        print("Error, el número debe ser mayor que cero")
        num = int(input("Introduce el numero máximo (>0): "))
    return num


# Devuelve los divisores de un número n
def es_primo(cand):
    div = 2
    primo = True
    while div <= cand // 2 and primo:
        if cand % div == 0:
            primo = False
        div = div + 1
    return primo


# Programa principal
n = leer_positivo()
print(f"Los primos gemelos hasta {n} son:")
for candidato in range(3, n + 1):
    if es_primo(candidato):
        if es_primo(candidato + 2):
            print(f"{candidato} y {candidato+2}")