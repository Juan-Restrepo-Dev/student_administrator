import system_constans

STUDENTS = []


def text_bold(text:list|str) -> list|str:
    """
    Function that styles strings with bold type using ANSI

    Args:
        text: list -> list or string to styled bold using ansi

    Returns:
        returns list whit ANSI-styled text in bold type text   
    """
    if type(text) == list:
        stylized_text = []
        for lineText in text:
            stylized_text.append(system_constans.CONSOLE_STYLING['BOLD_TYPE'] + lineText.ljust(95) +\
                                 system_constans.CONSOLE_STYLING['END_COMAND'],)
        return stylized_text    
    else:
        return system_constans.CONSOLE_STYLING['BOLD_TYPE'] + lineText.ljust(95) + system_constans.CONSOLE_STYLING['END_COMAND']

def style_input_for_the_box(text:str,total_width:int)->str:
    """
    This function is used to style an input so that the box fits and the user 
    can differentiate it and return user response.


    Args:
        text: str -> text that is going to be stylized.
        total_width: int -> size of the box for adjust text that is going to be stylized.


    Returns:
        display styled text that fits the box and input user option and return
        user response

    """
    print(system_constans.CONSOLE_STYLING["CYAN"]+"║"+system_constans.CONSOLE_STYLING["END_COMAND"] +
          system_constans.CONSOLE_STYLING["BOLD_TYPE"] +
          system_constans.CONSOLE_STYLING["BLUE"] +
          "  " + (f"({text}) => ").
          ljust(total_width - 2) +
          system_constans.CONSOLE_STYLING["CYAN"] + "║")
    option = input("║  " + system_constans.CONSOLE_STYLING["END_COMAND"] + "  ")
    return option

def paint_box(type:str = "menu", title:str = "" ,data_table=None, text=None):
    """
    Function that creates a table or box in the console and inserts data and
    interacts with it depending on the option.


    Args:
        type: str -> type of box that will be painted on the console -> 'menu','data_table'.
        title: str -> title displayed at the top of the box.
        dataTable: The data to be entered into the table box.
        text: The data to entered into box text.

    Returns:
        type: -> menu: returns total width for extend box and
        Displays a box in the console and interacts with it depending on the
        option entered as an argument.

        type: -> datable: returns total width for extend data table and
        Displays a data table in the console and interacts with it depending on the
        option entered as an argument.
    """
    
    match type:
        case "menu":
            try:
                while True:
                    maxwidth = max(len(linetext) for linetext in text)
                    totalwidth = max(len(title), len(text_bold(system_constans.NAME_SYSTEM)),
                                     maxwidth) 
                   
                    print(system_constans.CONSOLE_STYLING["CYAN"] + "╔" + "═" * totalwidth +
                          "╗")

                    print("║" + system_constans.CONSOLE_STYLING["END_COMAND"] +
                          text_bold(system_constans.NAME_SYSTEM).center(totalwidth + 8) +
                          system_constans.CONSOLE_STYLING["CYAN"] + "║")

                    print("║" + system_constans.CONSOLE_STYLING["END_COMAND"] +
                          title.center(totalwidth + 8) +
                          system_constans.CONSOLE_STYLING["CYAN"] + "║")

                    print("╠" + "═" * totalwidth + "╣")
                    for linetext in text:
                        if system_constans.CONSOLE_STYLING["BOLD_TYPE"] in linetext:
                            if system_constans.CONSOLE_STYLING["YELLOW"] in linetext:
                                print("║" + system_constans.CONSOLE_STYLING["END_COMAND"] +
                                      "  " +
                                      linetext.center(totalwidth + 15) +
                                      system_constans.CONSOLE_STYLING["CYAN"] + "║")
                            else:
                                print("║" + system_constans.CONSOLE_STYLING["END_COMAND"] +
                                      "  " +
                                      linetext.ljust(totalwidth + 6) +
                                      system_constans.CONSOLE_STYLING["CYAN"] + "║")
                            
                        else:
                            print("║" + system_constans.CONSOLE_STYLING["END_COMAND"] + "  " +
                                  linetext.ljust(totalwidth - 2) +
                                  system_constans.CONSOLE_STYLING["CYAN"] + "║")
                    return (totalwidth)
                    
                    # break

            except ValueError:
                print('An exception occurred')

        case "data_table":   
            if data_table is None:
                data_table = []
           

            # Calculate the width of each column
            column_width = [max(len(str(col)) for col in column)for
                            column in zip(*data_table)]
       
            totalwidth = (sum(column_width) + 32)
            # Crete table
            print(system_constans.CONSOLE_STYLING["CYAN"] + "╠" + "╦".join(["═" * (width + 6)
                  for width in column_width]) + "╣")
            
            for fila in data_table:
                print(system_constans.CONSOLE_STYLING["CYAN"] + "║" +
                      system_constans.CONSOLE_STYLING["END_COMAND"], end="")
                for i, valor in enumerate(fila):
                    if system_constans.CONSOLE_STYLING["BACKGROUND_BLUE"] in str(valor):
                        print(
                            str(valor).ljust(column_width[i] + 15) +
                            system_constans.CONSOLE_STYLING["CYAN"] + "║" +
                            system_constans.CONSOLE_STYLING["END_COMAND"],
                            end=""
                            )
                    elif system_constans.CONSOLE_STYLING["GREEN"] in str(valor):
                        print(
                            str(valor).ljust(column_width[i] + 17) +
                            system_constans.CONSOLE_STYLING["CYAN"] + "║" +
                            system_constans.CONSOLE_STYLING["END_COMAND"],
                            end=""
                            )
                    elif system_constans.CONSOLE_STYLING["RED"] in str(valor):
                        print(
                            str(valor).ljust(column_width[i] + 17) +
                            system_constans.CONSOLE_STYLING["CYAN"] + "║" +
                            system_constans.CONSOLE_STYLING["END_COMAND"],
                            end=""
                            )        
                    elif system_constans.CONSOLE_STYLING["BACKGROUND_GREEN"] in str(valor):
                        print(
                            str(valor).ljust(column_width[i] + 15) +
                            system_constans.CONSOLE_STYLING["CYAN"] + "║" +
                            system_constans.CONSOLE_STYLING["END_COMAND"],
                            end=""
                            )    
                    else:
                        print(
                            str(valor).ljust(column_width[i] + 6) +
                            system_constans.CONSOLE_STYLING["CYAN"] + "║" +
                            system_constans.CONSOLE_STYLING["END_COMAND"],
                            end=""
                            )
                print("")        
                print(system_constans.CONSOLE_STYLING["CYAN"] + "╠" + "╬".join(["═" * (
                      width + 6) for width in column_width]) + "╣" +
                      system_constans.CONSOLE_STYLING["END_COMAND"])
            print(system_constans.CONSOLE_STYLING["CYAN"] + "╚" + "╩".join(["═" * (
                  width + 6) for width in column_width]) + "╝" +
                  system_constans.CONSOLE_STYLING["END_COMAND"]) 
            return totalwidth
        case _:
            print("ingresa una opcion correcta")
def check_if_the_student_exist():
    """
    Function that creates a table in the console and inserts data and
    interacts with it depending on the option.


    Args:
        student: The data to be entered into the table.
        totalwidth: The interaction option chosen by the user.

    Returns:
        option menu: returns total width for extend table
        Displays a table in the console and interacts with it depending on the
        option entered as an argument.
    """ 
    
def create_student(student,total_width):
    """
    Function that creates a table in the console and inserts data and
    interacts with it depending on the option.


    Args:
        student: The data to be entered into the table.
        totalwidth: The interaction option chosen by the user.

    Returns:
        option menu: returns total width for extend table
        Displays a table in the console and interacts with it depending on the
        option entered as an argument.
    """ 
    if student.count(",") == 6:   
        student_data = student.split(",")  
        student =  {"name_student": student_data[0],
                    "id":int(student_data[1]),
                    "age":int(student_data[2],
                              )}       

def show_create_student():
    """
    Function that displays a box where a new student can be created

    Args:
        None
    Returns:
        Displays a box where a new student can be created and interacts with it depending on the
        option entered as an argument.    
    """
    title = text_bold("Crear un estudiante")
    total_width = (paint_box(title=title,text=system_constans.INFO_CREATE_STUDENT))
    initial_create_status = True
    while initial_create_status:
        student = style_input_for_the_box("Ingresa un nuevo estudiante",total_width)
        create_product(student,total_width)


def show_main_menu():
    """
    Function that creates a table in the console and inserts data and
    interacts with it depending on the option.

    Args:
        None
    Returns:
        Displays a table in the console and interacts with it depending on the
        option entered as an argument.    
    """
    
    if STUDENTS:
        while True:
            title = text_bold("MENU PRINCIPAL")
            menu =  text_bold(system_constans.MENU_PRINCIPAL)
            total_width = paint_box(title=title, text=menu)
            option = style_input_for_the_box("Ingresa una opcion",total_width)
            match option:
                case "1":
                    flag = True
                    while flag:
                        title = text_bold("ESTUDIANTES")
                        menu = text_bold(system_constans.MENU_STUDENTS)
                        totalwidth = paint_box(title=title, text=menu)
                        option = style_input_for_the_box("Ingresa una opcion",total_width)
                        match option:
                            case "1":
                                show_create_student()
                        







    else: print("hola perro")
