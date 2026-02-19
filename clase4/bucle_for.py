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
# n = int(input("Cantidad de triangulos a ingresar: ")) agregue n para cantidad de veces
# for x in range(n):
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




# -------------------------------------------------------------------------------------------

# 7- Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
# a) La cantidad de valores ingresados negativos.
# b) La cantidad de valores ingresados positivos.
# c) La cantidad de múltiplos de 15.
# d) El valor acumulado de los números ingresados que son pares.
# valores_negativos = 0
# valores_positivos = 0
# cant_multiplos = 0
# valor_acu_pares = 0
# for x in range(5):
#     valor = int(input("Ingrese un valor entero: "))
#     if valor < 0:
#         valores_negativos +=1
#     elif valor > 0:
#         valores_positivos +=1

#     if valor % 15 == 0 and valor != 0:
#         cant_multiplos +=1

#     if valor % 2 == 0 and valor != 0:
#         valor_acu_pares += valor   
# print(f"La cantidad de valores ingresados negativos es : {valores_negativos}") 
# print(f"La cantidad de valores ingresados positivos es : {valores_positivos}")
# print(f"La cantidad de multiplos de 15 es: {cant_multiplos}") 
# print(f"El valor acumulado de los números ingresados que son pares es : {valor_acu_pares}")
#SOLUCION GEMINI
# # Inicializamos los contadores y el acumulador en 0
# negativos = 0
# positivos = 0
# multiplos_15 = 0
# suma_pares = 0

# print("Ingrese 10 valores enteros:")

# # Usamos un bucle para pedir los 10 números
# for i in range(10):
#     valor = int(input(f"Ingrese el valor {i+1}: "))
    
#     # a) y b) Clasificar si es negativo o positivo
#     if valor < 0:
#         negativos += 1
#     elif valor > 0:
#         positivos += 1
#     # Nota: El 0 no es ni positivo ni negativo, por eso usamos elif
        
#     # c) Cantidad de múltiplos de 15
#     # Usamos el operador % (módulo) que devuelve el resto de la división
#     if valor % 15 == 0 and valor != 0:
#         multiplos_15 += 1
        
#     # d) Valor acumulado de los números pares
#     if valor % 2 == 0:
#         suma_pares += valor

# # --- Impresión de resultados ---
# print("\n--- RESULTADOS ---")
# print(f"Cantidad de valores negativos: {negativos}")
# print(f"Cantidad de valores positivos: {positivos}")
# print(f"Cantidad de múltiplos de 15: {multiplos_15}")
# print(f"Suma total de los números pares: {suma_pares}")





# -------------------------------------------------------------------------------------------

# 8- Se cuenta con la siguiente información:
# Las edades de 5 estudiantes del turno mañana.
# Las edades de 6 estudiantes del turno tarde.
# Las edades de 11 estudiantes del turno noche.
# Las edades de cada estudiante deben ingresarse por teclado.
# a) Obtener el promedio de las edades de cada turno (tres promedios)
# b) Imprimir dichos promedios (promedio de cada turno)
# c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un
# promedio de edades mayor.

# promedio_turno_manana = 0
# promedio_turno_tarde = 0
# promedio_turno_noche = 0
# corte_turno_manana = 0
# corte_turno_tarde = 0
# corte_turno_noche = 0

# for x in range(22):
#     turno = input("Ingrese su turno: ")
#     edad = int(input("Ingrese su edad: "))
#     turno = turno.capitalize()
#     if turno == "Manana" and corte_turno_manana < 6:
#         corte_turno_manana +=1
#         promedio_turno_manana += edad
#     elif turno == "Tarde" and corte_turno_tarde < 7:
#         corte_turno_tarde +=1
#         promedio_turno_tarde += edad
#     elif turno == "Noche" and corte_turno_noche < 12:
#         corte_turno_noche +=1
#         promedio_turno_noche += edad

# prom_final_m = promedio_turno_manana / 5
# prom_final_t = promedio_turno_tarde / 6
# prom_final_n = promedio_turno_noche / 11

# if prom_final_m > prom_final_t and prom_final_m > prom_final_n:
#     promedio_final_mayor = "Turno manana"
# elif prom_final_t > prom_final_m and prom_final_t > prom_final_n:
#     promedio_final_mayor = "Turno tarde"
# elif prom_final_n > prom_final_m and prom_final_n > prom_final_t:
#     promedio_final_mayor = "Turno noche"

# print(f"Promedio de edad turno manana: {prom_final_m}")
# print(f"Promedio de edad turno tarde: {prom_final_t}")
# print(f"Promedio de edad turno noche: {prom_final_n}")
# print(f"El turno con mayor promedio de edad es: {promedio_final_mayor}")

# SOLUCION GEMINI
# # --- TURNO MAÑANA (5 estudiantes) ---
# suma_manana = 0
# print("Ingrese las edades del Turno Mañana:")
# for i in range(5):
#     edad = int(input(f"Edad estudiante {i+1}: "))
#     suma_manana += edad
# promedio_manana = suma_manana / 5

# # --- TURNO TARDE (6 estudiantes) ---
# suma_tarde = 0
# print("\nIngrese las edades del Turno Tarde:")
# for i in range(6):
#     edad = int(input(f"Edad estudiante {i+1}: "))
#     suma_tarde += edad
# promedio_tarde = suma_tarde / 6

# # --- TURNO NOCHE (11 estudiantes) ---
# suma_noche = 0
# print("\nIngrese las edades del Turno Noche:")
# for i in range(11):
#     edad = int(input(f"Edad estudiante {i+1}: "))
#     suma_noche += edad
# promedio_noche = suma_noche / 11

# # --- IMPRESIÓN DE RESULTADOS ---
# print("\n--- RESULTADOS DE PROMEDIOS ---")
# print("Promedio Mañana:", promedio_manana)
# print("Promedio Tarde:", promedio_tarde)
# print("Promedio Noche:", promedio_noche)

# # --- COMPARACIÓN ---
# if promedio_manana > promedio_tarde and promedio_manana > promedio_noche:
#     print("\nEl turno con el promedio mayor es: MAÑANA")
# elif promedio_tarde > promedio_manana and promedio_tarde > promedio_noche:
#     print("\nEl turno con el promedio mayor es: TARDE")
# else:
#     print("\nEl turno con el promedio mayor es: NOCHE")

    

