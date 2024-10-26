#Escriba un programa que muestre la tabla de multiplicar de los numero 1,2,3,4,5

num1=1
num2=2
num3=3
num4=4
num5=5

def tablamultiplicar(n):
    i=1
    resultado=0
    while i<=10:
        resultado=n *  i
        print(f"{n} * {i} = {resultado}")
        i+=1

print("Tabla de multilplicar del 1 al 5")
print(tablamultiplicar(num1))
print(tablamultiplicar(num2))
print(tablamultiplicar(num3))
print(tablamultiplicar(num4))
print(tablamultiplicar(num5))
