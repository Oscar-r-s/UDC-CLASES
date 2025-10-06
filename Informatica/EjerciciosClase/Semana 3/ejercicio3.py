divisiores = []
suma_divisores = 0

n = int(input("Introduce un número entero positivo : "))

while n<=0 :
    n = int(input("Introduce un número entero positivo : "))

#Desde 1 hasta el número (no incluyéndolo)
for i in range(1, n):
    if(n % i == 0):
        divisiores.append(i)

#Por cada divisor en la lista, sumarlo en una variable
for j in range(len(divisiores)):
    suma_divisores += divisiores[j]

if(n == suma_divisores):
    print(f"{n} SÍ es un número perfecto")
else:
    print(f"{n} NO es un número perfecto")
