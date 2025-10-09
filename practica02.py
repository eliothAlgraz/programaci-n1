#if  else elif 
edad= 25 #int(input("dime tu edad:"))

if edad >= 10 and edad <18:
    print("eres un adolecente.")
elif edad >=18:
    print("eres un adulto.")
else:
    print("todavia eres un niño")



#match 

opcion = int (input("""
1. agregar
2. editar
3. eliminar
4. leer
5. finalizar
"""))

match opcion:
    case 1:
        print("se ha agregado  correctamente.")
    case 2:
        print("se ha modificado correctamente.")
    case 3:
        print("se ha eliminado correctamente.")
    case 4:
        print("el usuario registrado se llama jorge.")
    case 5:
        print("se finalizo el programa.")


