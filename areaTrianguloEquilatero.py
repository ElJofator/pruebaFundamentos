lado = float(input("Ingrese el lado del triángulo equilátero: "))
# lado² = (lado/2)² + altura²
# altura² = lado² - (lado/2)²
# altura = sqrt[lado² - (lado/2)²]
altura = (lado**2 - (lado/2)**2)**(1/2)
# area = base*altura/2
area = lado*altura/2
if(area <= 1000):
    print(f"Area: {area}")
else:
    print("DATOS NO VÁLIDOS")