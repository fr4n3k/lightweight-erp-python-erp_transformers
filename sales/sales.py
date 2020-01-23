""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
    * customer_id (string): id from the crm
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
#date module
from datetime import date

FILE_NAME = 'sales/sales.csv'
ID_LIST_INDEX = 0
GAME_NAME_INDEX = 1
GAME_PRICE_INDEX = 2
SALE_MONTH_INDEX = 3
SALE_DAY_INDEX = 4
SALE_YEAR_INDEX = 5

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
                'get_lowest_price_item_id',
                'get_items_sold_between']
    dict_menu = {'1': show_table_wrapper,
                '2': add_wrapper,
                '3': remove_wrapper,
                '4': update_wrapper,
                '5': get_lowest_price_item_id_wrapper,
                '6': get_items_sold_between_wrapper}
    common.sub_menu(dict_menu, options, "Sales menu")


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


def get_lowest_price_item_id_wrapper():  
    table = data_manager.get_table_from_file(FILE_NAME)
    get_lowest_price_item_id(table)


def get_items_sold_between_wrapper():  
    table = data_manager.get_table_from_file(FILE_NAME)
    # check if input is intiger
    try:
        month_from, day_from, year_from, month_to, day_to, year_to = ui.get_inputs(['Month from :', 'Day from :','Year from :', 'Month to :', 'Day to :','Year to :'], 'Enter the dates: ' )
        int(month_from) and int(day_from) and  int(year_from) and int(month_to) and int(day_to) and int(year_to)
        get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
    except:
        ui.print_error_message("Value Error. Please provide a correct date format")
        get_items_sold_between_wrapper()

def show_table(table):

    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    titles_list = ['ID', 'title', 'price', 'month', 'day', 'year']
    ui.print_table(table, titles_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    record = ui.get_inputs(['title: ', 'price: ','month: ', 'day: ', 'year: '], "Please insert data: ")
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

    iterate = 0
    for row in table:
        if row[ID_LIST_INDEX] == id_[ID_LIST_INDEX]:
            updated_record = ui.get_inputs(['title: ', 'price: ', 'month: ', 'day: ', 'year: '], row)
            updated_record.insert(ID_LIST_INDEX, id_[ID_LIST_INDEX])
            table[iterate] = updated_record
            data_manager.write_table_to_file(FILE_NAME, table)
            break
        iterate += 1
    return table


# special functions:
# ------------------


def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """
    cheapest_price = min([row[GAME_PRICE_INDEX] for row in table])
    dict_cheapest_products = {}
    for row in table:
        if row[GAME_PRICE_INDEX] == cheapest_price:
            dict_cheapest_products[row[GAME_NAME_INDEX]] = [row[GAME_PRICE_INDEX]]
        else:
            pass
    print(min(dict_cheapest_products, key = dict_cheapest_products.get))
    # your code


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """
    filtered_table = []
    
    date_from = date(int(year_from),int(month_from),int(day_from))
    date_to = date(int(year_to),int(month_to),int(day_to))

    #logic check
    if date_to<date_from:
        message = "\nLogic error. End date precedes the start date"
        ui.print_error_message(message)
        get_items_sold_between_wrapper()
    else:
        pass

    for row in table:
        date_of_sale = date(int(row[SALE_YEAR_INDEX]),int(row[SALE_MONTH_INDEX]),int(row[SALE_DAY_INDEX]))
        if date_from<=date_of_sale<=date_to:
            filtered_table.append(row)
        else:
            pass
    label = 'ID;Title;Price;Month;Day;Year;Customer ID'
    ui.print_result(filtered_table, label)



# functions supports data abalyser
# --------------------------------


def get_title_by_id(id):

    """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code


def get_title_by_id_from_table(table, id):

    """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the sales table
        id (str): the id of the item

    Returns:
        str: the title of the item
    """

    # your code


def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code


def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _id_ of the item that was sold most recently.
    """

    # your code


def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.

    Args:
        table (list of lists): the sales table

    Returns:
        str: the _title_ of the item that was sold most recently.
    """

    # your code


def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.

    Args:
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code


def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.

    Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids

    Returns:
        number: the sum of the items' prices
    """

    # your code


def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
         sale_id (str): sale id to search for
    Returns:
         str: customer_id that belongs to the given sale id
    """

    # your code


def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.

    Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
        str: customer_id that belongs to the given sale id
    """

    # your code


def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.

    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # your code


def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.

    Args:
        table (list of list): the sales table
    Returns:
         set of str: set of customer_ids that are present in the table
    """

    # your code


def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)

    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
            all the sales id belong to the given customer_id
    """

    # your code


def get_all_sales_ids_for_customer_ids_from_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """

    # your code


def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code


def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code
