"""
Calcular el perímetro y área de un círculo. Primero deberá solicitar el valor del radio al
usuario.
"""
import math
radio=float(input("Digite el valor del radio"))


perimetro=2 * math.pi * radio
area=math.pi * radio**2

print(f"El perimetro del circulo es {perimetro:.2f}")
print(f"El área del circulo {area:.2f}")
