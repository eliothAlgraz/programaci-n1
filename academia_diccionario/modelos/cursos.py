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
