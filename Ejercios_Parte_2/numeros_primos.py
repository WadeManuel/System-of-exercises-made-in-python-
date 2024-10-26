#Intrudusca un numero decir si es primo o no es primo


def esprimo(n):
    contDiv=0
    i=1
    while i<=n:
        if (n%i==0):
            contDiv +=1
        i+=1
    return contDiv == 2


i=1
lista=[]
while i<=1000:
    if esprimo(i):
        lista.append(i)
    i+=1
print(lista)