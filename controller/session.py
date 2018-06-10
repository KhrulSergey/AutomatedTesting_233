# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

__author__ = 'Sergey Khrul'


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, user_name, password):
        # TODO Check if the page is opened
        wd = self.app.wd
        self.app.navigation.ensure_home_opened()
        # Login to system
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def ensure_login(self, user_name, password):
        self.app.navigation.ensure_home_opened()
        if self._is_session_opened_():
            if self._is_session_correct_(user_name):
                return
            else:
                self.logout()
        self.login(user_name, password)

    def logout(self):
        # Logout
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self._is_session_opened_():
            self.logout()

    def _is_session_opened_(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0

    def _is_session_correct_(self, user_name):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div[@id='top']/form/b").text == '('+user_name+')'
