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
        group_name="Modified Group",
        address2="address2",
        phone2="phone2",
        notes="notes"
    )
    app.contact_page.create(new_contact)
    app.session.logout()
    # self.assertTrue(success)


def test_add_empty_contact(app):
    # success = True
    app.session.login(user_name="admin", password="secret")
    new_contact = Contact()
    app.contact_page.create(new_contact)
    app.session.logout()
    # self.assertTrue(success)


def test_modify_contact(app):
    # success = True
    app.session.login(user_name="admin", password="secret")
    contact_to_modify = Contact(
        first_name="first_name",
        last_name="last_name",)

    new_contact = Contact(
        first_name="first_name1",
        middle_name="middle_name1",
        last_name="last_name1",
        nickname="nickname1",
        title="title1",
        company="company1",
        address="address1",
        home_phone="home_phone1",
        mobile_phone="mobile_phone1",
        work_phone="work_phone1",
        fax_phone="fax_phone1",
        email="email-1",
        email2="email2-1",
        email3="email3-1",
        homepage="homepage-1",
        birth_date=date(1801, 5, 5),
        anniversary_date=date(1901, 7, 7),
        address2="address2-1",
        phone2="phone2-1",
        notes="notes-1"
    )
    app.contact_page.edit(contact_to_modify, new_contact)
    app.session.logout()
    # self.assertTrue(success)


def test_delete_contact(app):
    # success = True
    app.session.login(user_name="admin", password="secret")
    delete_contact = Contact(
        first_name="first_name",
        last_name="last_name",)
    app.contact_page.delete(delete_contact)
    app.session.logout()
    # self.assertTrue(success)


def test_delete_first_contact(app):
    # success = True
    app.session.login(user_name="admin", password="secret")
    app.contact_page.delete_first()
    app.session.logout()
    # self.assertTrue(success)
