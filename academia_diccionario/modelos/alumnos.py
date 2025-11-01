import modelos.cursos
from modelos.cursos import mostrarcursos

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