def agregarcurso(cursos):
    nombre = input("nombre del curso:\n")
    instructor = input("nombre del instructor:\n")
    aula = int(input("numero de aula:\n"))
    cursos.append([nombre, instructor, aula,[]])
    print("curso agregado correctamente.\n")

def mostrarcursos(cursos):
    if len(cursos) == 0:
        print("No hay cursos registrado")
    else:
        print("--cursos registrados--")
        for i in range(len(cursos)):
            curso = cursos[i]
            print(f"id {i} - {cursos[0]} | instructor: aula:{curso[2]}|alumnos:{len(curso[3])}")
        print()

def agregaralumno(cursos):
    if len(cursos) == 0:
        print("primero tiene que añadir un curso")
        return
    mostrarcursos(cursos)
    try:
        idcurso = int(input("selecciona el id del curso donde agregaras el alumno:\n"))
    except:
        print("id invalido")
        return
    if idcurso < 0 or idcurso >= len(cursos):
        print("curso invalido ")
        return
    nombre_alumno = input("indique el nombre del alumno:\n")
    cursos[idcurso][3].append(nombre_alumno)
    print("elalumno fue agregado correctamente")

def mostraralumno (cursos):
    if len(cursos) == 0:
        print("no hay cursos registrado")
        return
    mostrarcursos(cursos)
    try:
        idcurso = int(input("seleccione el id del curso para ver la lista de alumno:\n"))
    except:
        print("id invalido")
        return
    if idcurso < 0 or idcurso >= len(cursos):
        print("curso no valido")
        return
    alumnos = cursos[idcurso][3]
    if len(alumnos) == 0:
        print("no hay ningun alumno registrado en este curso")
    else:
        print(f"--alumnos del curso{cursos[idcurso][0]}--")
        for i in range(len(alumnos)):
            print(f"id {i} - {alumnos[i]}")
        print()

def darbajaalumno(cursos):
    if len(cursos) == 0:
        print("no hay cursos registrado.")
        return
    mostrarcursos(cursos)
    try:
        idcurso = int(input("selecciona el id del curso:\n"))
    except:
        print("id invalido")
        return
    if idcurso < 0 or idcurso >= len(cursos):
        print("curso invalido")
        return
    alumnos = cursos[idcurso][3]
    if len(alumnos) == 0:
        print("no hay alumnos registrados en este curso")
        return
    print(f"--alumnos del curso {cursos[idcurso][0]}--")
    for i in range(len(alumnos)):
        print(f"id{i}-{alumnos[i]}")
    try:
        idalumno = int(input("indique el id del alumno a dar de baja"))
    except:
        print("id del alumno invalido")
        return
    if idalumno < 0 or idalumno >= len(alumnos):
        print("id del alumno invalido")
        return
    eliminacion = alumnos.pop(idalumno)
    print(f"se elimino al alumno: {eliminacion}")

def eliminarcurso(cursos):
    if len(cursos) == 0:
        print("no hay cursos que se elimine")
        return
    mostrarcursos(cursos)
    try:
        idcurso = int(input("selecciona el id del curso que desea eliminar:\n"))
    except:
        print("id invalido")
        return
    if idcurso < 0 or idcurso >= len(cursos):
        print("curso invalido")
        return
    eliminacion = cursos.pop(idcurso)
    print(f"se elimino el curso:{eliminacion[0]}")

cursos = []

while True:
    print("""
    1. agregar un curso
    2. agregar un alumno
    3. dar de baja a un alumno 
    4. mostrar lista de alumno
    5. mostrar cursos
    6. eliminar curso
    7. salir
    """)

    opcion = int(input("seleccione una opcion con numero:\n"))

    try:
        opcion1 = int(opcion)
    except:
        print("por favoringresa un numero valido")
        continue

    match opcion1:
        case 1:
            agregarcurso(cursos)
        case 2:
            agregaralumno(cursos)
        case 3:
            darbajaalumno(cursos)
        case 4:
            mostraralumno(cursos)
        case 5:
            eliminarcurso(cursos)
        case 6:
            print("usted salio del programa")
            break
        case _:
            print("por favor selecciones una opcion valida ")