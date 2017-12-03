# -*- coding: utf-8 -*-
import unittest

import pytest

from fixture.application import Application
from model.contact import Contact


def test_test_add_contact(app):
    #test
    #wd = self.wd
    #app.open_home_page()
    #app.session.login("admin", "secret")
    old_contacts = app.contact.get_contact_list()
    app.contact.open_new_contact_page()
    contact = Contact(name="test", middle_name="test", last_name="test", nickname="test", title="test", company="test", address="test", telephone_home="test", telephone_mobile="test",
             telephone_work="test", fax_work="test", email_1="test", email_2="test", email_3="test", homepage="test", birthday_option_1=4, birthday_option_2=2,
             birthday_year="2010", anniversary_option_1=3, anniversary_option_2=3, anniversary_year="2010", secondary_address="test", home="test", notes="test")
    app.contact.add_new_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

    old_contacts.append(contact)

    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    #app.session.logout()


if __name__ == '__main__':
    unittest.main()
