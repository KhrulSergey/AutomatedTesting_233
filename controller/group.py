from models.group import Group
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
__author__ = 'Sergey Khrul'


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def get_list(self):
        wd = self.app.wd
        # Open page
        self.open_groups_page()
        groups_list = []
        list_of_groups_name = wd.find_elements(By.CSS_SELECTOR, "span.group")
        for element in list_of_groups_name:
            group_name = element.text if element.text else None  # check if '' then it should be None
            group_id = element.find_element(By.NAME, "selected[]").get_attribute('value')
            groups_list.append(Group(name=group_name, _id=group_id))
        return groups_list

    def create(self, group: Group):
        wd = self.app.wd
        # Open page
        self.open_groups_page()
        # Init group creation
        wd.find_element_by_name("new").click()
        self._fill_fields_(group)
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
        self._fill_fields_(modified_group)
        # Submit group edition
        wd.find_element_by_name("update").click()
        # Return to group page
        self.open_groups_page()

    def edit_first(self, modified_group: Group):
        wd = self.app.wd
        # Open group page
        self.open_groups_page()
        self._select_first_group_()
        # submit deletion
        wd.find_element_by_name("edit").click()
        # Fill all fields
        self._fill_fields_(modified_group)
        # Submit group edition
        wd.find_element_by_name("update").click()
        # Return to group page
        self.open_groups_page()

    def delete_first(self):
        wd = self.app.wd
        # Open group page
        self.open_groups_page()
        self._select_first_group_()
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
        group_url = self.app.mainURL + self.app.groupPathURL
        key_element = wd.find_elements(By.NAME, 'new')
        if wd.current_url is not group_url and len(key_element) == 0:
            # Open Group page
            wd.find_element_by_link_text("groups").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        # Select all groups
        group_list = wd.find_elements_by_name("selected[]")
        return len(group_list)

    def _select_first_group_(self):
        # choose first group
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def _fill_fields_(self, group: Group):
        # Fill group fields
        self._change_field_value_(locator="group_name", field_value=group.name)
        self._change_field_value_(locator="group_header", field_value=group.header)
        self._change_field_value_(locator="group_footer", field_value=group.footer)

    # TODO create additional class for helpers
    def _change_field_value_(self, locator, field_value):
        wd = self.app.wd
        if field_value is not None:
            # TODO check Element is Present
            value_filed = wd.find_element_by_name(locator)
            value_filed.click()
            value_filed.clear()
            value_filed.send_keys(field_value)
