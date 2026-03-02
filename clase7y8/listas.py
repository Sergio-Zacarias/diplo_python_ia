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

#Respuesta Gemini
# 1. Cargamos la lista
# numeros = []
# for i in range(5):
#     valor = int(input(f"Ingresa el número {i+1}: "))
#     numeros.append(valor)

# # 2. Encontramos el mayor manualmente
# # Asumimos que el primero es el mayor para empezar
# mayor = numeros[0] 

# for n in numeros:
#     if n > mayor:
#         mayor = n

# # 3. Contamos las repeticiones manualmente
# contador = 0
# for n in numeros:
#     if n == mayor:
#         contador += 1

# # Imprimimos resultados
# print(f"\nEl número mayor es: {mayor}")

# if contador > 1:
#     print(f"¡Atención! El número {mayor} se repite {contador} veces.")
# else:
#     print("El número mayor no se repite.")

# -------------------------------------------------------------------------------------------
# LISTAS PARALELAS
# 9- Crear y cargar dos listas con los nombres de 5 productos en una y sus
# respectivos precios en otra. Definir dos listas paralelas. Mostrar cuantos
# productos tienen un precio mayor al primer producto ingresado
# nombres = []
# precios = []
# contador_mayores = 0
# print("Ingreso de productos")
# for x in range(5):
#     nomb = input("Ingrese nombre del producto: ")
#     precio = float(input("Ingrese precio del producto: "))
#     nombres.append(nomb)
#     precios.append(precio)

# for x in range(1,5):
#     if precios[x] > precios[0]:
#         contador_mayores+= 1
# print(f"La cantidad de productos con un precio mayor al primer producto ingresado es: {contador_mayores}")

# -------------------------------------------------------------------------------------------
# 10- En un curso de 4 alumnos se registraron las notas de sus exámenes y
# se deben procesar de acuerdo a lo siguiente:
# a) Ingresar nombre y nota de cada alumno (almacenar los datos en dos listas
# paralelas)
# b) Realizar un listado que muestre los nombres, notas y condición del
# alumno. En la condición, colocar "Muy Bueno" si la nota es mayor o igual a
# 8, "Bueno" si la nota está entre 4 y 7, y colocar "Insuficiente" si la
# nota es inferior a 4.
# c) Imprimir cuantos alumnos tienen la leyenda “Muy Bueno”

# nombres = []
# notas = []
# cont_mb = 0

# for x in range(4):
#     nombre = input("Ingrese nombre: ")
#     nota = float(input("Ingrese su nota: "))
#     nombres.append(nombre)
#     notas.append(nota)

# for x in range(4):
#     if notas[x] >= 8:
#         print(f"Alumno: {nombres[x]} - Nota: {notas[x]} - Condicion: Muy bueno")
#         cont_mb += 1
#     elif notas[x] <= 7 and notas[x] >= 4:
#         print(f"Alumno: {nombres[x]} - Nota: {notas[x]} - Condicion: Bueno")
#     else:
#         print(f"Alumno: {nombres[x]} - Nota: {notas[x]} - Condicion: Insuficiente")

# print(f"Cantidad de alumnos con calificacion muy buena: {cont_mb}")

# -------------------------------------------------------------------------------------------
# 11- Realizar un programa que pida la carga de dos listas numéricas enteras
# de 4 elementos cada una. Generar una tercer lista que surja de la suma de
# los elementos de la misma posición de cada lista. Mostrar esta tercer lista.

# lista1 = []
# lista2 = []
# lista_total = []

# print("Carga lista uno")
# for x in range(4):
#     valor = int(input("Ingrese un numero entero: "))
#     lista1.append(valor)

# print("Carga lista dos")
# for x in range(4):
#     valor = int(input("Ingrese un numero entero: "))
#     lista2.append(valor)

# print("Generamos 3er lista con la suma de las dos anteriores")
# for x in range(4):
#     suma = lista1[x] + lista2[x]
#     lista_total.append(suma)

# print(f"Mostramos 3er lista {lista_total}")

# -------------------------------------------------------------------------------------------
# ORDENAMIENTO DE LISTAS
# 12- Crear una lista y almacenar los nombres de 5 países.
# Ordenar alfabéticamente la lista e imprimirla
# paises = []
# for x in range(5):
#     nombre = input("Ingrese el nombre del pais: ")
#     paises.append(nombre)
# print(f"Paises sin orden alfabetico: {paises}")
# paises.sort()
# print(f"Paises ordenados alfabeticamente: {paises}")

# -------------------------------------------------------------------------------------------
# 13- Solicitar por teclado la cantidad de empleados que tiene la empresa.
# Crear y cargar una lista con todos los sueldos de dichos empleados.
# Imprimir la lista de sueldos ordenamos de menor a mayor
cantidad_empleados = int(input("Ingrese cantidad de empleados: "))
sueldos = []

for x in range(cantidad_empleados):
    sueldo = int(input("Ingrese su sueldo: "))
    sueldos.append(sueldo)
    
print(f"Lista desordenada: {sueldos}")
# 2. Algoritmo de Burbuja para ordenar
# El ciclo externo recorre la lista varias veces
for i in range(len(sueldos)):
    # El ciclo interno compara elementos vecinos
    for j in range(len(sueldos) - 1):
        if sueldos[j] > sueldos[j + 1]:
            # Intercambio de valores (swap)
            aux = sueldos[j]
            sueldos[j] = sueldos[j + 1]
            sueldos[j + 1] = aux
            # print(sueldos)

print("Los sueldos ordenados de menor a mayor son:", sueldos)




