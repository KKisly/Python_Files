import pytest
import json
import os.path
import importlib
import jsonpickle
from fixture.db import DbFixture

from fixture.application import Application

target1 = None
fixture = None

def load_config(file):
    global target1
    if target1 is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target1 = json.load(f)
    return target1



@pytest.fixture
#@pytest.fixture(scope = "session")
def app(request):
    global fixture
    #global target1
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target1"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
    # elif fixture.is_valid() != True:
    #     fixture = Application(browser=browser, base_url=base_url)
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target1"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    #parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--target1", action="store", default="target.json")

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_form_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_form_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())

