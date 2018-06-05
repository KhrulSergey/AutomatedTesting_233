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
    app.group_page.create(Group())
    app.session.logout()
    # self.assertTrue(success)


def test_edit_group(app):
    group_to_edit = Group(name="test group")
    group_modified = Group(name="Modified Group", footer="Modified footer", header="Modified header")
    app.session.login(user_name="admin", password="secret")
    app.group_page.edit(group_to_edit, group_modified)
    app.session.logout()


def test_del_first_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group_page.delete_first()
    app.session.logout()


def test_del_group(app):
    group_to_delete = Group(name="test group")
    app.session.login(user_name="admin", password="secret")
    app.group_page.delete(group_to_delete)
    app.session.logout()
