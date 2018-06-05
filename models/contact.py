__author__ = 'Sergey Khrul'

from datetime import date


class Contact:
    def __init__(self, first_name="", middle_name="", last_name="", nickname="", title="", company="", address="",
                 home_phone="", mobile_phone="", work_phone="", fax_phone="", email="", email2="", email3="",
                 homepage="", birth_date=date(1900, 1, 1), anniversary_date=date(1900, 2, 2), group_name="",
                 address2="", phone2="", notes=""):
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
