"""
• Realizar un programa en Python que que lea un un número entero positivo n por 
teclado, que no sea mayor que 100, y que escriba tres columnas por pantalla:    

    1. La primera columna muestra los números desde 1 hasta n de uno en uno. 
    2. La segunda columna muestra los números desde 2n hasta 2 de dos en dos.  
    3. La tercera columna contiene un símbolo (+) si el dato de la primera columna 
    es mayor que el de la segunda y un (-) si sucede lo contrario.  

• Si el número introducido no cumple las condiciones mencionadas anteriormente 
se le pedirá de nuevo al usuario hasta que se obtenga uno válido.
"""
print("============================================= ")
n = int(input("Dime un número positivo menor que 100: "))

hasta_n = [] #Si n = 9 : [1, 2, 3, 4, 5, 6, 7, 8, 9]
desde_2n_hasta_2 = []#Si n= 9 : [18, 16, 14, 12, 10, 8, 6, 4, 2]

if(0<n<=100 and (int(n) - n == 0)):

    for i in range(n):
        hasta_n.append(i + 1)

    for j in range(2*n, 1, -2):
        desde_2n_hasta_2.append(j)

    for k in range(len(hasta_n)):
        signo = ""

        if(hasta_n[k] > desde_2n_hasta_2[k]):
            signo = "+"

        elif((hasta_n[k] < desde_2n_hasta_2[k])):
            signo = "-"

        else:
            signo = "="

        print(f"{hasta_n[k]}    {desde_2n_hasta_2[k]}     ({signo})")
    
    print("============================================= ")


else:
    print("Error en el rango.")
    print("============================================= ")
