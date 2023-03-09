# Repetir hasta que se te acabe la plata
"""
saldo = 2000

print(f"Tienes ${saldo} en tu cuenta")

while saldo >= 0:
    gasto = int(input("Cuanto quieres gastar?: "))
    saldo = saldo - gasto
    print(f"te quedan {saldo}")
    if saldo <= 0:
        break
"""
saldo = 2000

while True:
    seleccion = int(input("""
1. Ingreso de dinero
2. Retiro de dinero
3. Mostrar dinero
4. Salir

Elija un opcion: """))
    if seleccion == 1:
        ingreso = int(input("Cuanto deseas ingresar?: "))
        saldo += ingreso
        print(f"Tienes en la cuenta ${saldo} pesos actualmente")
    elif seleccion == 2:
        retiro = int(input("Cuanto deseas retirar?: "))
        saldo -= retiro
        print(f"Te queda ${saldo} pesos en la cuenta")
    elif seleccion == 3:
        print(f"En la cuenta tienes ${saldo}")
    elif seleccion == 4:
        print("Cerrando el programa")
        break
    else:
        print("Valor invalido vuelva a elegir")
