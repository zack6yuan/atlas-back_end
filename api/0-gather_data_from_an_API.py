#!/usr/bin/python3
""" Method: Return information using REST API """
import sys
from sys import argv
import requests

def employee_statistics(employee_id):
    """ Method: Format employee information from input
    Arguments:
        - employee_id(int)
    Raises:
        - ValueError - when employee_id is not provided.
        - TypeError - when employee_id is not type "int"
    Returns:
        - Employee data (completed + uncompleted tasks)
    """
    if len(sys.argv) < 2:
        raise ValueError("Plase input empolyee id.")
    elif not isinstance(employee_id, int):
        raise TypeError("Employee id must be an integer.")
    else:
        employee_id = sys.argv(1)

    """ Method: Build URL's to gather data """
    root = "https://jsonplaceholder.typicode.com"
    user = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todo = "https://jsonplaceholder.typicode.com/users/{}/todo".format(employee_id)
