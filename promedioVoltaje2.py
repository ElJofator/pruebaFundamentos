suma = 0
cantidad = 3
for i in range(cantidad):
    suma += float(input(f"Ingrese el voltaje {i+1}: "))
promedio = suma/cantidad
if(promedio <= 115):
    print("VOLTAJE CORRECTO")
elif(115 < promedio < 220):
    print("ALTO VOLTAJE")
else:
    print("PELIGRO")