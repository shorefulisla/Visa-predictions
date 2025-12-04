from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

try:
    a = 1 / 0
    print(a)
except Exception as e:
    raise USvisaException(e, sys) 


logging.info("This is an info mfsdkasdfasdf sdfessage from demo.py")