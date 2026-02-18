# 1- Confeccionar un programa que lea n pares de datos, cada par de datos
# corresponde a la medida de la base y la altura de un triángulo.
# El programa deberá informar:
# a) De cada triángulo la medida de su base, su altura y su superficie.
# b) La cantidad de triángulos cuya superficie es mayor a 12
# superficie_mayores = 0

# for x in range(5):
#     base = int(input("Ingrese la medida de la base del triangulo: "))
#     altura = int(input("Ingrese la medida de la altura del triangulo: "))
#     superficie = base * altura / 2
#     if superficie > 12:
#         superficie_mayores += 1
#     print(f"La medida de la base es: {base}")
#     print(f"La medida de la altura es: {altura}")
#     print(f"La medida de la superficie es: {superficie}")
#     # print(x)

# print(f"La cantidad de triangulos con superficie mayor a 12 es de: {superficie_mayores}")



# -------------------------------------------------------------------------------------------

# 2- Desarrollar un programa que solicite la carga de 10 números e
# imprima la suma de los últimos 5 valores ingresados.

# last_five_values = 0

# for x in range(10):
#     numero = int(input("Ingrese un numero: "))
#     if x >= 5:
#         last_five_values = last_five_values + numero

# print(f"La suma de los ultimos 5 valores es de: {last_five_values}")



# -------------------------------------------------------------------------------------------

# 3- Desarrollar un programa que muestre la tabla de multiplicar del
# 5 (del 5 al 50)

# for x in range(10):
#     print(5 * (x + 1))



# -------------------------------------------------------------------------------------------

# 4- Confeccionar un programa que permita ingresar un valor del 1 a
# 10 y nos muestre la tabla de multiplicar del mismo
# (los primeros 12 términos)
# Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3,
# 6, 9, hasta el 36.

# FORMA SIN VERIFICACION DEL VALOR INGRESADO
# valor = int(input("Ingrese un valor del 1 al 10: "))
# for x in range(12):
#     print(f"{3 * (x + 1)}")

# FORMA CON VERIFICACION DEL VALOR INGRESADO
# valor = int(input("Ingrese un valor del 1 al 10: "))
# while valor > 10 or valor < 1:
#     valor = int(input("Error, el numero no esta en el rango indicado. Ingrese nuevamente un valor del 1 al 10: "))

# for x in range(12):
#     print(f"{valor * (x + 1)}")




# -------------------------------------------------------------------------------------------

# 5- Realizar un programa que lea los lados de n triángulos, e informar:
# a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados
# iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
# b) Cantidad de triángulos de cada tipo.

# cont_equilatero = 0
# cont_isosceles = 0
# cont_escaleno = 0

# for x in range(5):
#     lado1 = int(input("Ingrese medida del primer lado del triangulo: "))
#     lado2 = int(input("Ingrese medida del segundo lado del triangulo: "))
#     lado3 = int(input("Ingrese medida del tercer lado del triangulo: "))
    
#     if lado1 == lado2 and lado2 == lado3:
#         print("Es un triangulo equilatero")
#         cont_equilatero += 1
#     elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
#         print("Es un triangulo isosceles")
#         cont_isosceles += 1
#     else:
#         print("Es un triangulo escaleno")
#         cont_escaleno += 1

# print(f"La cantidad de triangulos escalenos es de: {cont_escaleno}")
# print(f"La cantidad de triangulos isosceles es de: {cont_isosceles}")
# print(f"La cantidad de triangulos equilateros es de: {cont_equilatero}")

