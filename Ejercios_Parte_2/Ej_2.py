
"""Crear un programa  que solicite una frase por teclado y muestre la siguiente info
1-La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.
2 -Dicha cadena con la primera letra de cada palabra en mayúsculas. Por
ejemplo, si recibe república argentina debe devolver República Argentina.
Las palabras que comiencen con la letra A. Por ejemplo, si recibe
Antes de ayer debe devolver Antes ayer.
"""
frase = str(input("Digite una frase por teclado"))
def depilarmayuscula(cadena):
    pila = [""]
    fraselista=list(cadena)
    for i in fraselista:
        pila.append(i)
        nuevalista=[]
    for caracter in pila:
        if caracter.isupper():
            nuevalista.append(caracter)

    return nuevalista

frase1="".join(depilarmayuscula(frase))
print(f"{frase1}")

#Inc2

cadena = input("Digite una frase que contega mas de dos palabras en minuscula todo")
#word.capitalize() se utiliza para convertir la primera letra de una palabra en mayúsculas
# y el resto en minúscula
nueva_frase=''.join(word.capitalize() for word in cadena.split())
print(nueva_frase)

#Inc3

cadena_palabras = input("Digite una frase que contega palabras con a\n")
lista10=[]
for palabra in cadena_palabras.split():
    #Me agrega a la lista las palabras que contegan la letra a al inicio p
    if palabra.lower().startswith('a'):
        lista10.append(palabra)

#Convertir la lista en una frase
nueva_frase1="".join(lista10)
print(nueva_frase1)











