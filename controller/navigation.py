__author__ = 'Sergey Khrul'


class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        # open home_phone page
        wd.get(self.app.mainURL)

    def ensure_home_opened(self):
        wd = self.app.wd
        # open home_phone page
        # TODO Check if the browser is opened
        if wd.current_url is not self.app.mainURL:
            self.open_home_page()
