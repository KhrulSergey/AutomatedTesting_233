__author__ = 'Sergey Khrul'

import pytest
from controller.application import Application

Fixture = None


@pytest.fixture()
def app(request):
    global Fixture
    if Fixture is None or not Fixture.is_valid():
        Fixture = Application()
    else:
        Exception("No Fixture was initialized")
    Fixture.session.ensure_login(user_name="admin", password="secret")
    return Fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        Fixture.session.ensure_logout()
        Fixture.destroy()
    request.addfinalizer(fin)
    return Fixture


