# 1- Definir por asignación una lista con 8 elementos enteros.
# Contar cuantos de dichos valores almacenan un valor superior a 100
# Con While
# lista = [101,2,300,4,5,670,100,830]
# sup_cien = 0
# x = 0
# while x < len(lista):
#     if lista[x] > 100:
#         sup_cien += 1
#     x+=1
# print(f"La cantidad de valores superiores a cien es: {sup_cien}")
# Con For
# lista = [101,2,300,4,5,670,100,830]
# sup_cien = 0
# for x in range(len(lista)):
#     if lista[x] > 100:
#         sup_cien+=1
# print(f"La cantidad de valores superiores a cien es: {sup_cien}")

# -------------------------------------------------------------------------------------------
# 2- Definir una lista por asignación con 5 enteros. Mostrar por pantalla solo
# los elementos con valor iguales o superiores a 7
# lista = [10,2,33,7,5]

# for x in range(len(lista)):
#     if lista[x] >= 7:
#         print(lista[x])
# lista = [10,2,33,7,5]
# x = 0
# while x < len(lista):
#     if lista[x] >= 7:
#         print(lista[x])
#     x+=1

# -------------------------------------------------------------------------------------------
# 3- Definir una lista que almacene por asignación los nombres de 5 personas.
# Contar cuantos de esos nombres tienen 5 o más caracteres
# lista = ["Sergio", "Gladis", "Juan", "Leonardo", "Facundo"]
# mayores = 0
# for x in range(len(lista)):
#     if len(lista[x]) >= 5:
#         mayores += 1
# print(f"La cantidad de nombres con 5 o mas caracteres es: {mayores}")

# -------------------------------------------------------------------------------------------
# 4- Almacenar en una lista los sueldos (valores float) de 5 operarios.
# Imprimir la lista y el promedio de sueldos.
# lista = []
# suma_sueldos = 0
# for x in range(6):
#     sueldo = float(input("Ingrese su sueldo: "))
#     suma_sueldos = suma_sueldos + sueldo
#     lista.append(sueldo)

# print(lista)
# print(f"Promedio de sueldos: {suma_sueldos / 5}")

# -------------------------------------------------------------------------------------------
# 5- Cargar por teclado y almacenar en una lista las alturas de 5 personas
# (valores float)
# Obtener el promedio de las mismas. Contar cuántas personas son más altas
# que el promedio y cuántas más bajas
# lista = []
# suma_alturas = 0
# contador_altos = 0
# contador_bajos = 0
# for x in range(6):
#     altura = float(input("Ingrese su altura: "))
#     lista.append(altura)
#     suma_alturas = suma_alturas + altura

# promedio = suma_alturas / 5

# for x in range(5):
#     if lista[x] > promedio:
#         contador_altos+= 1
#     if lista[x] < promedio:
#         contador_bajos += 1

# print(f"El promedio de las alturas es: {promedio:.2f}") #el especificador :. en f strings rendonde a n decimales
# print("Personas mas altas que el promedio: ",contador_altos)
# print("Personas mas bajas que el promedio: ",contador_bajos)

# -------------------------------------------------------------------------------------------
# 6- Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8
# empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa que
# permita almacenar los sueldos de los empleados agrupados en dos listas.
# Imprimir las dos listas de sueldos
# turno_morning = []
# turno_afternoon = []

# for x in range(8):
#     turno = input("Ingrese turno: mañana o tarde: ").lower()
#     sueldo = float(input("Ingrese sueldo: "))
#     if turno == "mañana" and len(turno_morning) < 5:
#         turno_morning.append(sueldo)
#     elif turno == "tarde" and len(turno_afternoon) < 5:
#         turno_afternoon.append(sueldo)

# print(f"Turno mañana: {turno_morning}")
# print(f"Turno tarde: {turno_afternoon}")

# -------------------------------------------------------------------------------------------
# 7- Ingresar por teclado los nombres de 5 personas y almacenarlos en
# una lista. Mostrar el nombre de persona menor en orden alfabético. 
# nombres = []

# for x in range(5):
#     nomb = input("Ingrese su nombre: ")
#     nombres.append(nomb)

# print(min(nombres))

# -------------------------------------------------------------------------------------------
# 8- Cargar una lista con 5 elementos enteros. Imprimir el mayor y
# un mensaje si se repite dentro de la lista (es decir si dicho valor
# se encuentra en 2 o más posiciones en la lista)
numeros = []
posicion_del_mayor = numeros[0]
for x in range(5):
    num = int(input("Ingrese un numero: "))
    numeros.append(num)
for x in range(1-5):
    if numeros[x] > posicion_del_mayor:
        posicion_del_mayor = numeros[x]

