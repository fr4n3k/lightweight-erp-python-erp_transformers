""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month
    * day (number): Day
    * year (number): Year
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

FILE_NAME = "accounting/items.csv"

def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """


    options = ['Show table',
                'Add a new record',
                'Remove record',
                'Update single record',
                'Which year has the highest profit?',
                'What is the average (per item) profit in a given year?']
    dict_menu = {'1': show_table_wrapper,
                '2': add_wrapper,
                '3': remove_wrapper,
                '4': update_wrapper,
                '5': which_year_max_wrapper,
                '6': avg_amount_wrapper}
    common.sub_menu(dict_menu, options, "Accounting menu")


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


def which_year_max_wrapper():
    table = data_manager.get_table_from_file(FILE_NAME)
    which_year_max(table)


def avg_amount_wrapper():
    table = data_manager.get_table_from_file(FILE_NAME)
    avg_amount(table, ui.get_inputs(['Year'], 'Enter a year: '))


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code
    titles_list = ['ID', 'Month', 'Day', 'Year', 'in = income, out = outflow', 'Amount of transaction in USD']
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
    record = ui.get_inputs(['Month: ', 'Day: ', 'Year: ', 'in = income, out = outflow: ', 'Amount of transaction in USD: '], "Please insert data: ")
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

    # your code
    ID_LIST_INDEX = 0
    for row in table:
        if row[ID_LIST_INDEX] == id_[ID_LIST_INDEX]:
            table.remove(row)
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
    for row in table:
        if row[ID_LIST_INDEX] == id_[ID_LIST_INDEX]:
            updated_record = ui.get_inputs(['Month: ', 'Day: ', 'Year: ', 'in = income, out = outflow: ', 'Amount in USD: '], row)
            updated_record.insert(ID_LIST_INDEX, id_[ID_LIST_INDEX])
            table[iterate] = updated_record
            data_manager.write_table_to_file(FILE_NAME, table)
            break
        iterate += 1
    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    set_of_years = set ()
    for row in table: 
        set_of_years.add(row[3])

    dict_annual_profit = {}


    for year in set_of_years:
        profit = 0
        for row in table:
            if row[3] == year:
                if row[4] == "in":
                    profit += int(row[5])
                elif row[4] == "out":
                    profit -= int(row[5])
            else:
                pass
        dict_annual_profit[year] =profit
    print (max(zip(dict_annual_profit.values(), dict_annual_profit.keys())))

    # your code


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    # your code
