# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from contact import Contact
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test_add_contact(app):
    #test
    #wd = self.wd
    app.open_home_page()
    app.login("admin", "secret")
    app.open_new_contact_page()
    app.add_new_contact(Contact(name="test", middle_name="test", last_name="test", nickname="test", title="test", company="test", address="test", telephone_home="test", telephone_mobile="test",
             telephone_work="test", fax_work="test", email_1="test", email_2="test", email_3="test", homepage="test", birthday_option_1=4, birthday_option_2=2,
             birthday_year="2010", anniversary_option_1=3, anniversary_option_2=3, anniversary_year="2010", secondary_address="test", home="test", notes="test"))
    app.logout()


if __name__ == '__main__':
    unittest.main()
