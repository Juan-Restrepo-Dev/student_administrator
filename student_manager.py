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
            stylized_text.append(system_constans.CONSOLE_STYLING['BOLD_TYPE'] + lineText.ljust(95) +
                                 system_constans.CONSOLE_STYLING['END_COMAND'])
        return stylized_text    
    else:
        return system_constans.CONSOLE_STYLING['BOLD_TYPE'] + text.ljust(2) + system_constans.CONSOLE_STYLING['END_COMAND']

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
                    "  " + (f"({text})").
                    ljust(total_width) +system_constans.CONSOLE_STYLING["CYAN"] + "║"+system_constans.CONSOLE_STYLING["END_COMAND"])

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
                    "  " + (f"({text})").
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
       
            total_width = (sum(column_width)+ 36)
            # Crete table
            print(system_constans.CONSOLE_STYLING["CYAN"] + "╠" + "╦".join(["═" * (width - 8)
                  for width in column_width]) + "╣")
            
            for fila in data_table:
                print(system_constans.CONSOLE_STYLING["CYAN"] + "║" +
                      system_constans.CONSOLE_STYLING["END_COMAND"], end="")
                for i, valor in enumerate(fila):
                    if system_constans.CONSOLE_STYLING["BACKGROUND_BLUE"] in str(valor):
                        print(
                            str(valor).ljust(column_width[i] + 1) +
                            system_constans.CONSOLE_STYLING["CYAN"] + "║" +
                            system_constans.CONSOLE_STYLING["END_COMAND"],
                            end=""
                            )
                    elif system_constans.CONSOLE_STYLING["GREEN"] in str(valor):
                        print(
                            str(valor).ljust(column_width[i] + 3) +
                            system_constans.CONSOLE_STYLING["CYAN"] + "║" +
                            system_constans.CONSOLE_STYLING["END_COMAND"],
                            end=""
                            )
                    elif system_constans.CONSOLE_STYLING["RED"] in str(valor):
                        print(
                            str(valor).ljust(column_width[i] + 3) +
                            system_constans.CONSOLE_STYLING["CYAN"] + "║" +
                            system_constans.CONSOLE_STYLING["END_COMAND"],
                            end=""
                            )
                    elif system_constans.CONSOLE_STYLING["YELLOW"] in str(valor):
                        print(
                            str(valor).ljust(column_width[i] + 3) +
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
                            str(valor).ljust(column_width[i] - 8) +
                            system_constans.CONSOLE_STYLING["CYAN"] + "║" +
                            system_constans.CONSOLE_STYLING["END_COMAND"],
                            end=""
                            )
                print("")        
                print(system_constans.CONSOLE_STYLING["CYAN"] + "╠" + "╬".join(["═" * (
                      width - 8) for width in column_width]) + "╣" +
                      system_constans.CONSOLE_STYLING["END_COMAND"])
            print(system_constans.CONSOLE_STYLING["CYAN"] + "╚" + "╩".join(["═" * (
                  width - 8) for width in column_width]) + "╝" +
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
    return any(student.get(search_key) == student_reference for student in STUDENTS)
    
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
            if len(student_data[0]) < 30 and str(student_data[0]).replace(" ", "").isalpha() :
                student =  {"name_student": student_data[0]}
            else:
                raise ValueError("El nombre esta mal escrito no puede estar vacio ni contener simbolos o numeros")
                
            if str(student_data[1]).isdigit() and len(student_data[1]) >= 8 and len(student_data[1]) <= 10:
                student["id"] = int(student_data[1])
            else:
                raise ValueError("la identificacion del estudiante es numerica y debe tener de 8 a 10 digito")    
            if str(student_data[2]).isdigit() and int(student_data[2]) > 3 and int(student_data[2]) < 86:    
                student["age"] = int(student_data[2])
            else:
                raise ValueError("la edad del estudiante debe estar entre 4 y 85 años")    
        
            if float(student_data[3]) > 0 and float(student_data[3]) < 10 and float(student_data[4]) > 0 and float(student_data[4]) < 10 and float(student_data[5]) > 0 and float(student_data[5]) < 10 and float(student_data[6]) > 0 and float(student_data[6]) < 10 and float(student_data[7]) > 0 and float(student_data[7]) < 10: 
                student["grade1"] = float(student_data[3]) 
                student["grade2"] = float(student_data[4])  
                student["grade3"] = float(student_data[5])
                student["grade4"] = float(student_data[6])
                student["grade5"] = float(student_data[7])
            else:
                raise ValueError("Las notas deben estar entre el 0 y el 10")


            if check_if_the_student_exist(student["id"]):
                raise ValueError("El estudiante",student["name_student"], "ya esta registrado en el sistema")
            else:
                    STUDENTS.append(student)
                    #logs function
                    style_text_for_the_box("El estudiante se a añadido con exito",total_width)
                    
        except ValueError as e:
            style_text_for_the_box("Ingresa los datos de manera valida",total_width)  
            style_error_for_the_box("Ingresa un valor valido. el error es =>",total_width)
            style_error_for_the_box(e,total_width)

    elif "," not in student:
    
        try:
            while True:
                if  len(student) < 30 and str(student).replace(" ", "").isalpha() :
                    break
                else:
                    raise ValueError("El nombre esta mal escrito no puede estar vacio ni contener simbolos o numeros")
                    
            while True:
                id = int(style_input_for_the_box("Ingresa la identificacion del estudiante",total_width))
                if len(str(id)) >= 8 and len(str(id)) <= 10:
                    break
                else:
                    style_error_for_the_box("la identificacion del estudiante es numerica y debe tener de 8 a 10 digito",total_width)
            while True:
                age = int(style_input_for_the_box("Ingresa la edad del estudiante",total_width))
                if age > 3 and age < 86:
                    break
                else:
                    style_error_for_the_box("la edad del estudiante debe estar entre 4 y 85 años",total_width)
            while True:
                grade1 = float(style_input_for_the_box("Ingresa las notas de la Materia 1",total_width))
                if grade1 > 0 and grade1 < 10:
                    break
                else:
                    style_error_for_the_box("La nota debe estar en el rango de 0 a 10",total_width)
            while True:
                grade2 = float(style_input_for_the_box("Ingresa las notas de la Materia 2",total_width))
                if grade2 > 0 and grade2 < 10:
                    break
                else:
                    style_error_for_the_box("La nota debe estar en el rango de 0 a 10",total_width)
            while True:
                grade3 = float(style_input_for_the_box("Ingresa las notas de la Materia 3",total_width))
                if grade3 > 0 and grade3 < 10:
                    break
                else:
                    style_error_for_the_box("La nota debe estar en el rango de 0 a 10",total_width)
            while True:
                grade4 = float(style_input_for_the_box("Ingresa las notas de la Materia 4",total_width))
                if grade4 > 0 and grade4 < 10:
                    break
                else:
                    style_error_for_the_box("La nota debe estar en el rango de 0 a 10",total_width)
            while True:
                grade5 = float(style_input_for_the_box("Ingresa las notas de la Materia 5",total_width))
                if grade5 > 0 and grade5 < 10:
                    break
                else:
                    style_error_for_the_box("La nota debe estar en el rango de 0 a 10",total_width)                        
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
                style_error_for_the_box(("El estudiante",student["name_student"], "ya esta registrado en el sistema"),total_width)
            else:
                STUDENTS.append(student)
                 #logs function
                style_text_for_the_box("El estudiante se a añadido con exito",total_width)    
                
        except ValueError as e:
            style_text_for_the_box("Ingresa los datos de manera valida",total_width)  
            style_error_for_the_box("Ingresa un valor valido. el error es =>",total_width)
            style_error_for_the_box(e,total_width)
            
    else:
        style_error_for_the_box("Ingresa los datos de manera valida",total_width)
        style_error_for_the_box("(ejemplo: Juan Jose Restrepo,1152335520,27,8.9,9.5,7.5,9.3,6.4 ).",total_width)  

def filter_students(text_search,dic_key,type, total_width):
    filter_value= style_input_for_the_box(text_search,total_width)
    try:
        if type == "equal_to":
            if dic_key == "id" or dic_key == "age" or  dic_key == "grade1" or dic_key == "grade2" or dic_key == "grade3" or dic_key == "grade4" or  dic_key == "grade5":
                filter_students = list(filter(lambda x: x[dic_key] == int(filter_value), STUDENTS))
                return filter_students
            else:
                filter_students = list(filter(lambda x: x[dic_key] == filter_value, STUDENTS))
                return filter_students
        elif type == "greater_than":
            filter_students = list(filter(lambda x: x[dic_key] >= int(filter_value), STUDENTS))
            return filter_students
        elif type == "less_than":
            filter_students = list(filter(lambda x: x[dic_key] <= int(filter_value), STUDENTS))
            return filter_students

        
    except ValueError:
        style_error_for_the_box("No hay coincidencias con la busqueda comprueba que los datos este bien escritos")
    
def edit_product(id,column_value,new_value):
    for dic in STUDENTS:
        if dic["id"] == id:
             dic[column_value] = new_value 

def delete_product(product_name):
    try:
        for dic in STUDENTS:
            if dic["name_product"] == product_name:
                STUDENTS.remove(dic)
                #logfuntion
    except ValueError:
        print(ValueError)            

def show_datatable_studens():
    data_table = [system_constans.HEADERS_DATA_TABLE]
    
    for student in STUDENTS:
        list_grades = [student["grade1"],student["grade2"],student["grade3"],
                       student["grade4"],student["grade5"],]
        average = sum(list_grades) / len(list_grades)
        if average > 7 :
            average = system_constans.CONSOLE_STYLING['GREEN']+(f"{average}").ljust(1) + system_constans.CONSOLE_STYLING['END_COMAND']
        elif average > 5:
            average = system_constans.CONSOLE_STYLING['YELLOW']+(f"{average}").ljust(1) + system_constans.CONSOLE_STYLING['END_COMAND']
        else:
            average = system_constans.CONSOLE_STYLING['RED']+(f"{average}").ljust(1) + system_constans.CONSOLE_STYLING['END_COMAND']         
        data_table.append([student["name_student"], 
                          student["id"],
                          student["age"],
                          student["grade1"],
                          student["grade2"],
                          student["grade3"],
                          student["grade4"],
                          student["grade5"],
                          average
                         ])
    total_width = paint_box(type="data_table",data_table=data_table)
    paint_box(title="filtrar datos ->",text=system_constans.MENU_FILTER)
    option = style_input_for_the_box("Ingresa una opcion",total_width)
    headers_data_table = system_constans.HEADERS_DATA_TABLE
    flag = True
    while flag:
        match option:
            case "1":
                break
            case "2":
                break
            case "3":
                break
            case "4":
                break
            case "5":
                break
            case "6":
                break
            case _:
                break                            

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
        other_student = style_input_for_the_box("Deseas añadir otro estudiante? SI(S)/NO(N)",total_width)
        if other_student == "s" or other_student == "S":
            continue
        elif other_student == "n" or other_student == "N":
            print(system_constans.CONSOLE_STYLING["CYAN"] + "╚" + "═" * total_width + "╝")
            break
        else:
            style_error_for_the_box("Ingresa una opcion valida",total_width)    

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
                            case "3":
                                try:
                                    edit_status = True
                                    while edit_status:
                                        student_id = int(style_input_for_the_box("Ingresa la identificacion del estudiante que quieres editar",total_width))
                                        
                                        if check_if_the_student_exist(student_id):
                                            text_bold("Ingresa la columna que quieres editar")
                                            filter_column = style_input_for_the_box(system_constans.MENU_EDIT,total_width)
                                            match filter_column:
                                                case "1":
                                                    new_value = style_input_for_the_box("Ingresa el nuevo valor",total_width)
                                                    if  len(new_value) < 30 and str(new_value).replace(" ", "").isalpha() :
                                                        edit_product(student_id,"name_student",new_value)

                                                        style_text_for_the_box("se ha editado correctamente",total_width)
                                                        edit_status = False
                                                    else:
                                                        raise ValueError("El nombre esta mal escrito no puede estar vacio ni contener simbolos o numeros")
                                                case "2":
                                                    new_value = int(style_input_for_the_box("Ingresa el nuevo valor",total_width))
                                                    if  len(str(new_value)) >= 8 and len(str(new_value)) <= 10() :
                                                        edit_product(student_id,"id",new_value)
                                                        style_text_for_the_box("se ha editado correctamente",total_width)
                                                        edit_status = False
                                                    else:
                                                        raise ValueError("la identificacion del estudiante es numerica y debe tener de 8 a 10 digito")
                                                case "3":
                                                    new_value = int(style_input_for_the_box("Ingresa el nuevo valor",total_width))
                                                    if  new_value> 3 and new_value< 86() :
                                                        edit_product(student_id,"age",new_value)
                                                        style_text_for_the_box("se ha editado correctamente",total_width)
                                                        edit_status = False
                                                    else:
                                                        raise ValueError("la edad del estudiante debe estar entre 4 y 85 años")
                                                case "4":
                                                    new_value = float(style_input_for_the_box("Ingresa el nuevo valor",total_width))
                                                    if  new_value > 0 and new_value < 10() :
                                                        edit_product(student_id,"grade1",new_value)
                                                        style_text_for_the_box("se ha editado correctamente",total_width)
                                                        edit_status = False
                                                    else:
                                                        raise ValueError("La nota debe estar en el rango de 0 a 10")
                                                case "5":
                                                    new_value = float(style_input_for_the_box("Ingresa el nuevo valor",total_width))
                                                    if  new_value > 0 and new_value < 10() :
                                                        edit_product(student_id,"grade2",new_value)
                                                        style_text_for_the_box("se ha editado correctamente",total_width)
                                                        edit_status = False
                                                    else:
                                                        raise ValueError("La nota debe estar en el rango de 0 a 10")
                                                case "6":
                                                    new_value = float(style_input_for_the_box("Ingresa el nuevo valor",total_width))
                                                    if  new_value > 0 and new_value < 10() :
                                                        edit_product(student_id,"grade3",new_value)
                                                        style_text_for_the_box("se ha editado correctamente",total_width)
                                                        edit_status = False
                                                    else:
                                                        raise ValueError("La nota debe estar en el rango de 0 a 10") 
                                                case "7":
                                                    new_value = float(style_input_for_the_box("Ingresa el nuevo valor",total_width))
                                                    if  new_value > 0 and new_value < 10() :
                                                        edit_product(student_id,"grade4",new_value)
                                                        style_text_for_the_box("se ha editado correctamente",total_width)
                                                        edit_status = False
                                                    else:
                                                        raise ValueError("La nota debe estar en el rango de 0 a 10")
                                                case "8":
                                                    new_value = float(style_input_for_the_box("Ingresa el nuevo valor",total_width))
                                                    if  new_value > 0 and new_value < 10() :
                                                        edit_product(student_id,"grade5",new_value)
                                                        style_text_for_the_box("se ha editado correctamente",total_width)
                                                        edit_status = False
                                                    else:
                                                        raise ValueError("La nota debe estar en el rango de 0 a 10")
                                                case "9":
                                                    edit_status = False

                                                case _:
                                                    style_error_for_the_box("ingresa una opocion valida",total_width)                 
                                        else:
                                            style_error_for_the_box("No se encuentra al estudiante",total_width)
                                except ValueError as e:
                                    style_error_for_the_box(e)

                            case "4":
                                student = style_input_for_the_box("Ingresa la identificacion del estudiante que quieres eliminar",total_width)
                                if check_if_the_student_exist(student):
                                    delete_product(student)
                                    style_text_for_the_box("El estudiante se elimino con exito",total_width)
                                else:
                                    style_error_for_the_box("El estudiante no esta registrado",total_width) 
                            case "5":
                                flag = False        
                            case _:
                                style_error_for_the_box("Ingresa una opcion valida",total_width)        
                case "2":
                    print("en construcion")
                case "3": exit()
                
                case _:
                    style_error_for_the_box("Ingresa una opcion valida",total_width)      
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
                            style_error_for_the_box("Ingresa una opcionvalida",total_width)
                            continue
                else:
                    style_error_for_the_box("Ingresa una opcionvalida",total_width)
                    continue

show_main_menu()