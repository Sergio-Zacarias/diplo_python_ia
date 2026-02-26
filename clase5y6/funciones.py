# 1- Desarrollar un programa con dos funciones. La primer solicite el ingreso
# de un entero y muestre el cuadrado de dicho valor. La segunda que solicite
# la carga de dos valores y muestre el producto de los mismos.
# LLamar desde el bloque del programa principal a ambas funciones
# def cuadrado():
#     num = int(input("Ingrese un numero: "))
#     print(f"El cuadrado del numero ingresado es: {num**2}") #Eleva numero al cuadrado
# def producto():
#     num1 = int(input("Ingrese primer numero: "))
#     num2 = int(input("Ingrese segundo numero: "))
#     print(f"El producto de ambos numeros es: {num1*num2}")

# cuadrado()
# producto()

# -------------------------------------------------------------------------------------------
# 2- Desarrollar un programa que solicite la carga de tres valores y muestre
# el menor. Desde el bloque principal del programa llamar 2 veces a dicha
# función (sin utilizar una estructura repetitiva)
# def mostrar_menor(num1,num2,num3):
#     print("El valor menor es: ")
#     if num1 < num2 and num1 < num3:
#         print(num1)
#     elif num2 < num1 and num2 < num3:
#         print(num2)
#     else:
#         print(num3)
# def cargar_valores():
#     valor1 = int(input("Ingrese primer valor: "))
#     valor2 = int(input("Ingrese segundo valor: "))
#     valor3 = int(input("Ingrese tercer valor: "))
#     mostrar_menor(valor1,valor2,valor3)

# cargar_valores()

# ------------------------------------------------------------------------------------------- 
# 3- Desarrollar una funcion que reciba un string como parametro y nos
# muestre la cantidad de vocales. Llamarla desde el bloque principal del
# programa 3 veces con string distintos
# def contador_vocales(str):
#     cont_vocals = 0
#     minusculas = str.lower()
#     for x in range(len(minusculas)):
#         if minusculas[x] == "a" or minusculas[x] == "e" or minusculas[x] == "i" or minusculas[x] == "o" or minusculas[x] == "u":
#             cont_vocals += 1
#     print(f"La palabra {minusculas} contiene: {cont_vocals} vocales")
# contador_vocales("perro")
# contador_vocales("gatubelo")
# contador_vocales("prr")

# -------------------------------------------------------------------------------------------
# 4- Confeccionar una función que reciba tres enteros y los muestre ordenados
# de menor a mayor. En otra función solicitar la carga de 3 enteros por
# teclado y proceder a llamar a la primer función definida

# def ordenar_imprimir(v1,v2,v3):
#     if v1<v2 and v1<v3:
#         if (v2<v3):
#             print(v1,v2,v3)
#         else:
#             print(v1,v3,v2)
#     else:
#         if (v2<v3):
#             if (v1<v3):
#                 print(v2,v1,v3)
#             else:
#                 print(v2,v3,v1)
#         else:
#             if (v1<v2):
#                 print(v3,v1,v2)
#             else:
#                 print(v3,v2,v1)

# def cargar_valores():
#     valor1 = int(input("Ingrese primer valor: "))
#     valor2 = int(input("Ingrese segundo valor: "))
#     valor3 = int(input("Ingrese tercer valor: "))
#     ordenar_imprimir(valor1,valor2,valor3)

# cargar_valores

# -------------------------------------------------------------------------------------------
# 5- Elaborar una función que reciba tres enteros y nos retorne el valor
# promedio de los mismos
# def promedio(num1,num2,num3):
#     promedio = (num1 + num2 + num3) // 3 #elimina parte decimal y deja la parte entera redondea hacia abajo
#     return print(promedio) #uso print porque sino sale muy rapido en consola y no se llega a ver el return
# valor1 = int(input("Ingrese primer valor: "))
# valor2 = int(input("Ingrese segundo valor: "))
# valor3 = int(input("Ingrese tercer valor: "))
# promedio(valor1,valor2,valor3)

# -------------------------------------------------------------------------------------------
# 6- Elaborar una función que nos retorne el perímetro de un cuadrado
# pasando como parámetros el valor de un lado
# def perimetro(lado):
#     perimetro = lado * 4
#     return print(f"El perimetro del cuadrado es: {perimetro}")

# perimetro(2) 
# Otra variante
# lado=int(input("Lado del cuadrado:"))
# print("El perimetro es:",retornar_perimetro(lado))

# -------------------------------------------------------------------------------------------
# 7- Confeccionar una función que calcule la superficie de un rectángulo
# y la retorne, la función recibe como parámetros los valores de dos de su
# lados:
# En el bloque principal del programa cargar los lados de dos rectángulos
# y luego mostrar cual de los dos tiene una superficie mayor
# def retornar_superficie(base,altura):
#     superficie = base * altura
#     return superficie

# print("Primer rectangulo")
# valor1 = int(input("Ingrese lado menor del rectangulo: "))
# valor2 = int(input("Ingrese lado mayor del rectangulo: "))
# print("Segundo rectangulo")
# valor3 = int(input("Ingrese lado menor del rectangulo: "))
# valor4 = int(input("Ingrese lado mayor del rectangulo: "))

# if retornar_superficie(valor1,valor2) == retornar_superficie(valor3,valor4):
#     print("Las superficies son iguales")
# else:
#     if retornar_superficie(valor1,valor2) > retornar_superficie(valor3,valor4):
#         print("El primer rectangulo tiene una superficie mayor")
#     else:
#         print("El segundo rectangulo tiene una superficie mayor")

# -------------------------------------------------------------------------------------------
# 8- Plantear una función que reciba un string en mayúsculas o minúsculas y
# retorne la cantidad de letras 'a' o 'A
# def contador_letra_a(str):
#     cont_a_mayusculas = 0
#     cont_a_minusculas = 0
#     for x in range(len(str)):
#         if str[x] == "A":
#             cont_a_mayusculas += 1
#         if str[x] == "a":
#             cont_a_minusculas += 1
#     return print(f"La cantidad de letras a mayusculas es de: {cont_a_mayusculas} y la cantidad de letras a minusculas es de: {cont_a_minusculas}")

# contador_letra_a("parAguAs")
# contador_letra_a("lluviahermosA")
#Otra variante
# def cantidad_vocal_a(palabra):
#     cant=0
#     for x in range(len(palabra)):
#         if palabra[x]=='a' or palabra[x]=="A":
#             cant=cant+1
#     return cant
# # bloque principal
# palabra=input("Ingrese una palabra:")
# print("La palabra",palabra,"tiene",cantidad_vocal_a(palabra),"a")


# -------------------------------------------------------------------------------------------
# 9- Confeccionar una función que reciba entre 2 y 5 enteros.
# La misma nos debe retornar la suma de dichos valores. Debe tener tres
# parámetros por defecto

# def suma(num1, num2, num3=8, num4=2, num5=7):
#     total = num1 + num2 + num3 + num4 + num5
#     return print(total)
# suma(5,2,7)
# suma(1,1)
# suma(5,7,8,3)
# suma(1,2,3,4,5)

