# -*- coding: utf-8 -*-
import pytest
from Lesson_2.application import Application
from Models.group import Group

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    # success = True
    app.login(user_name="admin", password="secret")
    app.create_group(Group(name="test group", header="New Test Header", footer="New group footer"))
    app.logout()
    # self.assertTrue(success)


def test_add_null_group(app):
    # success = True
    app.login(user_name="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
    # self.assertTrue(success)