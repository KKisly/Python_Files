
import pytest

from fixture.application import Application

fixture = None

@pytest.fixture
#@pytest.fixture(scope = "session")
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.login(username="admin", password="secret")
    elif fixture.is_valid() != True:
        fixture = Application()
        fixture.session.login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture