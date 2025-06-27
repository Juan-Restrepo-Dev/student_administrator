# solicitar al usuario que ingrese una calificacion de el 0 al 100
# evaluar si el usuario ha reprobado o aprobado basandose en calificacion.
# el usuario puede ingresar una lista de calificaciones separadas por coma.
# calcular y mostrar el promedio de la lista de calificaciones.
# preguntar al usuario por un valor espesifico.
# ver calificaciones mayores a un valor en especifico
# verificar si esta calificiacion esta en la lista de calificaciones

import time

CONSOLE_STYLING = {
    "END_COMAND": "\033[0m",
    "BOLD_TYPE": "\033[1m",
    "CYAN": "\033[36m",
    "BLUE": "\033[34m",
    "BACKGROUND_BLUE": "\033[44m"
}


def blink_input(texto):
    """
    Imprime el texto proporcionado en la consola con un efecto de parpadeo.

    Args:
        texto: El texto a parpadear.
    """
    while True:
        # Activamos el parpadeo
        print(f"\033[5m{texto}\033[0m", end="\r")
        # Esperamos un período
        time.sleep(0.5)
        # Borramos la línea actual (para que el texto parpadee)
        print("\033[K", end="\r")
        # Esperamos otro período
        time.sleep(0.5)


def paint_data_table(data_table=None, option="initial", title=""):
    """
    Funcion que crea una tabla en consola y se insertan datos e interactua
    con ella dependiendo de la opcion.

    Args:
        dataTable: son los datos que se introduciran en la tabla.
        option: la opcion de interaccion elegida por el usuario

    Returns:
        Pinta una tabla en consola e interactua con ella dependiendo
        de la opcion que se introduzca como argumento
    """
    match option:
        case "initial":
            try:
                while True:
                    text = [
                        CONSOLE_STYLING['BOLD_TYPE'] + "Por favor, ingresa tu "
                        "listado de calificaciones" +
                        CONSOLE_STYLING['END_COMAND'],

                        "Puedes hacerlo de dos maneras:",

                        CONSOLE_STYLING["BOLD_TYPE"]+"Individualmente :" +
                        CONSOLE_STYLING["END_COMAND"],

                        "Escribe cada calificación y presiona Enter.",

                        CONSOLE_STYLING["BOLD_TYPE"]+"Separadas por coma :" +
                        CONSOLE_STYLING["END_COMAND"],

                        "Escribe todas las calificaciones a la vez, "
                        "separándolas con una coma ",

                        CONSOLE_STYLING["BOLD_TYPE"] +
                        "(ejemplo: 2.5, 3.8, 5.0)." +
                        CONSOLE_STYLING["END_COMAND"],

                        ""
                        ]
                    title = "Gestor de calificaciones"
                    maxwidth = max(len(linetext) for linetext in text)
                    totalwidth = max(len(title), maxwidth) + 10

                    print(CONSOLE_STYLING["CYAN"] + "╔" + "═" * totalwidth +
                          "╗")

                    print("║" + CONSOLE_STYLING["END_COMAND"] + 
                          title.center(totalwidth) + CONSOLE_STYLING["CYAN"] +
                          "║")
                              
                    print("╠" + "═" * totalwidth + "╣")               
                    for linetext in text:
                        if CONSOLE_STYLING["BOLD_TYPE"] in linetext:
                            print("║" + CONSOLE_STYLING["END_COMAND"] + "  " +
                                  linetext.ljust(totalwidth + 6) +
                                  CONSOLE_STYLING["CYAN"] + "║")
                        else:
                            print("║" + CONSOLE_STYLING["END_COMAND"] + "  " +
                                  linetext.ljust(totalwidth - 2) +
                                  CONSOLE_STYLING["CYAN"] + "║")
                            
                    print("║" + CONSOLE_STYLING["END_COMAND"] +
                          CONSOLE_STYLING["BOLD_TYPE"] +
                          CONSOLE_STYLING["BLUE"] +
                          "  " + ("(Calificacion/es) => ").
                          ljust(totalwidth - 2) +
                          CONSOLE_STYLING["CYAN"] + "║")
                                                                                                             
                    student_ratings = str(input("║" +
                                                CONSOLE_STYLING["END_COMAND"]
                                                + " "))

                    rating_list = student_ratings.split(",")
                    headers_data_table = [f"{CONSOLE_STYLING['BACKGROUND_BLUE']}Nombre Materia{CONSOLE_STYLING["END_COMAND"]}",
                                          f"{CONSOLE_STYLING['BACKGROUND_BLUE']}Calificacion{CONSOLE_STYLING["END_COMAND"]}",
                                          f"{CONSOLE_STYLING['BACKGROUND_BLUE']}Status{CONSOLE_STYLING["END_COMAND"]}"]
                    if data_table is None:
                        data_table = []
                        data_table.append(headers_data_table)
                    # for i, rating in enumerate(rating_list):
                    #     grade_by_subjet = [f"Materia{i}", rating, 
                    #                        "Aproved"if int(rating) > 3 else "denied"]
                    #     data_table.append(grade_by_subjet)
                    # Calcular el ancho de cada columna
                    column_width = [max(len(str(col)) for col in column)for
                                    column in zip(*data_table)]
                    # Crea la tabla
                    print(CONSOLE_STYLING["CYAN"] + "╠" + "╦".join(["═" * (width + 6) for
                          width in column_width]) + "╗")
                    for fila in data_table:
                        print("║", end="")
                        for i, valor in enumerate(fila):
                            if CONSOLE_STYLING["BACKGROUND_BLUE"] in valor:
                                print(
                                    CONSOLE_STYLING["END_COMAND"] + 
                                    str(valor).ljust(column_width[i] + 15) +
                                    CONSOLE_STYLING["CYAN"],
                                    end="║"
                                    )
                            else:
                                print(
                                    CONSOLE_STYLING["END_COMAND"] + 
                                    str(valor).ljust(column_width[i] + 6) +
                                    CONSOLE_STYLING["CYAN"],
                                    end="║"
                                    )
                                     
                    print("hola perro")
                    break
                    # USER_RATINGS = str(input("(Calificacion/es) => "))
                    
                    # 
                    # print(ratingList)
                    # paint_data_table(ratingList)

                    # se pinta la lista de opciones del menu
                    # print("-" * 48)
                    # print("                      MENU                      ")
                    # print("-" * 48)
                    # print()
                    # print("(-1) Crear una orden de reparacion")
                    # print("(0) Mostrar una lista de reparaciones pendientes")
                    # print("(1) Editar estado de una resparcion")
                    # print("(2) ver el historial de reparaciones")
                    # print("(3) Salir del sistema")
                    # print()

                    # if menuOption ==

            except ValueError:
                print('An exception occurred')
            
        case _:
            print("ingresa una opcion correcta")    
    
    # 
    

    
    # # Calcular el ancho de cada columna
    # column_width = [max(len(str(col)) for col in column)
    #                 for column in zip(*data_table)]

    # # Crea la tabla
    # print("+" + "+".join(["-" * width for width in column_width]) + "+")
    # for fila in data_table:
    #     print("|", end="")
    #     for i, valor in enumerate(fila):
    #         print(f"{str(valor):<{column_width[i]}} |", end="")
    #     print("\n" + "+" + "+".join(["-" * width for width in column_width]) + "+") 

paint_data_table()
