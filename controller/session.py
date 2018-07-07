# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

__author__ = 'Sergey Khrul'


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, user_name, password):
        wd = self.app.wd
        # Check if the page is opened
        self.app.navigation.ensure_home_opened()
        # Login to system
        user_field = wd.find_element_by_name("user")
        user_field.click()
        user_field.clear()
        user_field.send_keys(user_name)
        pass_field = wd.find_element_by_name("pass")
        pass_field.click()
        pass_field.clear()
        pass_field.send_keys(password)
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
        return self._get_logged_user_() == user_name

    def _get_logged_user_(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div[@id='top']/form/b").text[1:-1]
