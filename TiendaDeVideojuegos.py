info_tienda= {
    'eslogan': 'Game On!',
    'Año de fundación': 2010
}
print(f"{info_tienda}")
print("Este es el catalogo de juegos:")
inv_juegos= {
    "Spiderman 2" :{"precio":999,"stock":20},
    "Minecraft" :{"precio":40,"stock": 22},
    "pac-mac" :{"precio":50,"stcok": 25},
     }
print(inv_juegos)
while True:
    opcion= input("quiere comprar un juego? si/no:\n").lower()
    if (opcion == "no"):
        print("gracias por su visita ")
        break
    elif (opcion == "si"):
        opcion = input("que jeugo desea comprar:\n ") 

    