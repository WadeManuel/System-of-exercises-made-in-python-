#Ordenando un arregelo por el metodo de insersción
arr=[32,4,324,56,5,6,5,7,34,5,34,3,5,345,54,6,45,6,56,54,5334,34,4,324,32,4,32,4,324,2,3,24,32] #1


for j in range(1,len(arr)):
    actual = arr[j]

    i=j-1
    while i>=0 and arr[i] > actual:
        arr[i+1]=arr[i]
        i-=1
    arr[i+1]=actual
print(arr)


arr_monedas=[1,10,50,25,100,1,1,1,50,]




def voraz(arr_monedas,monto):
    resto=monto
    contador=0
    while resto>0:
        moneda=max(arr_monedas)
        resto-=moneda
        if resto<0:
            arr_monedas.remove(moneda)
            resto = monto
        else:
            contador += 1


    return contador

print(voraz(arr_monedas,28))


def esPrimo(n):
    contador=0
    i=1
    while i<=n:
        if n%i==0:
            contador +=1
        i+=1
    return contador==2

print(esPrimo(5))












