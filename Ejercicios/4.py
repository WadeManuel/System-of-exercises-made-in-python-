""""
Escribir un programa que dados dos números, realice y muestre la suma, resta, división
y multiplicación de ambos
"""

num1=int(input("Digite el primer numero"))
num2=int(input("Digite el segundo numero"))
print(""""
-----Menu-Opciones---
1-Suma\n
2-Resta\n
3-Multiplicación\n
4-División\n
5-Salir
"""
"")

opcion=int(input("Digite una opción"))



if(opcion==1):
    num1 += num2
    print(f"El resultado de la suma es {num1}")
elif(opcion==2):
    num1 -=num2
    print(f"El resultado de resta es {num1}")
elif(opcion==3):
    num1 *=num2
    print(f"El resulta de la multiplicación es {num1}")
elif(opcion==4):
    num1 /= num2
    print(f"El resultado de la división es {num1}")
elif(opcion==5):
    print("Ha salido del menú")
elif(opcion>5):
    print("Error no ninguna opción con ese numero")


