
ano=int(input("Digite un año para saber si es bisiesto o no"))

def es_bisiesto(ano):
    if(ano%4==0 and ano%100 !=0 or ano%400==0):
        return True
    else:
        return False

if(es_bisiesto(ano)==True):
    print(f"El año {ano} es bisiesto")
else:
    print(f"El año {ano}no lo es")
