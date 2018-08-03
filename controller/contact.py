from models.contact import Contact
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from datetime import date
import re

__author__ = 'Sergey Khrul'


class ContactHelper:

    def __init__(self, app):
        self.app = app

    contact_cache = None

    def get_list(self):
        '''Get all Contact's info from home page'''
        if self.contact_cache is None:
            wd = self.app.wd
            # Open page
            self.open_contacts_page()
            self.contact_cache = []
            # TODO check if it can be optimized
            # find contact table
            table = wd.find_element(By.ID, 'maintable')
            contact_entity_list = table.find_elements(By.CSS_SELECTOR, 'tr')

            # pass Headers of Table
            for element in contact_entity_list[1:]:
                # find list of contacts

                contact_fields = element.find_elements(By.CSS_SELECTOR, 'td')
                contact_lname = contact_fname = contact_address = None
                all_phones = None
                contact_home_phone = contact_work_phone = contact_mobile_phone = contact_phone2 = None
                if contact_fields:
                    # find and save fields of contact
                    # check for each if '' then it should be None
                    contact_lname = contact_fields[1].text if contact_fields[1].text else None
                    contact_fname = contact_fields[2].text if contact_fields[2].text else None

                    # It's not true if not all phone fields added to Contact page
                    # It's should be deleted or used carefully
                    if contact_fields[5]:
                        all_phones = contact_fields[5].text

                        # all_phones.splitlines()
                        # if len(all_phones) == 4:
                        #     contact_home_phone = all_phones[0]
                        #     contact_mobile_phone = all_phones[1]
                        #     contact_work_phone = all_phones[2]
                        #     contact_phone2 = all_phones[3]

                # find ID of contact
                contact_id = contact_fields[0].find_element(By.NAME, "selected[]").get_attribute('value')
                self.contact_cache.append(Contact(_id=contact_id, first_name=contact_fname, last_name=contact_lname,
                                                  address=contact_address, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def create(self, contact):
        '''Create new contact'''
        wd = self.app.wd
        self.open_contacts_page()
        # Add new contact
        wd.find_element_by_link_text("add new").click()
        self._set_all_fields_(contact)
        # Submit addition
        wd.find_element_by_name("submit").click()
        # Return to Contact page
        self.open_contacts_page()
        self._clear_cache_()

    def edit(self, original_contacts: Contact, modified_contacts: Contact):
        '''Fins and modify some fileds in Contact
         Takes original_contacts as contact to Find
         Takes modified_contacts as fields to Modify'''
        wd = self.app.wd
        self.open_contacts_page()

        # TODO check why the code stopped working
        # # Select contact to modify
        # contact_check_box = wd.find_element_by_xpath("(//input[@name='selected[]' and @title='Select (" +
        #                                              original_contacts.first_name + " " + original_contacts.last_name + ")'])")
        # # Select button to click
        # wd.find_element(By.CSS_SELECTOR, "a[href*='edit.php?id=" + contact_check_box.get_attribute("id") + "']").click()

        wd.find_element(By.CSS_SELECTOR, "a[href*='edit.php?id=" + original_contacts.id + "']").click()
        # Fill all modified fields
        self._set_all_fields_(modified_contacts, True)
        # Submit modification
        wd.find_element_by_name("update").click()
        # Return to Contact page
        self.open_contacts_page()
        self._clear_cache_()

    def delete(self, contact: Contact):
        '''Delete exact contact from List'''
        wd = self.app.wd
        self.open_contacts_page()
        # Select contact to delete
        self._select_by_id_(contact.id)  # self._select_by_name_(contact.first_name, contact.last_name)
        # Click delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        # Return to Contact page
        self.open_contacts_page()
        self._clear_cache_()

    def delete_first(self):
        '''Old method: Delete the first contact'''
        self.delete_by_index(0)

    def delete_by_index(self, index: int):
        '''Delete some contact by index'''
        wd = self.app.wd
        self.open_contacts_page()
        # Select contact to modify
        self._select_by_index_(index)
        # Submit delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # Accept confirmation
        wd.switch_to_alert().accept()
        # Return to Contact page
        self.open_contacts_page()
        self._clear_cache_()

    def open_contacts_page(self):
        '''Open contact home page'''
        wd = self.app.wd
        contact_url = self.app.mainURL + self.app.contactPathURL
        if wd.current_url is not contact_url:
            # Open Contact page
            wd.find_element_by_link_text("home").click()

    def count(self):
        '''Count the length of Contact List'''
        wd = self.app.wd
        self.open_contacts_page()
        # Select all contacts
        contact_list = wd.find_elements_by_name("selected[]")
        return len(contact_list)

    def get_info_from_edit_page(self, index: int):
        '''Get all data from Edit Form of index'es Contact'''
        wd = self.app.wd
        self._open_edit_page_by_index_(index)
        contact = self._get_fields_from_edit_()
        return contact

    def get_info_from_view_page(self, index: int):
        '''Get all date from VIEW Form of index'es Contact'''
        wd = self.app.wd
        self._open_view_page_by_index_(index)
        contact = self._get_fields_from_view_()
        return contact

    # ------------------------------------
    # Additional closed methods for Support
    # ------------------------------------

    def _clear_cache_(self):
        self.contact_cache = None

    def _select_by_id_(self, _id: int):
        wd = self.app.wd
        wd.find_element(By.XPATH, "(//input[@value='" + str(_id) + "'])").click()

    def _select_by_name_(self, first_name: str, last_name: str):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='selected[]' and @title='Select (" + first_name + " " + last_name + ")'])").click()

    def _select_by_index_(self, index: int):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def _open_edit_page_by_index_(self, index: int):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def _open_view_page_by_index_(self, index: int):
        wd = self.app.wd
        self.open_contacts_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def _set_all_fields_(self, contact: Contact, is_edit=False):
        wd = self.app.wd
        # Fill main fields
        self._set_field_value_(By.NAME, "firstname", contact.first_name)
        self._set_field_value_(By.NAME, "middlename", contact.middle_name)
        self._set_field_value_(By.NAME, "lastname", contact.last_name)
        self._set_field_value_(By.NAME, "nickname", contact.nickname)

        # Fill companies fields
        self._set_field_value_(By.NAME, "company", contact.company)
        self._set_field_value_(By.NAME, "title", contact.title)
        self._set_field_value_(By.NAME, "address", contact.address)

        # Fill phones fields
        self._set_field_value_(By.NAME, "home", contact.home_phone)
        self._set_field_value_(By.NAME, "mobile", contact.mobile_phone)
        self._set_field_value_(By.NAME, "work", contact.work_phone)
        self._set_field_value_(By.NAME, "fax", contact.fax_phone)

        # Fill email fields
        self._set_field_value_(By.NAME, "email", contact.email)
        self._set_field_value_(By.NAME, "email2", contact.email2)
        self._set_field_value_(By.NAME, "email3", contact.email3)
        self._set_field_value_(By.NAME, "homepage", contact.homepage)

        # Fill birthday date field
        if contact.birth_date is not date.min and contact.birth_date is not None:
            b_day = contact.birth_date.day.__str__()
            b_month = contact.birth_date.strftime("%B")
            b_year = contact.birth_date.year.__int__()
        else:
            b_day = None
            b_month = None
            b_year = None

        self._set_select_value_(By.XPATH, "//div[@id='content']/form/select[1]", b_day)
        self._set_select_value_(By.XPATH, "//div[@id='content']/form/select[2]", b_month)
        self._set_field_value_(By.NAME, "byear", b_year)

        # Fill anniversary date field
        if contact.anniversary_date is not date.min and contact.anniversary_date is not None:
            a_day = contact.anniversary_date.day.__str__()
            a_month = contact.anniversary_date.strftime("%B")
            a_year = contact.anniversary_date.year.__int__()
        else:
            a_day = None
            a_month = None
            a_year = None

        self._set_select_value_(By.XPATH, "//div[@id='content']/form/select[3]", a_day)
        self._set_select_value_(By.XPATH, "//div[@id='content']/form/select[4]", a_month)
        self._set_field_value_(By.NAME, "ayear", a_year)

        # Select group of contact.
        if not is_edit:
            # Get list of existed groups
            self._set_select_value_(By.XPATH, "//div[@id='content']/form/select[5]", contact.group_name)

        # Fill address fields

        self._set_field_value_(By.NAME, "address2", contact.address2)
        self._set_field_value_(By.NAME, "phone2", contact.phone2)
        self._set_field_value_(By.NAME, "notes", contact.notes)

    def _get_fields_from_edit_(self):
        wd = self.app.wd
        contact = Contact()
        # GET main fields
        contact.id = self._get_field_value_(By.NAME, "id")
        contact.first_name = self._get_field_value_(By.NAME, "firstname")
        contact.middle_name = self._get_field_value_(By.NAME, "middlename")
        contact.last_name = self._get_field_value_(By.NAME, "lastname")
        contact.nickname = self._get_field_value_(By.NAME, "nickname")

        # GET companies fields
        contact.company = self._get_field_value_(By.NAME, "company")
        contact.title = self._get_field_value_(By.NAME, "title")
        contact.address = self._get_field_value_(By.NAME, "address")

        # GET phones fields
        contact.home_phone = self._get_field_value_(By.NAME, "home")
        contact.mobile_phone = self._get_field_value_(By.NAME, "mobile")
        contact.work_phone = self._get_field_value_(By.NAME, "work")
        contact.fax_phone = self._get_field_value_(By.NAME, "fax")

        # GET email fields
        contact.email = self._get_field_value_(By.NAME, "email")
        contact.email2 = self._get_field_value_(By.NAME, "email2")
        contact.email3 = self._get_field_value_(By.NAME, "email3")
        contact.homepage = self._get_field_value_(By.NAME, "homepage")

        # TODO do some stuff for get value of selector
        # GET birthday date field
        # if contact.birth_date is not date.min and contact.birth_date is not None:
        #     b_day = contact.birth_date.day.__str__()
        #     b_month = contact.birth_date.strftime("%B")
        #     b_year = contact.birth_date.year.__int__()
        # else:
        #     b_day = None
        #     b_month = None
        #     = None
        # self._set_select_value_(By.XPATH, "//div[@id='content']/form/select[1]", b_day)
        # self._set_select_value_(By.XPATH, "//div[@id='content']/form/select[2]", b_month)
        # b_year = self._get_field_value_(By.NAME, "byear", b_year)
        # contact.birth_date = date(b_year,b_month,b_day)

        # GET anniversary date field
        # if contact.anniversary_date is not date.min and contact.anniversary_date is not None:
        #     a_day = contact.anniversary_date.day.__str__()
        #     a_month = contact.anniversary_date.strftime("%B")
        #     a_year = contact.anniversary_date.year.__int__()
        # else:
        #     a_day = None
        #     a_month = None
        #     a_year = None
        # self._set_select_value_(By.XPATH, "//div[@id='content']/form/select[3]", a_day)
        # self._set_select_value_(By.XPATH, "//div[@id='content']/form/select[4]", a_month)
        # a_year = self._get_field_value_(By.NAME, "ayear")
        # contact.birth_date = date(a_year, a_month, a_day)

        # GET address fields
        contact.address2 = self._get_field_value_(By.NAME, "address2")
        contact.phone2 = self._get_field_value_(By.NAME, "phone2")
        contact.notes = self._get_field_value_(By.NAME, "notes")
        # Return founded fields
        return contact

    # TODO make this method read all information from view page
    def _get_fields_from_view_(self):
        wd = self.app.wd
        contact = Contact()
        the_whole_data = wd.find_element(By.ID, 'content').text
        contact.home_phone = re.search("H: (.*)", the_whole_data).group(1)
        contact.mobile_phone = re.search("M: (.*)", the_whole_data).group(1)
        contact.work_phone = re.search("W: (.*)", the_whole_data).group(1)
        contact.fax_phone = re.search("F: (.*)", the_whole_data).group(1)
        contact.phone2 = re.search("P: (.*)", the_whole_data).group(1)

        return contact

    # TODO create additional class for helpers
    def _set_field_value_(self, locator_by: By, locator_value, field_value):
        wd = self.app.wd
        if field_value is not None:
            # TODO check Element is Present
            value_filed = wd.find_element(locator_by, locator_value)
            value_filed.click()
            value_filed.clear()
            value_filed.send_keys(field_value)

    def _set_select_value_(self, locator_by: By, locator_value, field_value):
        wd = self.app.wd
        if field_value is not None:
            # TODO check Element is Present
            locator_value = Select(wd.find_element(locator_by, locator_value))
            # TODO check Select_element is Present
            locator_value.select_by_visible_text(field_value)

    def _get_field_value_(self, locator_by: By, locator_value):
        wd = self.app.wd
        # TODO check Element is Present
        value_filed = wd.find_element(locator_by, locator_value)
        return value_filed.get_attribute('value')

    def _get_select_value_(self, locator_by: By, locator_value):
        wd = self.app.wd
        # TODO check Element is Present
        locator_value = Select(wd.find_element(locator_by, locator_value))
        value = locator_value.__getattribute__('value')
        return wd.find_element(locator_by, locator_value).text
