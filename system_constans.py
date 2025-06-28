
# It is a list of ANSI codes to style the console
CONSOLE_STYLING = {
    "END_COMAND": "\033[0m",
    "BOLD_TYPE": "\033[1m",
    "CYAN": "\033[36m",
    "BLUE": "\033[34m",
    "BACKGROUND_BLUE": "\033[44m",
    "BACKGROUND_GREEN": "\033[42m",
    "YELLOW": "\033[1;33m",
    "RED": "\033[0;31m",
    "GREEN": "\033[0;32m"
}
# It is a name of this system
NAME_SYSTEM = "GESTOR DE ESTUDIANTES"
MENU_PRINCIPAL = ["(1) Estudiantes","(2) Logs","(4) salir"]
MENU_STUDENTS = ["(1) Crear Estudiante","(2) Mostrar Estudiantes","(3) Editar Estudiante",
                 "(4) eliminar Estudiante","(5) volver"]
MENU_FILTER = [
                "(1): Nombre de el estudiante",
                "(2): ID de el estudiante",
                "(3): Edad de el estudiante",
                "(4): mayor o igual que",
                "(5): menor o igual que",
                "(6): volver"
              ]

MENU_EDIT = [
                "(1): Nombre de el estudiante",
                "(2): ID de el estudiante",
                "(3): Edad de el estudiante",
                "(4): Materia 1",
                "(5): Materia 2",
                "(6): Materia 3",
                "(7): Materia 4",
                "(8): Materia 5",
                "(9): Volver",
              ]



INFO_CREATE_STUDENT = [
                CONSOLE_STYLING['BOLD_TYPE'] + "Puedes hacerlo de dos maneras:"
                + CONSOLE_STYLING['END_COMAND'],

                "",

                CONSOLE_STYLING["BOLD_TYPE"]+"Individualmente :" +
                CONSOLE_STYLING["END_COMAND"],

                "Empieza escribiendo el nombre del Estudiante y presiona Enter.",

                "Luego se te pedira el numero de identificacion del estudiante"
                "ingresalo y preciona enter",

                "Luego se te pedira la edad del estudiante"
                "ingresalo y preciona enter",

                "Luego Notas del estudiante de manera individual  la nota individual "
                "de las 5 materias del estudiante",
                "recuerda que las notas son del 0 al 10",

                "",

                CONSOLE_STYLING["BOLD_TYPE"]+"Datos Separados por coma :" +
                CONSOLE_STYLING["END_COMAND"],

                "Escribe todos los datos del estudiante a la vez",

                "separándolas con una coma con el siguiente orden: " +
                CONSOLE_STYLING["BOLD_TYPE"] , 
                "("
                "Nombre del estudiante", 
                "Identificacion del estudiante", 
                "Edad del estudiante",
                "Nota 1",
                "Nota 2", 
                "Nota 3", 
                "Nota 4",
                "Nota 5)"+CONSOLE_STYLING["END_COMAND"],

                "nota:Utiliza puntos para el decimales usar en la nota del estudiante",

                CONSOLE_STYLING["BOLD_TYPE"] +
                "(ejemplo: Juan Jose Restrepo,1152335520,27,8.9,9.5,7.5,9.3,6.4 )." +
                CONSOLE_STYLING["END_COMAND"],

                ""]
NO_STUDENTS_FOUND =[
                CONSOLE_STYLING['BOLD_TYPE'] + "Bienvenido" +
                CONSOLE_STYLING['END_COMAND'],

                "",

                CONSOLE_STYLING['BOLD_TYPE'] + CONSOLE_STYLING["YELLOW"] +
                "⚠️  Atencion! ⚠️ " +
                CONSOLE_STYLING['END_COMAND'],

                "",

                "No tienes estudiantes registrados en tu "
                "Deberias ingresar al menos 5 estudiantes",

                ""
        ]
HEADERS_DATA_TABLE = [CONSOLE_STYLING['BACKGROUND_BLUE']+"Nombre de estudiante" + CONSOLE_STYLING['END_COMAND'],
                                    CONSOLE_STYLING['BACKGROUND_BLUE']+"identificacion" + CONSOLE_STYLING['END_COMAND'],
                                    CONSOLE_STYLING['BACKGROUND_BLUE']+"edad" + CONSOLE_STYLING['END_COMAND'],
                                    CONSOLE_STYLING['BACKGROUND_BLUE']+"Materia 1" + CONSOLE_STYLING['END_COMAND'],
                                    CONSOLE_STYLING['BACKGROUND_BLUE']+"Materia 2" + CONSOLE_STYLING['END_COMAND'],
                                    CONSOLE_STYLING['BACKGROUND_BLUE']+"Materia 3" + CONSOLE_STYLING['END_COMAND'],
                                    CONSOLE_STYLING['BACKGROUND_BLUE']+"Materia 4" + CONSOLE_STYLING['END_COMAND'],
                                    CONSOLE_STYLING['BACKGROUND_BLUE']+"Materia 5" + CONSOLE_STYLING['END_COMAND'],
                                    CONSOLE_STYLING['BACKGROUND_BLUE']+"promedio" + CONSOLE_STYLING['END_COMAND'],
                                    ]