import random

num2=int(input("Digite un numero hasta que acerte"))


lista = []
lista.append(num2)

for i in lista:
    num2 = int(input("Digite un numero hasta que acerte"))
    numero_aletorio = random.randint(1, 1000)
    mayor = False
    menor = False
    if numero_aletorio >= 500:
        print("Es mayor")
        mayor = True
    else:
        print("Es menor")
        menor = True
    lista.append(num2)
    print(lista)
    if num2 > i and mayor==True :
        print("Ha acertado la respuesta correcta")
        break
    elif num2 < i and menor==True:
        print("Ha acertado la respuesta correcta")
        break








