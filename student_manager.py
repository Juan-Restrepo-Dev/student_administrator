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
        return system_constans.CONSOLE_STYLING['BOLD_TYPE'] + text.ljust(20) + system_constans.CONSOLE_STYLING['END_COMAND']
def style_text_for_the_box(text:str,total_width):
    """
    Function that styles strings for the box type using ANSI

    Args:
        text: string-> string to styled bold using ansi
        total_width: int -> size of the box for adjust text that is going to be stylized.

    Returns:
        returns text whit ANSI-styled text  
    """
    print(system_constans.CONSOLE_STYLING["CYAN"]+"║"+system_constans.CONSOLE_STYLING["END_COMAND"] +
                    system_constans.CONSOLE_STYLING["BOLD_TYPE"] +
                    system_constans.CONSOLE_STYLING["BLUE"] +
                    "  " + (f"({text}) => ").
                    ljust(total_width -2) +system_constans.CONSOLE_STYLING["CYAN"] + "║")

def style_error_for_the_box(text:str,total_width):
    """
    Function that styles strings  whe alert error for the box type using ANSI

    Args:
        text: string-> string to styled bold using ansi
        total_width: int -> size of the box for adjust text that is going to be stylized.

    Returns:
        returns text whit ANSI-styled text to error system 
    """
    print(system_constans.CONSOLE_STYLING["CYAN"]+"║"+system_constans.CONSOLE_STYLING["END_COMAND"] +
                    system_constans.CONSOLE_STYLING["BOLD_TYPE"] +
                    system_constans.CONSOLE_STYLING["RED"] +
                    "  " + (f"({text}) => ").
                    ljust(total_width - 2) +
                    system_constans.CONSOLE_STYLING["CYAN"] + "║")

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
          ljust(total_width-2) +
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
                    total_width = max(len(title), len(text_bold(system_constans.NAME_SYSTEM)),
                                     maxwidth) 
                   
                    print(system_constans.CONSOLE_STYLING["CYAN"] + "╔" + "═" * total_width +
                          "╗")

                    print("║" + system_constans.CONSOLE_STYLING["END_COMAND"] +
                          text_bold(system_constans.NAME_SYSTEM).center(total_width + 8) +
                          system_constans.CONSOLE_STYLING["CYAN"] + "║")

                    print("║" + system_constans.CONSOLE_STYLING["END_COMAND"] +
                          title.center(total_width + 8) +
                          system_constans.CONSOLE_STYLING["CYAN"] + "║")

                    print("╠" + "═" * total_width + "╣")
                    for linetext in text:
                        if system_constans.CONSOLE_STYLING["BOLD_TYPE"] in linetext:
                            if system_constans.CONSOLE_STYLING["YELLOW"] in linetext:
                                print("║" + system_constans.CONSOLE_STYLING["END_COMAND"] +
                                      "  " +
                                      linetext.center(total_width + 15) +
                                      system_constans.CONSOLE_STYLING["CYAN"] + "║")
                            else:
                                print("║" + system_constans.CONSOLE_STYLING["END_COMAND"] +
                                      "  " +
                                      linetext.ljust(total_width + 6) +
                                      system_constans.CONSOLE_STYLING["CYAN"] + "║")
                            
                        else:
                            print("║" + system_constans.CONSOLE_STYLING["END_COMAND"] + "  " +
                                  linetext.ljust(total_width - 2) +
                                  system_constans.CONSOLE_STYLING["CYAN"] + "║")
                    return (total_width)
                    
                    # break

            except ValueError:
                print('An exception occurred')

        case "data_table":   
            if data_table is None:
                data_table = []
           

            # Calculate the width of each column
            column_width = [max(len(str(col)) for col in column)for
                            column in zip(*data_table)]
       
            total_width = (sum(column_width) + 32)
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
            return total_width
        case _:
            print("ingresa una opcion correcta")

def check_if_the_student_exist(student_reference,search_key:str="id"):
    """
    Function to check if a student is already registered in the system


    Args:
        student_reference: Reference of the student you want to consult
        search_key: key of column to search

    Returns:
        boolean if the student exists returns true if it does not exist returns false
    """ 
    return any(student.get(search_key) == search_key for student in STUDENTS)
    
