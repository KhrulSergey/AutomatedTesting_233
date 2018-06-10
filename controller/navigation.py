__author__ = 'Sergey Khrul'

URL = "http://localhost:90/addressbook/"


class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        # open home_phone page
        # TODO Check if the page is opened
        wd.get(URL)

    def ensure_home_opened(self):
        wd = self.app.wd
        # open home_phone page
        # TODO Check if the page is opened
        if wd.current_url is not URL:
            self.open_home_page()
