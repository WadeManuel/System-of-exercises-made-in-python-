"""
 Escribe un programa que lea una cadena y devuelva un diccionario con la
cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si
recibe “Qué lindo día que hace hoy” debe devolver: ‘que’: 2, ‘lindo’: 1, ‘día’:
1, ‘hace’: 1, ‘hoy’: 1
"""



def contarpalabrasdicionario(cadena):
    # Dividiendo la frase en palabras
    palabras=cadena.split()
    #Creando un diccionario para contar las palabras que se repiten
    diccionario_palabras={}
    for palabra in palabras:
        #Eliminado signos de puntuación al final de la palabra
        palabra=palabra.strip('.,!?:;"')
        palabra=palabra.lower()
        if palabra in diccionario_palabras:
            #Agregando al diccionarios la palabras si la palabra esta se incrementa su valor
            diccionario_palabras[palabra]+=1
        else:
            diccionario_palabras[palabra]=1
    return  diccionario_palabras

cadena=input("Digite una cadena de texto")

dicionario=contarpalabrasdicionario(cadena)
print(dicionario)

try:
    elimina=str(input("Elimina una palabra de la frase anterior"))
    palabra_sin_espaciados="".join(elimina.split())
    del (dicionario[palabra_sin_espaciados])
    print(f"La palabra {palabra_sin_espaciados} ha sido eliminada del diccionario\n")
    print(dicionario)
except:
    print("La palabra a eliminar no existe")
finally:
    print("Profe he culminado el ejercico correctamente")

