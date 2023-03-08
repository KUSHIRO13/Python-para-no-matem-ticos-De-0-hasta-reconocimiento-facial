#Decir cual es mayor
n1 = int(input("Escriba el numero 1: "))
n2 = int(input("Escriba el numero 2 "))
n3 = int(input("Escriba el numero 3: "))

if n1 >= n2 and n1 >= n3:
    print(f"El numero {n1} es mayor")
elif n2 >= n1 and n2 >= n3:
    print(f"El numero {n2} es mayor")
else:
    print(f"El numero {n3} es mayor")