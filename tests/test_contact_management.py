# -*- coding: utf-8 -*-
from models.contact import Contact
from datetime import date
from random import randrange
import re

__author__ = 'Sergey Khrul'


FULLCONTACT  = new_contact = Contact(
        first_name="first_name",
        middle_name="middle_name",
        last_name="last_name",
        nickname="nickname",
        title="title",
        company="company",
        address="address",
        home_phone="+783(546)33h",
        mobile_phone="883(546)33m",
        work_phone="56-78-23w",
        fax_phone="56-78-45f",
        email="email",
        email2="email2",
        email3="email3",
        homepage="homepage",
        birth_date=date(1800, 1, 1),
        anniversary_date=date(1900, 2, 2),
        # group_name="Modified Group",
        address2="address2",
        phone2="+783-546-332p2",
        notes="notes",
)


def test_add_new_contact(app):
    # Get list of existing contacts
    old_contact_list = app.contact_page.get_list()
    new_contact = FULLCONTACT
    # Add new group to WEB
    app.contact_page.create(new_contact)

    # Assert result
    assert len(old_contact_list) + 1 == app.contact_page.count()  # additional assert for list length in case of exception
    # Get new list from WEB
    new_contact_list = app.contact_page.get_list()
    old_contact_list.append(new_contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


def test_add_empty_contact(app):
    # Get list of existing contacts
    old_contact_list = app.contact_page.get_list()
    new_contact = Contact()
    app.contact_page.create(new_contact)

    # Assert result
    assert len(old_contact_list) + 1 == app.contact_page.count()  # additional assert for list length in case of exception
    # Get new list from WEB
    new_contact_list = app.contact_page.get_list()
    old_contact_list.append(new_contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)


def test_modify_contact(app):
    # Get list of existing contacts
    old_contact_list = app.contact_page.get_list()
    contact_to_modify = Contact(
        first_name="first_name",
        last_name="last_name",)
    # Check if certain contact exist in list
    if contact_to_modify not in old_contact_list:
        app.group_page.create(contact_to_modify)  # if not then we create new contact
        old_contact_list = app.contact_page.get_list()

    # Find certain contact in list and determinate its ID
    modified_contact_index = old_contact_list.index(contact_to_modify)
    contact_to_modify.id = old_contact_list[modified_contact_index].id
    # Determinate fields to modify in new entity
    modified_contact = Contact(
        first_name="first_name1",
        middle_name="middle_name1",
        last_name="last_name1",
        phone2="phone2-1",
        notes="notes-1",
        _id=contact_to_modify.id
    )
    # Modify contact in WEB
    app.contact_page.edit(contact_to_modify, modified_contact)

    # Assert result
    assert len(old_contact_list) == app.contact_page.count()  # additional assert for list length in case of exception
    # Get updated contacts list
    new_contacts_list = app.contact_page.get_list()
    # Change modified contact in old list
    old_contact_list[modified_contact_index] = modified_contact
    # Assert result
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contacts_list, key=Contact.id_or_max)


def test_delete_contact(app):
    # Get list of existing contacts
    contacts_list = app.contact_page.get_list()
    contact_to_delete = Contact(
        first_name="first_name1",
        last_name="last_name1",)
    # Check if certain contact exist in list
    if contact_to_delete not in contacts_list:
        app.group_page.create(contact_to_delete)  # if not then we create new contact
        contacts_list = app.contact_page.get_list()
    # Find certain contact in list and save its ID
    contact_to_delete_index = contacts_list.index(contact_to_delete)
    contact_to_delete.id = contacts_list[contact_to_delete_index].id
    #  Delete certain contact from list
    app.contact_page.delete(contact_to_delete)

    # Assert result
    assert len(contacts_list) - 1 == app.contact_page.count()  # check new length of contacts list
    # Get updated contacts list
    contacts_list = app.contact_page.get_list()
    assert contact_to_delete not in contacts_list  # check for deleted element existed


