import os,sys
from src.data_gathering.logging import logging

def get_error_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message=f"""error occur in python script name [{file_name}] line nbr [{exc_tb.tb_lineno}] error message [{str(error)}]"""
    return error_message
class CustomException(Exception):
    def __init__(self,error_message,error_message_detail):
        super().__init__(error_message)
        self.error_message=get_error_detail(error_message,error_message_detail)
    
    def __str__(self):
        return self.error_message