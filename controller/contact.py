from models.contact import Contact
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.webdriver import WebDriver

__author__ = 'Sergey Khrul'


class ContactHelper:

    def __init__(self, app):
        self.app = app

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
        wd.find_element_by_xpath("(//img[@alt='Edit'])[" + contact_check_box.get_attribute("id") + "]").click()
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
        # Open Group page
        wd.find_element_by_link_text("home").click()

    def _fill_field_(self, contact: Contact, is_edit=False):
        wd = self.app.wd

        # Fill main fields
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)

        # Fill companies fields
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)

        # Fill phones fields
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax_phone)

        # Fill email fields
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)

        # Fill birthday date field
        b_day = contact.birth_date.day.__str__()
        b_month = contact.birth_date.strftime("%B")
        b_year = contact.birth_date.year.__int__()

        select_b_day = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[1]"))
        select_b_day.select_by_visible_text(b_day)
        select_b_month = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[2]"))
        select_b_month.select_by_visible_text(b_month)

        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(b_year)

        # Fill anniversary date field
        a_day = contact.anniversary_date.day.__str__()
        a_month = contact.anniversary_date.strftime("%B")
        a_year = contact.anniversary_date.year.__int__()

        select_a_day = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[3]"))
        select_a_day.select_by_visible_text(a_day)
        select_a_month = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[4]"))
        select_a_month.select_by_visible_text(a_month)

        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(a_year)

        # Select group of contact.
        if not is_edit:
            select_a_day = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[5]"))
            select_a_day.select_by_visible_text(contact.group_name)

        # Fill address fields
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.homepage)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
