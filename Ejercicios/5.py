"""
 Escribir un programa que le pida una palabra al usuario, para luego imprimirla 1000
veces, con espacios intermedios.

"""


frase=input("Digite una palabra")
i=1
num=1000
while i<=num:
    print(f"{i}-{frase} ")
    i +=1