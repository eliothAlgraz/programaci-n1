print("asistente de decisiones del dia")
print("indique el dia con los numeros asignados")
dia = int(input("""
1.lunes
2.martes
3.miercoles
4.jueves
5.viernes
6.sabado
7.domingo
"""))

print("indique el clima del dia")
clima = int(input("""
1. soleado
2. nublado
3. lloviendo 
"""))

match dia:
    case 1:
        print("el primer dia de la semana. " + " es lunes")

        if(clima == 1):{
            print("se recomienda utilizar bloqueador ")
        }
        
        if(clima == 2):{
            print("buen dia para caminar ")
        }
        if(clima == 3):{
            print("se recomienda no salir de casa")
        }
    case 2: 
        print("segundo dia de la semana ya casi." + " es martes")
        
        if(clima == 1):{
            print("se recomienda utilizar bloqueador ")
        }
        
        if(clima == 2):{
            print("buen dia para caminar ")
        }
        if(clima == 3):{
            print("se recomienda no salir de casa")
        }
    case 3:
        print("mitad de sama, sigue asi." + "es miercoles ")
        
        
        if(clima == 1):{
            print("se recomienda utilizar bloqueador ")
        }
        
        if(clima == 2):{
            print("buen clima para salir a caminar")
        }
        if(clima == 3):{
            print("se recomienda no salir de casa, disfruta del sonido de la lluvia")
        }
    case 4:
        print("faltan dos dia para terminar la semana." + "es jueves")

        if(clima == 1):{
            print("utiliza bloqueador, puedes apreciar la vista ")
        }
        
        if(clima == 2):{
            print("buen clima para salir a correr")
        }
        if(clima == 3):{
            print("recomendacion no salir y disfrutar la vista de la lluvia")
        }
    
    case 5:
        print("ultimo dia de trabajo bien echo." + "es viernes")

        if(clima == 1):{
            print("utilice bloqueador, hace un buen dia para tomar algo bien frio")
        }
        
        if(clima == 2):{
            print("buen clima para salir a caminar con compañia")
        }
        if(clima == 3):{
            print("se recomienda no salir de casa y ver una maraton de peliculas acompañado ")
        }
    
    case 6:
        print("fin de semana bien echo." + "es viernes")

        if(clima == 1):{
            print("si va a la playa apliquese bloqueador ")
        }
        
        if(clima == 2):{
            print("buen clima para salir con amigos ")
        }
        if(clima == 3):{
            print("buen clima para apreciar el paisaje")
        }
            
    case 7:
        print("fin de semana." + "es domingo")

        if(clima == 1):{
            print("buen dia para salir a la playa")
        }
        
        if(clima == 2):{
            print("buen clima para salir con amigo a tomar algo")
        }
        if(clima == 3):{
            print("se recomienda no salir de casa, dia de maraton de peliculas acompañado")
        }