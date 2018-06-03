# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from controler.session import SessionHelper

__author__ = 'Sergey Khrul'

class Application:
    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def create_group(self, group):
        wd = self.wd
        # Open page
        self.open_groups_page()
        # Init group creation
        wd.find_element_by_name("new").click()
        # Fill group fields
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        # Return to page
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.wd
        # Open Group page
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.wd
        # Return to Group page
        wd.find_element_by_link_text("group page").click()

    def open_home_page(self):
        wd = self.wd
        # open home_phone page
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
