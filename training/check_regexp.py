__author__ = 'Sergey Khrul'
# import re


# def clear_phone_num(phone_num):
#     return re.sub("[(),-. +]", "", phone_num)
#
#
# print(clear_phone_num('+7(931)602-988-4'))


from models.group import Group
from random import randrange
from random import choice
import pytest
import string




class BrowserTypeEnum(Enum):
   Firefox = webdriver.Firefox(capabilities={"marionette": False})
   Chrome = webdriver.Chrome()
   Edge = webdriver.Edge()
   IE_11 = webdriver.Ie()

   # @classmethod
   # def get_right_function(cls):
   #      if(cls.Firefox):
   #          return
   #     return