# -*- coding: utf-8 -*-
import pytest
from controler.application import Application
from models.group import Group

__author__ = 'Sergey Khrul'

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    # success = True
    app.session.login(user_name="admin", password="secret")
    app.group.create(Group(name="test group", header="New Test Header", footer="New group footer"))
    app.session.logout()
    # self.assertTrue(success)


def test_add_null_group(app):
    # success = True
    app.session.login(user_name="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
    # self.assertTrue(success)

