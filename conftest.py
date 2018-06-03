__author__ = 'Sergey Khrul'

import pytest
from controller.application import Application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture