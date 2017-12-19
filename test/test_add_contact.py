# -*- coding: utf-8 -*-
import unittest
from model.contact import Contact
import random
import string
import pytest


def random_string(prefix, maxlen):
    # symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# testdata = Contact(name="test", middle_name="test", last_name="test", nickname="test", title="test", company="test", address="test", telephone_home="test", telephone_mobile="test",
#              telephone_work="test", fax="test", email_1="test", email_2="test", email_3="test", homepage="test", birthday_option_1=4, birthday_option_2=2,
#              birthday_year="2010", anniversary_option_1=3, anniversary_option_2=3, anniversary_year="2010", secondary_address="test", home="test", notes="test")

testdata = [Contact("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")] + [
        Contact(name=random_string("name", 10), middle_name=random_string("middle_name", 10), last_name=random_string("last_name", 20), nickname=random_string("nickname", 10), title=random_string("title", 10),
                company=random_string("company", 10), address=random_string("address", 20), telephone_home=random_string("telephone_home", 10),
                telephone_mobile=random_string("telephone_mobile", 10), telephone_work=random_string("telephone_work", 10), fax=random_string("fax", 10),
                email_1=random_string("email_1", 10), email_2=random_string("email_2", 10), email_3=random_string("email_3", 10), homepage=random_string("homepage", 10),
                secondary_address=random_string("secondary_address", 10), home=random_string("home", 10), notes=random_string("notes", 10), id=None,
                 all_telephones_from_home_page=None, all_emails_from_home_page=None)
        for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_test_add_contact(app, contact):

    old_contacts = app.contact.get_contact_list()
    app.contact.open_new_contact_page()

    app.contact.add_new_contact(contact)

    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


if __name__ == '__main__':
    unittest.main()
