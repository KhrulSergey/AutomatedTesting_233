# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from controller.session import SessionHelper
from controller.group import GroupHelper
from controller.contact import ContactHelper
from controller.navigation import NavigationHelper

__author__ = 'Sergey Khrul'


class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group_page = GroupHelper(self)
        self.contact_page = ContactHelper(self)
        self.navigation = NavigationHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
