#Librerias
import math
#Obtener el radio

r = float(input("Ingrese el radio para calcular el area: "))

area = math.pi * r**2
longitud = 2*math.pi*r

print(f"El area total es: {round(area,2)}")
print(f"la longitud total es: {round(longitud,2)}")
