__author__ = 'Sergey Khrul'

import pytest
from controller.application import Application
from controller.application import BrowserTypeEnum
import json
import os.path

Fixture = None
Config = None
DefaultConfigFileName = "config.json"

@pytest.fixture()
def app(request):
    global Fixture
    global Config
    if Config is None:
        Config = __read_config__(get_config_directory(request.config.getoption("--conf")))
    browser_type = request.config.getoption("--browser")
    if Fixture is None or not Fixture.is_valid():
        Fixture = Application(browser_type=browser_type, main_url=Config['mainURL'])
    else:
        Exception("No Fixture was initialized")
    Fixture.session.ensure_login(user_name=Config['username'], password=Config['password'])
    return Fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        Fixture.session.ensure_logout()
        Fixture.destroy()
    request.addfinalizer(fin)
    return Fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='chrome')
    parser.addoption("--conf", action='store', default=DefaultConfigFileName)


def get_config_directory(config_file_name):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), config_file_name)


def __read_config__(json_file):
    '''
    Read all config data from file
    :param json_file: Config file
    :return: List of configuration
    '''
    config = None
    try:
        config_file = open(json_file)
        config = json.load(config_file)
    except:
        print("\n\nError in conf file! Please check! \n")
    finally:
        config_file.close()
    return config
