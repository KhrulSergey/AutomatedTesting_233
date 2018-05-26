# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from Models.contact import Contact
from datetime import date

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_add_new_contact(self):
        # success = True
        wd = self.wd
        self.open_home(wd)
        self.login(wd, user_name="admin", password="secret")
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
            birth_date=date(1800,1,1),
            anniversary_date=date(1900,2,2),
            address2="address2",
            phone2="phone2",
            notes="notes"
        )
        self.add_contact(wd, new_contact)
        self.return_to_contact_list(wd)
        self.logout(wd)
        # self.assertTrue(success)

    def return_to_contact_list(self, wd):
        """Return to Contact lis"""
        wd.find_element_by_link_text("home").click()

    def open_home(self, wd):
        """Open home_phone page"""
        wd.get("http://localhost/addressbook/")

    """Login to system"""
    def login(self, wd, user_name, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def add_contact(self, wd, contact):
        """Add new contact"""
        wd.find_element_by_link_text("add new").click()
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
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
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
        wd.find_element_by_name("homepage").send_keys("link to homepage")
        # Fill birthday date field
        b_day = (contact.birth_date.day + 2).__str__()
        b_month = (contact.birth_date.month + 1).__str__()
        b_year = contact.birth_date.year.__int__()
        print(b_day,b_month)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[" + b_day + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[" + b_day + "]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[" + b_month + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[" + b_month + "]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(b_year)
        # Fill anniversary date field
        a_day = (contact.anniversary_date.day + 2).__str__()
        a_month = (contact.anniversary_date.month + 1).__str__()
        a_year = contact.anniversary_date.year.__int__()
        print(a_day, a_month)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[" + a_day + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[" + a_day + "]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[" + a_month + "]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[" + a_month + "]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(a_year)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[5]//option[4]").click()
        # Fill adress fields
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("Additional adress")
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("Home field")
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("Additional notes")
        wd.find_element_by_name("submit").click()

    def logout(self, wd):
        """Logout"""
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
