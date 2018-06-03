

__author__ = 'Sergey Khrul'


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
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

    def return_to_contact_list(self):
        wd = self.app.wd
        """Return to Contact lis"""
        wd.find_element_by_link_text("home").click()