def create_student(student,total_width):
    """
    Function that creates a table in the console and inserts data and
    interacts with it depending on the option.


    Args:
        student: The data to be entered into the table.
        total_width: The interaction option chosen by the user.

    Returns:
        option menu: returns total width for extend table
        Displays a table in the console and interacts with it depending on the
        option entered as an argument.
    """ 
    if student.count(",") == 7:
        try:   
            student_data = student.split(",")  
            student =  {"name_student": student_data[0],
                        "id":int(student_data[1]),
                        "age":int(student_data[2]),
                        "grade1":float(student_data[3]),
                        "grade2":float(student_data[4]),
                        "grade3":float(student_data[5]),
                        "grade4":float(student_data[6]),
                        "grade5":float(student_data[7]),          
                        }
            if check_if_the_student_exist(student["id"]):
                style_text_for_the_box("El estudiante",student["name_student"], "ya esta registrado en el sistema",total_width)
            else:
                if student["grade1"] > 0 and student["grade1"] < 10 and student["grade2"] > 0 and student["grade2"] < 10 and student["grade3"] > 0 and student["grade3"] < 10 and student["grade4"] > 0 and student["grade4"] < 10 and student["grade5"] > 0 and student["grade5"] < 10:
                    STUDENTS.append(student)
                    #logs function
                    style_text_for_the_box("El estudiante se a añadido con exito",total_width)
                else:
                    style_error_for_the_box("Las notas deben estar entre el 0 y el 10",total_width)
                    
        except ValueError as ex:
            style_text_for_the_box("Ingresa los datos de manera valida",total_width)  
            style_error_for_the_box(f"  Ingresa un valor valido. el error es:{ex}")
    elif "," not in student:
        try:
            while True:
                id = int(style_input_for_the_box("Ingresa la identificacion del estudiante",total_width))
                if id > 0:
                    break
                else:
                    style_error_for_the_box("la identidicacion no puede ser 0 o contener letras")
            while True:
                age = int(style_input_for_the_box("Ingresa la edad del estudiante",total_width))
                if age > 0:
                    break
                else:
                    style_error_for_the_box("la edad del estudiante tiene que ser mayor a 0")
            while True:
                grade1 = float(style_input_for_the_box("Ingresa las notas de la Materia 1",total_width))
                if grade1 > 0 and grade1 < 10:
                    break
                else:
                    style_error_for_the_box("La nota debe estar en el rango de 0 a 10")
            while True:
                grade2 = float(style_input_for_the_box("Ingresa las notas de la Materia 2",total_width))
                if grade2 > 0 and grade2 < 10:
                    break
                else:
                    style_error_for_the_box("La nota debe estar en el rango de 0 a 10")
            while True:
                grade3 = float(style_input_for_the_box("Ingresa las notas de la Materia 3",total_width))
                if grade3 > 0 and grade3 < 10:
                    break
                else:
                    style_error_for_the_box("La nota debe estar en el rango de 0 a 10")
            while True:
                grade4 = float(style_input_for_the_box("Ingresa las notas de la Materia 4",total_width))
                if grade4 > 0 and grade4 < 10:
                    break
                else:
                    style_error_for_the_box("La nota debe estar en el rango de 0 a 10")
            while True:
                grade5 = float(style_input_for_the_box("Ingresa las notas de la Materia 5",total_width))
                if grade5 > 0 and grade5 < 10:
                    break
                else:
                    style_error_for_the_box("La nota debe estar en el rango de 0 a 10")                        
            student = {"name_student": student,
                        "id":id,
                        "age":age,
                        "grade1":grade1,
                        "grade2":grade2,
                        "grade3":grade3,
                        "grade4":grade4,
                        "grade5":grade5,          
                        }
            if check_if_the_student_exist(student["id"]):
                style_text_for_the_box("El estudiante",student["name_student"], "ya esta registrado en el sistema",total_width)
            else:
                STUDENTS.append(student)
                 #logs function
                style_text_for_the_box("El estudiante se a añadido con exito",total_width)    
        except ValueError as ex:
            style_error_for_the_box(f"Ingresa un valor valido. el error es:{ex}",total_width)
    else:
        style_error_for_the_box("No has ingresado el estudiante de manera correcta",total_width)

def show_datatable_studens():
    data_table = system_constans.HEADERS_DATA_TABLE
    for student in STUDENTS:
        data_table.append([student["name_student"], 
                          student["id"],
                          student["age"],
                          student["grade1"],
                          student["grade2"],
                          student["grade3"],
                          student["grade4"],
                          student["grade5"],
                         ])
        total_width = paint_box(type="data_table",data_table=data_table)

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
        create_student(student,total_width)


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
                        total_width = paint_box(title=title, text=menu)
                        option = style_input_for_the_box("Ingresa una opcion",total_width)
                        match option:
                            case "1":
                                show_create_student()
                            case "2":
                                show_datatable_studens()
                            case "3": exit()
                        
                            case _:
                                style_error_for_the_box("Ingresa una opcion valida")        
                case "2":
                    print("en construcion")
                case "3": exit()
                
                case _:
                    style_error_for_the_box("Ingresa una opcion valida")      
    else: 
        text = system_constans.NO_STUDENTS_FOUND + system_constans.INFO_CREATE_STUDENT
        title = text_bold("ingreso inicial de estudiantes")
        total_width = paint_box(title=title,text=text)
        initial_create_status = True
        while initial_create_status:
            student = str(style_input_for_the_box("Ingresa un estudiante",total_width))
            create_student(student,total_width)

            flag1 = True
            while flag1:
                other_student = style_input_for_the_box("Deseas añadir otro estudiante? SI(S)/NO(N)",total_width)
                if other_student == "s" or other_student == "S":
                    flag1 = False
                    continue
                elif other_student == "n" or other_student == "N":
                    if len(STUDENTS) >= 5:
                        flag1 = False
                        initial_create_status = False
                        show_main_menu()
                    else:
                        style_text_for_the_box((f"Solo tienes {len(STUDENTS)} estudiantes guardados" +
                              " lo recomendado es tener al menos 5 estudiantes " +
                              "guardados"),total_width)
                        you_are_sure = str(style_input_for_the_box("esta seguro que desea omitir la creacion de la totalidad de estudiantes recomendados ? SI(S)/NO(N)",total_width))
                        if you_are_sure == "s" or you_are_sure == "S":
                            print(system_constans.CONSOLE_STYLING["CYAN"] + "╚" +
                                  "═" * total_width + "╝"
                                  )
                            show_main_menu()
                            flag1 = False
                            initial_create_status = False
                        elif you_are_sure == "n" or you_are_sure == "N":
                            continue
                        else:
                            style_error_for_the_box("Ingresa una opcionvalida")
                            continue
                else:
                    style_error_for_the_box("Ingresa una opcionvalida")
                    continue
show_main_menu()