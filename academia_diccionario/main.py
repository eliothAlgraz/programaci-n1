import modelos.cursos
import modelos.alumnos
from modelos.cursos import agregarcurso
from modelos.cursos import mostrarcursos
from modelos.cursos import eliminarcurso
from modelos.alumnos import agregaralumno
from modelos.alumnos import mostraralumno
from modelos.alumnos import darbajaalumno

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


