""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

FILE_NAME = 'hr/persons.csv'
ID_LIST_INDEX = 0
NAME_INDEX = 1
AGE_INDEX = 2

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code
    options = ['show table',
                'add',
                'remove',
                'update',
                'get oldest person',
                'get persons closest to average']
    dict_menu = {'1': show_table_wrapper,
                '2': add_wrapper,
                '3': remove_wrapper,
                '4': update_wrapper,
                '5': get_oldest_person_wrapper,
                '6': get_persons_closest_to_average_wrapper}
    common.sub_menu(dict_menu, options, "HR menu")


def show_table_wrapper():
    table = data_manager.get_table_from_file(FILE_NAME)
    show_table(table)


def add_wrapper():
    table = data_manager.get_table_from_file(FILE_NAME)
    add(table)


def remove_wrapper():
    table = data_manager.get_table_from_file(FILE_NAME)
    remove(table, ui.get_inputs(['ID :'], 'Enter ID: '))


def update_wrapper():
    table = data_manager.get_table_from_file(FILE_NAME)
    update(table, ui.get_inputs(['ID :'], 'Enter ID: '))


def get_oldest_person_wrapper():
    table = data_manager.get_table_from_file(FILE_NAME)
    get_oldest_person(table)


def get_persons_closest_to_average_wrapper():
    table = data_manager.get_table_from_file(FILE_NAME)
    get_persons_closest_to_average(table)


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code
    titles_list = ['ID', 'name', 'birth_year']
    ui.print_table(table, titles_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code
    ID_INDEX = 0
    record = ui.get_inputs(['Name: ', 'Birth year: '], "Please insert data: ")
    record.insert(ID_INDEX, common.generate_random(table))
    table.append(record)
    data_manager.write_table_to_file(FILE_NAME, table)
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    for person in table:
        if person[ID_LIST_INDEX] == id_[ID_LIST_INDEX]:
            table.remove(person)
    data_manager.write_table_to_file(FILE_NAME, table)
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code
    ID_LIST_INDEX = 0
    iterate = 0
    for person in table:
        if person[ID_LIST_INDEX] == id_[ID_LIST_INDEX]:
            updated_record = ui.get_inputs(['Name: ', 'Birth year: '], person)
            updated_record.insert(ID_LIST_INDEX, id_[ID_LIST_INDEX])
            table[iterate] = updated_record
            data_manager.write_table_to_file(FILE_NAME, table)
            break
        iterate += 1
    return table


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """
    
    oldest_year = min([person[AGE_INDEX] for person in table])
    oldest_people = []
    for person in table:
        if person[AGE_INDEX] == oldest_year:
            oldest_people.append(person[NAME_INDEX])
        else:
            pass
    print(oldest_people)




def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """

    counter = 0
    total_year_of_birth = 0
    persons_closest_to_average = []

    # enclose this loop in a new function
    for person in table:
        counter +=1
        total_year_of_birth += int(person[AGE_INDEX])
    average_year_of_birth = total_year_of_birth/counter

    closest_number_of_years_to_average = min([abs(int(person[AGE_INDEX])-average_year_of_birth) for person in table])

    for person in table:
        if abs(int(person[AGE_INDEX])-average_year_of_birth) == closest_number_of_years_to_average:
            persons_closest_to_average.append(person[NAME_INDEX])
    print(persons_closest_to_average)
    
    return persons_closest_to_average


