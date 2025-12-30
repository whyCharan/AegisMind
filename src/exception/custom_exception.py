import sys 

class AegisMindException(Exception):

    # Custom exception class for AegisMind

    def __init__(self, error_message: str, error_details: sys):
        super().__init__(error_message)
        _, _, tb = error_details.exc_info()
        self.lineno = tb.tb_lineno
        self.file_name = tb.tb_frame.f_code.co_filename
        self.error_message = error_message

    def __str__(self):
        return f"Error occurred in script : {self.file_name} at line number : {self.lineno} error message : {self.error_message}"
