# -*- coding: utf-8 -*-
from selenium import webdriver
from controller.session import SessionHelper
from controller.group import GroupHelper
from controller.contact import ContactHelper
from controller.navigation import NavigationHelper
from enum import Enum


__author__ = 'Sergey Khrul'

GroupPathUrl = "group.php"
ContactPathURL = ""


class BrowserTypeEnum(Enum):
   Firefox = 'firefox'
   Chrome = 'chrome'
   Edge = 'edge'
   IE_11 = 'ie11'


class Application:
    def __init__(self, browser_type, main_url):
        '''
        Class Create Instance of WebDriver and all infrastructure for testing
        :param browser_type: Type of browser to run All Tests
        '''
        self.wd = self.__browser_type__(browser_type)
        # self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group_page = GroupHelper(self)
        self.contact_page = ContactHelper(self)
        self.navigation = NavigationHelper(self)
        self.mainURL = main_url
        self.groupPathURL = GroupPathUrl
        self.contactPathURL = ContactPathURL

    @staticmethod
    def __browser_type__(browser_type):
        if browser_type == BrowserTypeEnum.Firefox.value:
            driver_func = webdriver.Firefox(capabilities={"marionette": False})
        elif browser_type == BrowserTypeEnum.Edge.value:
            driver_func = webdriver.Edge()
        elif browser_type == BrowserTypeEnum.Chrome.value:
            driver_func = webdriver.Chrome()
        elif browser_type == BrowserTypeEnum.IE_11.value:
            driver_func = webdriver.Ie()
        else:
            raise ValueError('Unrecognized Browser type - %s. Check configuration.' % browser_type)

        return driver_func

    def is_valid(self):
        try:
            if self.wd.current_url:
                return True
        except:
            return False

    def destroy(self):
        self.wd.quit()

