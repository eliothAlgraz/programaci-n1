while True:
    print("quieres conocer tu destino? si/no")
    print("1. si")
    print("2. no")
    opcion =  int(input("indique su respuesta con los numeros:"))
    if (opcion == 2 ):
        print("usted escogio no conocer su destino")
        break

    nombre = input("indique su nombre:\n")
    año_nacimiento = int(input("indique su año de nacimiento:\n"))
    numero_suerte = int(input("idique su numero de la suerte del 1 al 4 :\n"))
    año_actual = 2025
    def edad(año_actual  ,año_nacimiento):
         return año_actual - año_nacimiento
    edad1 = edad(año_actual, año_nacimiento)    
    print(f"tu edad es de: {edad1}")
    numero_sod=print(f"tu signo sodiacal es el numero: {año_nacimiento%10}")
    
while True:
    print("quieres conocer tu elemento?")
    print("1.si")
    print("2.no")
    opcion1 = int(input("indique su respuesta con numero 1 para indicar 'si' o 2 para indicar 'no' "))
    if (opcion1 == 2):
         print("ok, usted no quiere conocer su elemnto ")
         break
    
    int(input("indique su numero sodiacal para saber su elemento:\n"))

    if (numero_sod == 0,1):
          print("tu elemento es el metal")
    elif (numero_sod == 2,3):
          print("tuelemnto es el agua")
    elif (numero_sod == 4,5):
          print("tu elemento es la madera")
    elif (numero_sod == 6,7):
         print("tu elemento es el fuego")

