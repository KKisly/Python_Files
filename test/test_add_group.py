# -*- coding: utf-8 -*-
#from selenium.webdriver.common.action_chains import ActionChains
#import time, unittest
import unittest

import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_group(app):
        #test method
        #wd = self.wd
        app.open_home_page()
        app.login(username = "admin", password = "secret")
        app.open_groups_page()
        app.create_group(Group("Test", "TestTest", "TestTestTest" ))
        app.retrun_to_groups_page()
        app.logout()
        #self.assertTrue(success)

def test_add_empty_group(app):
    #test method
    #wd = self.wd
    app.open_home_page()
    app.login(username = "admin", password = "secret")
    app.open_groups_page()
    app.create_group(Group("", "", "" ))
    app.retrun_to_groups_page()
    app.logout()


if __name__ == '__main__':
    unittest.main()
