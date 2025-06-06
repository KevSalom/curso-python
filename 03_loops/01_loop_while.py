###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###

# print("\n Bucle while:")

# # Bucle con una simple condición
# contador = 0

# while contador <= 5:
#   print(contador)
#   contador += 1 # es super importante para evitar un bucle infinito

# # utilizando la palabra break, para romper el bucle
# print("\n Bucle while con break:")
# contador = 0

# while True:
#   print(contador)
#   contador += 1
#   if contador == 5:
#     break # sale del bucle

# # continue, que lo hace es saltar esa iteración en concreto
# # y continuar con el bucle
# print("\n Bucle con continue")
# contador = 0
# while contador < 10:
#   contador += 1

#   if contador % 2 == 0:
#     continue

#   print(contador)

# # else, esta condición cuando se ejecuta?
# print("\n Bucle while con else:")
# contador = 0
# while contador < 5:
#   print(contador)
#   contador += 1
# else:
#   print("El bucle ha terminado")

# # else, esta condición cuando se ejecuta?
# print("\n Bucle while con else:")
# contador = 0
# while contador < 5:
#   print(contador)
#   contador += 1
# else:
#   print("El bucle ha terminado")

# # pedirle al usuario un número que tiene
# # que ser positivo si no, no le dejamos en paz
# numero = -1
# while numero < 0:
#   numero = int(input("Escribe un número positivo: "))
#   if numero < 0:
#     print("El número debe ser positivo. Intenta otra vez, majo o maja.")

# print(f"El número que has introducido es {numero}")

# numero = -1
# while numero < 0:
#   try:
#     numero = int(input("Escribe un número positivo: "))
#     if numero < 0:
#       print("El número debe ser positivo. Intenta otra vez, majo o maja.")
#   except:
#     print("Lo que introduces debe ser un número, que si no peta!")

# print(f"El número que has introducido es {numero}")

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
# print("\nEjercicio 1:")
# numero = 10

# while numero >= 1:
#   print(f"numero {numero}")
#   numero -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
# print("\nEjercicio 2:")
# suma = 0
# numero = 1
# while numero <= 20:
#   if numero % 2 == 0:
#     suma += numero
#   numero += 1
# print(f"La suma es: {suma}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
# print("\nEjercicio 3:") 

# try:
#   numero = int(input("Introduce un numero entero positivo: "))  
#   if numero < 0:
#     print("El número debe ser positivo. Intenta otra vez, majo o maja.")
# except:
#     print("Lo que introduces debe ser un número, que si no peta!")

# contador = 1
# factorial = 1

# while contador <= numero:
#   factorial *= contador
#   contador += 1

# print(f"El factorial de {numero} es {factorial}")



# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
# print("\nEjercicio 4:")

# is_valid_password = False

# while not is_valid_password:
#   password = input("Introduce una contraseña: ")
#   if not len(password) >= 8:
#     continue
#   is_valid_password = True

# print(f"Perfecto! Tu contraseña es {password} y es muy segura")



# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
# print("\nEjercicio 5:")

# numero = int(input("Introduce un numero: "))
# multiplicador = 1
# while contador <= 10:
#   print(f"{numero} x {multiplicador}= {numero * multiplicador}")
#   contador+= 1


# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.55
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")

n = int(input("Introduce un numero positivo: "))

numero = 2
while numero <= n:
  divisor = 2
  es_primo = True
  while divisor * divisor <= numero :
    if numero % divisor == 0:
      es_primo = False
      break
    divisor+=1
  if es_primo : print(f"{numero} es un numero primo")
  numero+=1
