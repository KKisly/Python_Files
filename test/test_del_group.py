from model.group import Group

def test_delete_first_group(app):
    #test method
    #wd = self.wd
    #app.open_home_page()
    #app.session.login(username = "admin", password = "secret")
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_first_group()
    #app.session.logout()