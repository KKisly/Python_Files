import pytest
import json
import os.path

from fixture.application import Application

target1 = None
fixture = None
test = 0
#target = None

@pytest.fixture
#@pytest.fixture(scope = "session")
def app(request):
    global fixture
    global target1
    browser = request.config.getoption("--browser")
    if target1 is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--target1"))
        with open(config_file) as f:
            target1 = json.load(f)
    #base_url = request.config.getoption("--baseUrl")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target1['baseUrl'])
    # elif fixture.is_valid() != True:
    #     fixture = Application(browser=browser, base_url=base_url)
    fixture.session.ensure_login(username=target1['username'], password=target1['password'])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    #parser.addoption("--baseUrl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--target1", action="store", default="target.json")