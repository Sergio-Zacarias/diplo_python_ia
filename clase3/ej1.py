# Realizar un programa que solicite la carga por teclado de dos números
# si el primero es mayor al segundo informar su suma y diferencia
# en caso contrario informar el producto y la división del primero respecto al segundo.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 > num2:
    print("La suma de ambos numeros es: ",num1 + num2)
    print("La resta de ambos numeros es: ",num1 - num2)
else:
    print("La multiplicacion de ambos numeros es: ",num1 * num2)
    print("La division de ambos numeros es: ",num2 / num1)
