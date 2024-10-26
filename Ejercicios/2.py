"""
    . Escribir un programa que permita calcular el perímetro y área de un rectángulo. Primero
deberá solicitar los valores de la base y altura al usuario.
"""

base =int(input("Digite la base del rectángulo"))
altura=int(input("Digite la altura del rectángulo"))

def perimetro_rectángulo(l,w):
    perimetro=2*l + 2 * w
    return  perimetro

area=lambda l,w : l*w

print(f" El perímetro {perimetro_rectángulo(altura,base)}  y el área {area(altura,base)} de el rectángulo")


