
#Pedir un numero por teclado y mostrar la tabla de multiplicar

num=int(input("Digite un numero para mostrar la tabla de multiplicar de el"))


i=1
resultado = 0
while i<=10:
    resultado = num * i
    print(f" {num} * {i} = {resultado}")
    i +=1