def test_delete_some_contact(app):
    # Get list of existing contacts
    contact_to_delete = Contact(first_name="first_name1", last_name="last_name1")
    contacts_list_len = app.contact_page.count()
    # Check the lenght of contact list
    if contacts_list_len == 0:
        app.contact_page.create(contact_to_delete)

    contacts_list = app.contact_page.get_list()
    index = randrange(len(contacts_list))
    # Find first contact in list and save its ID
    contact_to_delete.id = contacts_list[index].id
    contact_to_delete.first_name = contacts_list[index].first_name
    contact_to_delete.first_name = contacts_list[index].last_name
    #  Delete first contact from list
    app.contact_page.delete_by_index(index)

    # Assert result
    assert len(contacts_list) - 1 == app.contact_page.count()  # check new length of contacts list
    # Get updated contacts list
    contacts_list = app.contact_page.get_list()
    assert contact_to_delete not in contacts_list  # check for deleted element existed


def test_check_phones_on_home_page_by_index(app):
    # Define index of check
    contact_index_to_check = 1
    contacts_list_len = app.contact_page.count()

    # Check the length of contact list
    while contacts_list_len <= contact_index_to_check:
        app.contact_page.create(FULLCONTACT)
        contacts_list_len = app.contact_page.count()

    # Get list of existing contacts
    contact_from_home_page = (app.contact_page.get_list())[contact_index_to_check]
    contact_from_edit_page = app.contact_page.get_info_from_edit_page(contact_index_to_check)

    # Merge all phone in one text element with RegExp and Join+Filter func
    all_phones = merge_phones_like_on_home_page(contact_from_edit_page)

    # Check fields
    assert all_phones == contact_from_home_page.all_phones_from_home_page


def test_check_phones_on_contact_view_page(app):
    # Define index of check
    contact_index_to_check = 0
    contacts_list_len = app.contact_page.count()

    # Check the length of contact list
    while contacts_list_len <= contact_index_to_check:
        app.contact_page.create(FULLCONTACT)
        contacts_list_len = app.contact_page.count()

    # Get list of existing contacts
    contact_from_view_page = app.contact_page.get_info_from_view_page(contact_index_to_check)
    contact_from_edit_page = app.contact_page.get_info_from_edit_page(contact_index_to_check)
    # Check fields
    assert contact_from_edit_page.work_phone == contact_from_view_page.work_phone
    assert contact_from_edit_page.home_phone == contact_from_view_page.home_phone
    assert contact_from_edit_page.mobile_phone == contact_from_view_page.mobile_phone
    assert contact_from_edit_page.phone2 == contact_from_view_page.phone2


def test_all_fields_on_home_page_by_index(app):
    # Define index of check
    contact_index_to_check = 0
    contacts_list_len = app.contact_page.count()

    # Check the length of contact list
    while contacts_list_len <= contact_index_to_check:
        app.contact_page.create(FULLCONTACT)
        contacts_list_len = app.contact_page.count()

    # Get list of existing contacts
    contact_from_home_page = (app.contact_page.get_list())[contact_index_to_check]
    contact_from_edit_page = app.contact_page.get_info_from_edit_page(contact_index_to_check)

    # Merge all phone in one text element with RegExp and Join+Filter func
    all_phones = merge_phones_like_on_home_page(contact_from_edit_page)
    # Merge all email in one text element with RegExp and Join+Filter func
    all_email = merge_email_like_on_home_page(contact_from_edit_page)

    # Check fields
    assert all_phones == contact_from_home_page.all_phones_from_home_page
    # Check fields
    assert all_email == contact_from_home_page.all_email_from_home_page
    # Check fields
    assert contact_from_edit_page.address == contact_from_home_page.full_address_from_home_page
    # Check fields
    assert contact_from_edit_page.first_name == contact_from_home_page.first_name
    assert contact_from_edit_page.last_name == contact_from_home_page.last_name

def clear_phone_num(phone_num):
    return re.sub("[(),-. ]", "", phone_num)


def merge_phones_like_on_home_page(contact: Contact):
    all_phones = "\n".join(filter(lambda x: x != '',  # filter all empty fields and pass all filled
                                  map(clear_phone_num,  # check all properties in RegEx function
                                      filter(lambda x: x is not None, [contact.home_phone,  # check for None phones
                                                                       contact.mobile_phone, contact.work_phone,
                                                                       contact.phone2]))))
    return all_phones

def merge_email_like_on_home_page(contact: Contact):
    all_email = "\n".join([contact.email, contact.email2, contact.email3])
    return all_email
