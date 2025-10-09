#examen de programacion de software
print("examen de programacion teorico")
input("nombre completo: ")
input("id: ")

print("1.- ¿cual de los siguientes componentes NO es parte fundamental de la arquitectura de von neumann")
opcion = int(input(""" 
1. tarjeta grafica
2. memoria principal
3. sestema de entrada/salida
4. CPU
"""))

match opcion:
    case 1:
        print("correcto")
    case 2:
        print("incorrecto")
    case 3: 
        print("incorreto")
    case 4: 
        print("incorrecto")

print("2.- El lenguaje maquina esta compuesto por:")
opcion1 = int(input("""
1. simbolos lógicos y matematicos 
2. pseudocódigo 
3. instrucciones en ingles abreviado 
4. código binario 
"""))
match opcion1:
    case 1:
        print("incorrecto")
    case 2:
        print("incorrecto")
    case 3:
        print("incorrecto")
    case 4:
        print("correcto")

print("3.- un lenguaje de programación de alto nivel se caracteriza por: ")
opcion2 = int(input("""
1. ser el mas rapido en tiempo de ejecucion
2. tener un control directo y preciso sobre el hardware
3. ser independiente de la arquitectura de la computadora 
4. ser muy dificil de aprender y leer
"""))
match opcion2:
    case 1:
        print("incorrecto")
    case 2: 
        print("incorrecto")
    case 3:
        print("correcto")
    case 4:
        print("incorrecto")

print("4.-¿que es un algoritmo?")
opcion3 = int(input("""
1. una secuencia de pasos finitos y bien definidos para resolver un problema 
2. un lenguaje de programacion especifico 
3. el codigo fuente de un programa de computadora 
4. un conjunto de instrucciones escritas en codigo
"""))
match opcion3:
    case 1:
        print("correcto")
    case 2:
        print("incorrecto")
    case 3:
        print("incorrecto")
    case 4: 
        print("incorrecto")

print("5.-en psudocodigo, ¿ que estructura de control se utiliza para ejecutar un bloque de cogigo solo si" \
"se cumple una condicion especifica?")
opcion4 = int(input("""
1. repititiva 'mientras'
2. repetitiva 'para'
3. secuencial 
4.condicional o de seleccion 
"""))
match opcion4:
    case 1:
        print("incorrecto")
    case 2:
        print("incorrecto")
    case 3: 
        print("incorrecto")
    case 4:
        print("correcto")

print("6.-el proposito principal del pseudocodigo es:")
opcion5 = int(input("""
1. traducir automaticamente codigo de alto nivel a lengiuaje maquina 
2. planificar y describir la logica de un algoritmo de formalegible para los humanos 
3. ejecutar programas de forma más eficiente que un lenguaje complicado
4. proporcionar un control directo sobre los registros del procesador. 
"""))
match opcion5:
    case 1:
        print("incorrecto")
    case 2: 
        print("correcto")
    case 3: 
        print("incorrecto")
    case 4:
        print("incorrecto")

print("7.- un programa de computadora es esencialmente :")
opcion6 = int(input("""
1. una collecion de algoritmos
2. elsistema operativo de una computadora 
3. un dispositivo de hardware 
4. una secuencia de instrucciones que la computadora ejecuta 
"""))
match opcion6:
    case 1:
        print("incorrecto")
    case 2:
        print("incorrecto")
    case 3:
        print("incorrecto")
    case 4:
        print("correcto")

print("8.-¿cual es la principal diferencia entre bucle'mientras'(while) y un bucle 'repetir'(do-while)?")
opcion7 = int(input("""
1. no hay ninguna diferencia, son intercambiables 
2. el bucle 'repetir' solo usa numeros, mientras que el 'mientras'puedes usar cualquier condicion
3. el bucle 'mientras' es mas rapido que el 'repetir'
4. el bucle 'mientras' puede no ejecutarse, mietras que el 'repetir'se ejecuta al menos una vez
"""))
match opcion7:
    case 1: 
        print("incorrecto")
    case 2:
        print("incorrecto")
    case 3:
        print("incorrecto")
    case 4:
        print("correcto")

print("9.- el lenjguaje ensamblador es considerado un lenguaje de nivel")
opcion8 = int(input("""
1. medio
2. alto
3. bajo
4. muy alto 
"""))
match opcion8:
    case 1:
        print("incorrecto")
    case 2:
        print("incorrecto")
    case 3:
        print("correcto")
    case 4:
        print("incorrecto")

print("10.-¿que estructua de control es mas adecuado para iterar sobre una secuencia de elemntos" \
"un numero de veces conocido de antemano?")
opcion9 = int(input("""
1. bucle 'para'
2. sentencia condicional 'si'
3. bucle 'repetir'
4. bucle 'mientras'
"""))
match opcion9:
    case 1:
        print("correcto")
    case 2: 
        print("incorrecto")
    case 3:
        print("incorrecto")
    case 4:
        print("incorrecto")

