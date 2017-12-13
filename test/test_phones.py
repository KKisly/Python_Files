#from model.contact import Contact
from random import randrange
import re

def test_phones_on_home_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_telephones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

# def test_phones_on_contact_view_page(app):
#     contacts = app.contact.get_contact_list()
#     index = randrange(len(contacts))
#     contact_from_view_page = app.contact.get_contact_from_view_page(index)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_view_page.telephone_home == contact_from_edit_page.telephone_home
#     assert contact_from_view_page.telephone_work == contact_from_edit_page.telephone_work
#     assert contact_from_view_page.telephone_mobile == contact_from_edit_page.telephone_mobile
#     assert contact_from_view_page.fax == contact_from_edit_page.fax


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                [contact.telephone_home, contact.telephone_work, contact.telephone_mobile, contact.fax])))) #from edit page
