"""
Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a
cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40
minutos.
"""
import  math


def cantidad_horas(horas):
    hour=math.floor(cantidad_minutos / 60)
    return  hour
cantidad_minutos=int(input("Digite la cantidad de minutos"))

hour = cantidad_horas(cantidad_minutos)
minutos= cantidad_minutos - hour * 60


print(f"{cantidad_minutos} minutos son {hour} horas y {minutos}  minutos")