# Se ingresa por teclado un número positivo de uno o dos dígitos
# (1..99) mostrar un mensaje indicando si el número tiene uno o dos
# dígitos.

numero = int(input("Ingrese un número positivo de uno o dos dígitos 1-99: "))

if numero >= 10:
    print("El numero tiene dos digitos")
else:
    print("The number have one digit")
    
