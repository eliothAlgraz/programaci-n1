while True:
    print("\n-calculadora")
    print("escoja la operacion que desea realizar")
    print("1. sumar 2 numeros")
    print("2. restar 2 numeros")
    print("3. multiplicar 2 numeros")
    print("4. dividir 2 numero")
    print("5. salir")

    opcion= int(input("elige una operaciondel 1 al 5: "))

    if (opcion == 5):
        print("usted a salido de la calculadora")
        break

    elif (opcion == 1):
        num1= float(input("introduce tu primer numero: "))
        num2= float(input("introduce tu segundo numeor: "))
        resultado = num1 + num2
        print(f"el resultado de la suma es: {resultado}")
    
    elif (opcion == 2):
        num1= float(input("introduce tu primer numero: "))
        num2= float(input("introduce tu segundo numeor: "))
        resultado = num1 - num2
        print(f"el resultado de la resta es: {resultado}")

    elif (opcion == 3):
        num1 = float(input("introduc tu primer nuemro: "))
        num2 = float(input("introduce tu segundo numero: "))
        resultado = num1 * num2
        print(f"el resultado de la multiplicacion es: {resultado}")
    
    elif (opcion == 4):
        num1= float(input("introduce tu primer numero: "))
        num2= float(input("introduce tu segundo numero: "))
        resultado= num1/num2
        print(f"el resultao de su division es: {resultado}")