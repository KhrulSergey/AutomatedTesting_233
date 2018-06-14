# -*- coding: utf-8 -*-
from models.contact import Contact
from datetime import date

__author__ = 'Sergey Khrul'


def test_add_new_contact(app):
    # success = True
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
    # self.assertTrue(success)


def test_add_empty_contact(app):
    # success = True
    new_contact = Contact()
    app.contact_page.create(new_contact)
    # self.assertTrue(success)


def test_modify_contact(app):
    # success = True
    contact_to_modify = Contact(
        first_name="first_name",
        last_name="last_name",)
    # TODO check if definite contact exist. Not count
    if app.contact_page.count() == 0:
        app.contact_page.create(contact_to_modify)
    new_contact = Contact(
        first_name="first_name1",
        middle_name="middle_name1",
        last_name="last_name1",
        phone2="phone2-1",
        notes="notes-1"
    )
    app.contact_page.edit(contact_to_modify, new_contact)
    # self.assertTrue(success)


def test_delete_contact(app):
    # success = True
    delete_contact = Contact(
        first_name="first_name1",
        last_name="last_name1",)
    if app.contact_page.count() == 0:
        app.contact_page.create(delete_contact)
    app.contact_page.delete(delete_contact)
    # self.assertTrue(success)


def test_delete_first_contact(app):
    # success = True
    if app.contact_page.count() == 0:
        app.contact_page.create(Contact(first_name="first_name1", last_name="last_name1"))
    app.contact_page.delete_first()
    # self.assertTrue(success)
