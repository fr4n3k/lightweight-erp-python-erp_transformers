"""
This module creates reports for the marketing department.
This module can run independently from other modules.
Has no own data structure but uses other modules.
Avoid using the database (ie. .csv files) of other modules directly.
Use the functions of the modules instead.
"""

# todo: importing everything you need

# importing everything you need
import ui
import common
from sales import sales
from crm import crm


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    options = ['get last buyer name',
                'get last buyer id',
                'get the name of the top buyer with amount of money spent',
                'get the id of the top buyer with amount of money spent',
                'get the name of the most frequent buyer',
                'get the id of the most frequent buyer']
    dict_menu = {'1': get_the_last_buyer_name_wrapper,
                '2': get_the_last_buyer_id_wrapper,
                '3': get_the_buyer_name_spent_most_and_the_money_spent_wrapper,
                '4': get_the_buyer_id_spent_most_and_the_money_spent_wrapper,
                '5': get_the_most_frequent_buyers_names_wrapper,
                '6': get_the_most_frequent_buyers_ids_wrapper}
    common.sub_menu(dict_menu, options, "Store menu")


def get_the_last_buyer_name_wrapper():
    pass
def get_the_last_buyer_id_wrapper():
    pass
def get_the_buyer_name_spent_most_and_the_money_spent_wrapper():
    pass
def get_the_buyer_id_spent_most_and_the_money_spent_wrapper():
    pass
def get_the_most_frequent_buyers_names_wrapper():
    pass
def get_the_most_frequent_buyers_ids_wrapper():
    pass


def get_the_last_buyer_name():
    """
    Returns the customer _name_ of the customer made sale last.

    Returns:
        str: Customer name of the last buyer
    """

    # find the _customer_id_ of the last sale in _sales_
    # find the _name_ of the given _customer_id_ as _id_ in _crm_
    last_buyer_id = 
    last_buyer_name = crm.get_name_by_id(last_buyer_name)
    return last_buyer_name

def get_the_last_buyer_id():
    """
    Returns the customer _id_ of the customer made sale last.

    Returns:
        str: Customer id of the last buyer
    """

    # find the _customer_id_ of the last sale in _sales_


def get_the_buyer_name_spent_most_and_the_money_spent():
    """
    Returns the customer's _name_ who spent the most in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer name and the sum the customer spent eg.: ('Daniele Coach', 42)
    """

    # find the _customer_id_ who spent most in _sales_
    # find the _name_ of the given _customer_id_ as _id_ in _crm_
    biggest_spender_id = 
    biggest_spender_name = crm.get_name_by_id(biggest_spender_id)
    return last_buyer_name

def get_the_buyer_id_spent_most_and_the_money_spent():
    """
    Returns the customer's _id_ who spent more in sum and the money (s)he spent.

    Returns:
        tuple: Tuple of customer id and the sum the customer spent eg.: (aH34Jq#&, 42)
    """

    # find the _customer_id_ who spent most in _sales_


def get_the_most_frequent_buyers_names(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer's name) who bought most frequently in an
    ordered list of tuples of customer names and the number of their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer names and num of sales
            The first one bought the most frequent. eg.: [('Genoveva Dingess', 8), ('Missy Stoney', 3)]
    """
    
    # find the _customer_id_ who is the most frequent buyer in _sales_
    # find the _name_ of the given _customer_id_ as _id_ in _crm_
    most_frequent_buyer_id = 
    most_frequent_buyer_name = crm.get_name_by_id(most_frequent_buyer_id)
    return last_buyer_name

def get_the_most_frequent_buyers_ids(num=1):
    """
    Returns 'num' number of buyers (more precisely: the customer ids of them) who bought more frequent in an
    ordered list of tuples of customer id and the number their sales.

    Args:
        num: the number of the customers to return.

    Returns:
        list of tuples: Ordered list of tuples of customer ids and num of sales
            The first one bought the most frequent. eg.: [(aH34Jq#&, 8), (bH34Jq#&, 3)]
    """

    # find the _customer_id_ who is the most frequent buyer in _sales_