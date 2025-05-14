###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# print("\nEjercicio 1:")
# num1 = int(input("Introduce el primer número: "))
# num2 = int(input("Introduce el segundo número: "))

# numMayor = num1 if num1 > num2 else num2
# print(f"El número mayor es: {numMayor}")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)
# print("\nEjercicio 2:")
# num1 = float(input("Introduce el primer número: "))
# num2 = float(input("Introduce el segundo número: "))
# operacion = input("Introduce la operación (+, -, *, /): ")

# if operacion == "+":
#     resultado = num1 + num2
# elif operacion == "-":
#     resultado = num1 - num2
# elif operacion == "*":
#     resultado = num1 * num2
# elif resultado == "/":
#     if num2 != 0:
#         resultado = num1 / num2
#     else:
#         print("Error: No se puede dividir entre cero wey...")
# else:
#     print("Error: Operacion no valida")

# if 'resultado' in locals(): #Comprueba si la variable resultado existe.
#     print(f"El resultado es: {resultado}")
  

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# print("\nEjercicio 3:")

# userYear = int(input("Introduce un año"))

# if (userYear % 4 == 0 and userYear % 100) or userYear % 400:
#     print(f"El año {userYear} es un año bisiesto")
# else:
#     print(f"El año {userYear} es NO un año bisiesto")



# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

print("\nEjercicio 4:")
edad = int(input("Introduce una edad: "))

if 0 <= edad <= 2
    print("Eres un bebé")
elif edad <= 12:
    print("Eres un niño")
elif edad <= 17:
    print("Eres un Adolescente")
elif edad <= 64:
    print("Eres un Adulto")
else:
    print("Seguro ya eres Abuelito")