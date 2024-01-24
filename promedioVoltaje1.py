suma = 0
cantidad = 5
for i in range(cantidad):
    suma += float(input(f"Ingrese el voltaje {i+1}: "))
promedio = suma/cantidad
if(promedio >= 220):
    print("ALTO VOLTAJE")
else:
    print("VOLTAJE CORRECTO")