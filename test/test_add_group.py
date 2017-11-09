# -*- coding: utf-8 -*-
#from selenium.webdriver.common.action_chains import ActionChains
#import time, unittest
import unittest

import pytest

from fixture.application import Application
from model.group import Group

def test_test_add_group(app):
        #test method
        #wd = self.wd
        #app.open_home_page()
        #app.session.login(username = "admin", password = "secret")
        app.group.open_groups_page()
        app.group.create(Group("Test", "TestTest", "TestTestTest"))
        app.group.retrun_to_groups_page()
        #app.session.logout()
        #self.assertTrue(success)

def test_add_empty_group(app):
    #test method
    #wd = self.wd
    #app.open_home_page()
    #app.session.login(username = "admin", password = "secret")
    app.group.open_groups_page()
    app.group.create(Group("", "", ""))
    app.group.retrun_to_groups_page()
    #app.session.logout()


if __name__ == '__main__':
    unittest.main()
