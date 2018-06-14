# -*- coding: utf-8 -*-

from models.group import Group

__author__ = 'Sergey Khrul'


def test_add_new_group(app):
    # success = True
    app.group_page.create(Group(name="test group", header="New Test Header", footer="New group footer"))
    # self.assertTrue(success)


def test_add_null_group(app):
    # success = True
    app.group_page.create(Group())
    # self.assertTrue(success)


def test_edit_group(app):
    group_to_edit = Group(name="test group")
    # TODO check if definite group exist. Not count
    if app.group_page.count() == 0:
        app.group_page.create(group_to_edit)
    # group_modified = Group(name="Modified Group", footer="Modified footer", header="Modified header")
    group_modified = Group(name="Modified Group")
    app.group_page.edit(group_to_edit, group_modified)


def test_edit_first_group(app):
    # group_modified = Group(name="Modified Group", footer="Modified footer", header="Modified header")
    if app.group_page.count() == 0:
        app.group_page.create(Group(name="test"))
    group_modified = Group(name="New Group")
    app.group_page.edit_first(group_modified)


def test_del_first_group(app):
    if app.group_page.count() == 0:
        app.group_page.create(Group(name="test"))
    app.group_page.delete_first()


def test_del_group(app):
    group_to_delete = Group(name="New Group")
    app.group_page.delete(group_to_delete)
