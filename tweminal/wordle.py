import random
palablras = ("abeto","actor","aguas","agudo","alado","verde", "altar","avion")

while True:
    palabra = palablras[random.randint(0,len(palablras)-1)]
    wordle = list(palabra)
    print("""\033[3;34;46m
===================================[wordle]===========================================
    bienvenido ya he elegido la palabra secreta. tienes 5 intentos para adivinar 
======================================================================================\033[0;30;m""")
    

    for i in range(5):
        intento = input("ingrese una palabra de 5 letras sin acentos.\n").lower()[:5]
        indice = 0
        resultado = ""
        correctas = 0
        for letra in intento:
            if letra == wordle[indice]:
                correctas +=1
                resultado += "\033[1;32m"+letra+"\033[0;30m"
            elif letra in wordle:
                resultado += "\033[1;33m"+letra+"\033[0;30m"
            else:
                resultado += "\033[1;31m"+letra+"\033[0;30m"
            indice+=1
        print(resultado)
        if correctas == 5:
            break
    if correctas == 5:
        print(f"felicidades la palabra era \033[1;32m{palabra}\033[0;30m has acertado.")
    else:
        print(f"lo siento has fallado. la palabra era: \033[1;31{palabra}\033[0;30")

    opcion = input("desea jugar otra vez? (si/no)").lower()
    if opcion == "no":
        break

