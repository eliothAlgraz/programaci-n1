import random
print("bienvenido a la bola magica")
while True:
    opcion=input("desea realizar una pregunta al a bola ocho? Si/No:\n").lower()
    if (opcion == "no" ):
        print("gracias, vuelve pronto")
        break
    if (opcion == "si"):
        input("cual es tu pregunta para la bola magica?:\n")
    dado = random.randint(1,20)
    if dado == 1:
        print("Es cierto")
    elif dado == 2:
        print("Es decididamente asi")
    elif dado == 3:
        print("Sin lugar a dudas.")
    elif dado == 4:
        print(" Sí, definitivamente.")
    elif dado == 5:
        print(" Puedes confiar en ello.")
    elif dado == 6:
        print(" Como yo lo veo, sí.")
    elif dado == 7:
        print("Lo más probable.")
    elif dado == 8:
        print("Perspectiva buena.")
    elif dado == 9:
        print(" Sí.")
    elif dado == 10:
        print("Las señales apuntan a que sí.")
    elif dado == 11:
        print("Respuesta confusa, vuelve a intentarlo.")
    elif dado == 12:
        print("Vuelve a preguntar más tarde.")
    elif dado == 13:
        print("Mejor no decirte ahora.")
    elif dado == 14:
        print("No se puede predecir ahora.")
    elif dado == 15:
        print("Concéntrate y vuelve a preguntar.")
    elif dado == 16:
        print("No cuentes con ello ")
    elif dado == 17:
        print("Mi respuesta es no.")
    elif dado == 18:
        print("Mis fuentes dicen que no.")
    elif dado == 19:
        print("Las perspectivas no son muy buenas.")
    elif dado == 20:
        print("Muy dudoso.")
