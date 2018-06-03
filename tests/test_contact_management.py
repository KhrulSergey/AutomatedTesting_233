# -*- coding: utf-8 -*-
from models.contact import Contact
from datetime import date

__author__ = 'Sergey Khrul'


def test_add_new_contact(app):
    # success = True
    app.session.login(user_name="admin", password="secret")
    new_contact = Contact(
        first_name="first_name",
        middle_name="middle_name",
        last_name="last_name",
        nickname="nickname",
        title="title",
        company="company",
        address="address",
        home_phone="home_phone",
        mobile_phone="mobile_phone",
        work_phone="work_phone",
        fax_phone="fax_phone",
        email="email",
        email2="email2",
        email3="email3",
        homepage="homepage",
        birth_date=date(1800, 1, 1),
        anniversary_date=date(1900, 2, 2),
        address2="address2",
        phone2="phone2",
        notes="notes"
    )
    app.contact_page.create(new_contact)
    app.contact_page.return_to_contact_list()
    app.session.logout()
    # self.assertTrue(success)



