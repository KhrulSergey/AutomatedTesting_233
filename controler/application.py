# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from controler.session import SessionHelper
from controler.group import GroupHelper

__author__ = 'Sergey Khrul'


class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group_helper = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        # open home_phone page
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
