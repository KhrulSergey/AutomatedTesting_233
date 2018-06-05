from models.group import Group
from selenium.webdriver.firefox.webdriver import WebDriver

__author__ = 'Sergey Khrul'


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group: Group):
        wd = self.app.wd
        # Open page
        self.open_groups_page()
        # Init group creation
        wd.find_element_by_name("new").click()
        self._fill_field_(group)
        # Submit group creation
        wd.find_element_by_name("submit").click()
        # Return to group page
        self.open_groups_page()

    def edit(self, original_group: Group, modified_group: Group):
        wd = self.app.wd
        # Open group page
        self.open_groups_page()
        # choose group with required name
        group_check_box = wd.find_element_by_xpath("(//input[@name='selected[]' and @title='Select (" +
                                                   original_group.name + ")'])")
        group_check_box.click()
        # submit deletion
        wd.find_element_by_name("edit").click()
        self._fill_field_(modified_group)
        # Submit group edition
        wd.find_element_by_name("update").click()
        # Return to group page
        self.open_groups_page()

    def delete_first(self):
        wd = self.app.wd
        # Open group page
        self.open_groups_page()
        # choose 1st group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        # Return to group page
        self.open_groups_page()

    def delete(self, group: Group):
        wd = self.app.wd
        # Open group page
        self.open_groups_page()
        # choose group with required name
        group_check_box = wd.find_element_by_xpath("(//input[@name='selected[]' and @title='Select (" + group.name
                                                   + ")'])")
        group_check_box.click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        # Return to group page
        self.open_groups_page()

    def open_groups_page(self):
        wd = self.app.wd
        # Open Group page
        wd.find_element_by_link_text("groups").click()

    def _fill_field_(self, group: Group):
        wd = self.app.wd
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
