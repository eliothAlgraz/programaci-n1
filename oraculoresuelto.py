def iniciar_oraculo():
    while True:
        opcion = input("¿deasea conocer tu destino? (si/no):").lower()
        if(opcion == "no" ):
            print("gracias vuelva pronto")
            break
        nombre = input("dame tu nombre: ")
        year = int(input("digita tu año de nacimiento:"))
        numero_suerte = int(input("dime un numero del 1 al 4:"))
        edad = 2025 - year
        elemento = calular_elemento(year)
        prediccion = generara_prediccion(nombre, elemento, numero_suerte)
        decorador = ""
        for i in range(20):
            decorador+= "*"
        print(decorador)
        print("*** oraculo de python ***")
        print(decorador)
        print(prediccion)

def calular_elemento(year):
    match (year%10):
        case 0 | 1: return "metal"
        case 2 | 3: return "agua"
        case 4 | 5: return "madera"
        case 6 | 7: return "fuego"
        case 8 | 9: return "tierra"

def generara_prediccion(nombre,elememto,numero_suerte):
    match numero_suerte:
        case 1: return (f"{nombre}, tu conexion con el elemento {elememto}, te traera gran sabiduria. !es un buen elemento para aprender alo nuevo" )
        case 2: return (f"{nombre}, tu conexion con el elemento {elememto}, te traera gran sabiduria. !es un buen elemento para aprender alo nuevo" )
        case 3: return (f"{nombre}, tu conexion con el elemento {elememto}, te traera gran sabiduria. !es un buen elemento para aprender alo nuevo" )
        case 4: return (f"{nombre}, tu conexion con el elemento {elememto}, te traera gran sabiduria. !es un buen elemento para aprender alo nuevo" )
        case _: return (f"{nombre}, tu conexion con el elemento {elememto}, te traera gran sabiduria. !es un buen elemento para aprender alo nuevo" )

iniciar_oraculo()