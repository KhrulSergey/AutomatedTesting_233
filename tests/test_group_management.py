# -*- coding: utf-8 -*-

from models.group import Group

__author__ = 'Sergey Khrul'


def test_add_new_group(app):
    # success = True
    app.session.login(user_name="admin", password="secret")
    app.group_page.create(Group(name="test group", header="New Test Header", footer="New group footer"))
    app.session.logout()
    # self.assertTrue(success)


def test_add_null_group(app):
    # success = True
    app.session.login(user_name="admin", password="secret")
    app.group_page.create(Group(name="", header="", footer=""))
    app.session.logout()
    # self.assertTrue(success)


