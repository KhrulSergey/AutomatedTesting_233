from models.contact import Contact
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from datetime import date

__author__ = 'Sergey Khrul'


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def get_list(self):
        wd = self.app.wd
        # Open page
        self.open_contacts_page()
        contacts_list = []
        # TODO check if it can be optimized
        # find contact table
        table = wd.find_element(By.ID, 'maintable')
        contact_entity_list = table.find_elements(By.CSS_SELECTOR, 'tr'
                                                  )
        # pass Headers of Table
        for element in contact_entity_list[1:]:
            # find list of contacts
            contact_fields = element.find_elements(By.CSS_SELECTOR, 'td')
            contact_lname = contact_fname = contact_address = None
            if contact_fields:
                # find and save fields of contact
                # check for each if '' then it should be None
                contact_lname = contact_fields[1].text if contact_fields[1].text else None
                contact_fname = contact_fields[2].text if contact_fields[2].text else None
            # find ID of contact
            contact_id = contact_fields[0].find_element(By.NAME, "selected[]").get_attribute('value')
            contacts_list.append(Contact(_id=contact_id, first_name=contact_fname,
                                         last_name=contact_lname, address=contact_address))
        return contacts_list

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # Add new contact
        wd.find_element_by_link_text("add new").click()
        self._fill_field_(contact)
        # Submit addition
        wd.find_element_by_name("submit").click()
        # Return to Contact page
        self.open_contacts_page()

    def edit(self, original_contacts: Contact, modified_contacts: Contact):
        wd = self.app.wd
        self.open_contacts_page()
        # Select contact to modify
        contact_check_box = wd.find_element_by_xpath("(//input[@name='selected[]' and @title='Select (" +
                                                     original_contacts.first_name + " " + original_contacts.last_name + ")'])")
        # Select button to click
        wd.find_element(By.CSS_SELECTOR, "a[href*='edit.php?id=" + contact_check_box.get_attribute("id") + "']").click()
        # Fill all modified fields
        self._fill_field_(modified_contacts, True)
        # Submit modification
        wd.find_element_by_name("update").click()
        # Return to Contact page
        self.open_contacts_page()

    def delete(self, contact: Contact):
        wd = self.app.wd
        self.open_contacts_page()
        # Select contact to delete
        contact_check_box = wd.find_element_by_xpath("(//input[@name='selected[]' and @title='Select ("
                                                     + contact.first_name + " " + contact.last_name + ")'])")
        contact_check_box.click()
        # Click delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        # Return to Contact page
        self.open_contacts_page()

    def delete_first(self):
        wd = self.app.wd
        self.open_contacts_page()
        # Select contact to modify
        wd.find_element_by_name("selected[]").click()
        # Click delete
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # Accept confirmation
        wd.switch_to_alert().accept()
        # Return to Contact page
        self.open_contacts_page()

    def open_contacts_page(self):
        wd = self.app.wd
        contact_url = self.app.mainURL + self.app.contactPathURL
        if wd.current_url is not contact_url:
            # Open Contact page
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        # Select all contacts
        contact_list = wd.find_elements_by_name("selected[]")
        return len(contact_list)

    def _fill_field_(self, contact: Contact, is_edit=False):
        wd = self.app.wd
        # Fill main fields
        self._change_field_value_(By.NAME, "firstname", contact.first_name)
        self._change_field_value_(By.NAME, "middlename", contact.middle_name)
        self._change_field_value_(By.NAME, "lastname", contact.last_name)
        self._change_field_value_(By.NAME, "nickname", contact.nickname)

        # Fill companies fields
        self._change_field_value_(By.NAME, "company", contact.company)
        self._change_field_value_(By.NAME, "title", contact.title)
        self._change_field_value_(By.NAME, "address", contact.address)

        # Fill phones fields
        self._change_field_value_(By.NAME, "home", contact.home_phone)
        self._change_field_value_(By.NAME, "mobile", contact.mobile_phone)
        self._change_field_value_(By.NAME, "work", contact.work_phone)
        self._change_field_value_(By.NAME, "fax", contact.fax_phone)

        # Fill email fields
        self._change_field_value_(By.NAME, "email", contact.email)
        self._change_field_value_(By.NAME, "email2", contact.email2)
        self._change_field_value_(By.NAME, "email3", contact.email3)
        self._change_field_value_(By.NAME, "homepage", contact.homepage)

        # Fill birthday date field
        if contact.birth_date is not date.min and contact.birth_date is not None:
            b_day = contact.birth_date.day.__str__()
            b_month = contact.birth_date.strftime("%B")
            b_year = contact.birth_date.year.__int__()
        else:
            b_day = None
            b_month = None
            b_year = None

        self._change_select_value_(By.XPATH, "//div[@id='content']/form/select[1]", b_day)
        self._change_select_value_(By.XPATH, "//div[@id='content']/form/select[2]", b_month)
        self._change_field_value_(By.NAME, "byear", b_year)

        # Fill anniversary date field
        if contact.anniversary_date is not date.min and contact.anniversary_date is not None:
            a_day = contact.anniversary_date.day.__str__()
            a_month = contact.anniversary_date.strftime("%B")
            a_year = contact.anniversary_date.year.__int__()
        else:
            a_day = None
            a_month = None
            a_year = None

        self._change_select_value_(By.XPATH, "//div[@id='content']/form/select[3]", a_day)
        self._change_select_value_(By.XPATH, "//div[@id='content']/form/select[4]", a_month)
        self._change_field_value_(By.NAME, "ayear", a_year)

        # Select group of contact.
        if not is_edit:
            # Get list of existed groups
            self._change_select_value_(By.XPATH, "//div[@id='content']/form/select[5]", contact.group_name)

        # Fill address fields

        self._change_field_value_(By.NAME, "address2", contact.address2)
        self._change_field_value_(By.NAME, "phone2", contact.homepage)
        self._change_field_value_(By.NAME, "notes", contact.notes)

    # TODO create additional class for helpers
    def _change_field_value_(self, locator_by: By, locator_value, field_value):
        wd = self.app.wd
        if field_value is not None:
            # TODO check Element is Present
            value_filed = wd.find_element(locator_by, locator_value)
            value_filed.click()
            value_filed.clear()
            value_filed.send_keys(field_value)

    def _change_select_value_(self, locator_by: By, locator_value, field_value):
        wd = self.app.wd
        if field_value is not None:
            # TODO check Element is Present
            locator_value = Select(wd.find_element(locator_by, locator_value))
            # TODO check Select_element is Present
            locator_value.select_by_visible_text(field_value)
