# -*- coding: utf-8 -*-
#from selenium.webdriver.common.action_chains import ActionChains
import pytest
import unittest
from sys import maxsize
from fixture.application import Application
from model.group import Group
import random
import string


def random_string(prefix, maxlen):
        #symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
        symbols = string.ascii_letters + string.digits + " " * 10
        return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group("", "", "")]# + [
        #Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
        #for i in range(5)
        #Group(name="test", header="testtest", footer="testtesttest")
        #Group("", "", "")
#]

# testdata = [
#         Group(name=name, header=header, footer=footer)
#         for name in ["", random_string("name", 10)]
#         for header in ["", random_string("header", 20)]
#         for footer in ["", random_string("footer", 20)]
#]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_test_add_group(app, group):
        #pass
        app.group.open_groups_page()
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
