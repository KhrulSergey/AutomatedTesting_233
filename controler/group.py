

__author__ = 'Sergey Khrul'

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
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
        wd = self.app.wd
        # Open Group page
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        # Return to Group page
        wd.find_element_by_link_text("group page").click()