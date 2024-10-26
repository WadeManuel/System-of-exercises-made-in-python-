
lista=[3,1,4,1,2]
cont = 0
j= 0
i = 0
min =0

#Lo que hice para resolver este ejercico fue ordena la lista por Selección
while i<5:
    min =i
    j = i + 1
    while j<5:
        if lista[j] < lista[min]:
            min = j
# Que si el contador se incremneta es que a ocurrido un cambio por que la lista estaba desordenada
            cont +=1
        j +=1
    lista[i] , lista[min] = lista[min] , lista[i]
    i +=1

print(f" La cantdida de veces que intercambio para orden la lista fue {cont} veces por tanto")
if cont>=1:
    print("Mi lista estaba desordena")
else:
    print("Mi lista estaba ordena")
print("Mi nueva lista ordena en forma ascendente es")
print(lista)














