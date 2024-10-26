def validar_campos(n:str,c:str):
      return  len(nombre) >= 4 and len(contraseña) >= 8

nombre = str(input("Digita un nombre de usario"))
contraseña = str(input("Digita la contraseña"))
respuesta = validar_campos(nombre,contraseña)

if validar_campos(nombre,contraseña)==True:
    print("Creedencias correctas")
else:
    print("Creedencias incorrectas")












