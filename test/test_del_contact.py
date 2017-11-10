from model.contact import Contact

def test_delete_first_contact(app):
    #test method
    #wd = self.wd
    #app.open_home_page()
    #app.session.login(username = "admin", password = "secret")
    if app.contact.count() == 0:
        app.contact.add_new_contact(Contact(name="test", middle_name="test", last_name="test", nickname="test", title="test", company="test", address="test", telephone_home="test", telephone_mobile="test",
             telephone_work="test", fax_work="test", email_1="test", email_2="test", email_3="test", homepage="test", birthday_option_1=4, birthday_option_2=2,
             birthday_year="2010", anniversary_option_1=3, anniversary_option_2=3, anniversary_year="2010", secondary_address="test", home="test", notes="test"))
    app.contact.delete_first_contact()
    #app.session.logout()