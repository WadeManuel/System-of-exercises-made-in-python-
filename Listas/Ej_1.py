"Escriba un programa que permita leet por teclado numeros y guardarlos en una lista "
#El proceso finaliza cunado se intruduza numero negativo .Mostrar el máximo de los numero guardados en la lista
#y los numeros pares

num = int(input("Digite un numero para guardarlos en la lista "))
list=[num]
while num>0:
    num = int(input("Digite un numero para guardarlos en la lista "))
    list.append(num)

print(list)
print(f"La cantidad de numero guardados es {len(list)}")

#Funcion para saber si un numero es par
def espar(n):
    return n%2==0

listapares=[]
for i in list:
    if (espar(i)):
        listapares.append(i)
print(f"Los numero pares dentro de la lista son {listapares}")


