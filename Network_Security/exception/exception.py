import sys

from Network_Security.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self,errmessage,error_detail:sys):
        super().__init__(errmessage)
        _, _, exc_tb = error_detail.exc_info()
        self.errmessage = errmessage
        self.error_detail = error_detail
        super().__init__(self.errmessage)
        self.lineno=exc_tb.tb_lineno
        self.filename=exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occurred in script: {self.filename} at line number: {self.lineno} with error message: {self.errmessage}"
        self.filename,self.lineno,self.errmessage


# if __name__ == "__main__":
#     try:
#         logger.logging.info("Enter the try block")
#         a=1/0
#         print("This will not be printed")
#     except Exception as e:
#         raise NetworkSecurityException(e,sys)