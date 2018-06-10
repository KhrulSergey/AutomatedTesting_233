__author__ = 'Sergey Khrul'

from datetime import date


class Contact:
    def __init__(self, first_name=None, middle_name=None, last_name=None, nickname=None, title=None, company=None, address=None,
                 home_phone=None, mobile_phone=None, work_phone=None, fax_phone=None, email=None, email2=None, email3=None,
                 homepage=None, birth_date=date.min, anniversary_date=date.min, group_name=None,
                 address2=None, phone2=None, notes=None):
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
