#Se ingresa por teclado un valor entero, mostrar una leyenda que indique
#si el número es positivo, negativo o nulo (es decir cero)

numero = int(input("Ingresar un numero entero, positivo, negatico o 0: "))

if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es 0, nulo")