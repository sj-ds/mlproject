# this is custom exception handling

import sys # sys module provides various functions and variables that are used to manipuolate different part of the Python runtime environment
import logging
from src.logger import logging 

def error_message_details(error, error_detail:sys):
    # return type of sys 
    _,_, exc_tb = error_detail.exc_info()  # execution info --> this will 3 info, we are interested in 3rd info only
    file_name = exc_tb.tb_frame.f_code.co_filename  # variable to store the file name
    error_message= "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name, 
        exc_tb.tb_lineno,  # get the line number
        str(error)
    )
    return error_message
    

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail= error_detail)

    def __str__(self):
        return self.error_message

    