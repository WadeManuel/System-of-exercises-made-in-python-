
#Escribe un programa que pida un numero entero , entre uno y doce , e imprima el número
#y la cantidad de días que tiene el mes al que corresponde el numero introduzido .

print("---Menu de opciones--\n"
      "1-Enero\n"
      "2-Febrero\n"
      "3-Maro\n"
      "4-Abril\n"
      "5-Mayo\n"
      "6-junio\n"
      "7-Julio\n"
      "8-Agosto\n"
      "9-Septiembre\n"
      "10-Octuber\n"
      "11-Noviembre\n"
      "12-Diciembre")
print()
opcion = int(input("Digite una opcion"))
if opcion>=1 and opcion<=12:
    print("El numero esta en rango ")

if  opcion==1:
    print("La cantidad de dias que tiene el mes de enero es 30")
elif opcion==2:
    print("La cantidad de dias que tiene el mes de febreo es 28")
elif opcion==3:
        print("La cantidad de dias que tiene el mes de marzo es 31")
elif opcion==4:
        print("La cantidad de dias que tiene el mes de abril es 30")
elif opcion==5:
        print("La cantidad de dias que tiene el mes de mayo es 31")
elif opcion==6:
        print("La cantidad de dias que tiene el mes de junio es 31")
elif opcion==7:
        print("La cantidad de dias que tiene el mes de julio es 30")
elif opcion==8:
        print("La cantidad de dias que tiene el mes de agosto es 30")
elif opcion==9:
        print("La cantidad de dias que tiene el mes de septiembre es 31")
elif opcion==10:
        print("La cantidad de dias que tiene el mes de Octubre es 31")
elif opcion==11:
        print("La cantidad de dias que tiene el mes de Noviembre es 31")
elif opcion==12:
        print("La cantidad de dias que tiene el mes de Diciembre es 31")
else:
    print("El numero no esta en rango ")