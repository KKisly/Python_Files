from model.contact import Contact
from random import randrange

def test_test_modify_contact_name(app):

    if app.contact.count() == 0:
        app.group.create(Contact(name="test"))

    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="New Name", last_name="New_Polina", address="New Address")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id

    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)