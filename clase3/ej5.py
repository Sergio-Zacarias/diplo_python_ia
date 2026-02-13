#Confeccionar un programa que permita cargar un número entero positivo
#de hasta tres cifras y muestre un mensaje indicando si tiene
# 1, 2, o 3 cifras.
# Mostrar un mensaje de error si el número de cifras es mayor.

numero = int(input("Ingresar un numero entero positivo de hasta 3 cifras: "))

if numero >= 0 and numero <= 9:
    print("El numero ingresado es de una cifra")
elif numero >= 10 and numero <= 99:
    print("El numero ingresado es de dos cifras")
elif numero >= 100 and numero <= 999:
    print("El numero ingresado es de tres cifras")
else:
    print("Error el numero ingresado es mayor a tres cifras o negativo")