from datetime import date
from sys import maxsize

import random
import string

__author__ = 'Sergey Khrul'

CONTACT_PRINT_FORMAT = "{id} - Full Name: {f_name} {l_name}."


class Contact:
    def __init__(self, _id=None, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None, address=None,
                 home_phone=None, mobile_phone=None, work_phone=None, fax_phone=None, email=None, email2=None, email3=None,
                 homepage=None, birth_date=date.min, anniversary_date=date.min, group_name=None,
                 address2=None, phone2=None, notes=None, all_phones=None):
        self.id = _id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax_phone = fax_phone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birth_date = birth_date
        self.anniversary_date = anniversary_date
        self.group_name = group_name
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.all_phones = all_phones

    def __repr__(self):
        return CONTACT_PRINT_FORMAT.format(id=self.id, f_name=self.first_name, l_name=self.last_name)

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name and \
               (self.id is None or other.id is None or self.id == other.id)

    def id_or_max(cntct):
        if cntct.id:
            return int(cntct.id)
        return maxsize

    def generate_str(self):
        list_of_rand_symbols = string.ascii_letters + string.digits
        max_number_of_letters = 20
        gen_str = ''.join([random.choice(list_of_rand_symbols) for i in range(random.randrange(max_number_of_letters))])
        return gen_str
