#Ingrese valores
valor1 = int(input("Ingrese el primer numero: "))
valor2 = int(input("Ingrese el segundo numero: "))

if valor1 % 2 == 0 and valor2 %2 == 0:
    print("Ambos numeros son pares")
elif valor1 % 2== 0 and valor2 %2 != 0:
    print(f"El numero {valor1} es par y el {valor2} no lo es")
elif valor1 % 2!= 0 and valor2 %2 == 0:
    print(f"El numero {valor1} es impar y el {valor2} si es par")
else:
    print(f"Ninguno es par")