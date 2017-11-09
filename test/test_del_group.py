
def test_delete_first_group(app):
    #test method
    #wd = self.wd
    #app.open_home_page()
    #app.session.login(username = "admin", password = "secret")
    app.group.delete_first_group()
    #app.session.logout()