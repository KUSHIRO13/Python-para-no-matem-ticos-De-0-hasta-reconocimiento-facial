# Bucle while
import math

numero = 0

while numero < 20:
    numero += 1
    print(numero)

num1 = int(input("Ingrese un numero: "))

while num1 < 0:
    print("Por Favor ingrese un numero positivo")
    num1 = int(input("vuela a ingresar: "))
print(f"El resultado de la raiz cuadrada es: {math.sqrt(num1):.2f}")

