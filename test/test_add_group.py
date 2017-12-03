# -*- coding: utf-8 -*-
#from selenium.webdriver.common.action_chains import ActionChains
#import time, unittest
import unittest
from sys import maxsize

import pytest

from fixture.application import Application
from model.group import Group

def test_test_add_group(app):
        #test method
        app.group.open_groups_page()
        group = Group("Test", "TestTest", "TestTestTest")
        old_groups = app.group.get_group_list()
        app.group.create(group)

        assert len(old_groups) + 1 == app.group.count()
        new_groups = app.group.get_group_list()
        old_groups.append(group)

        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

#def test_add_empty_group(app):
#    app.group.open_groups_page()
#    group = Group("", "", "")
#    old_groups = app.group.get_group_list()
#    app.group.create(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) + 1 == len(new_groups)
#    old_groups.append(group)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#    #app.group.retrun_to_groups_page()


if __name__ == '__main__':
    unittest.main()
