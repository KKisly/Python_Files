from model.group import Group

def test_test_modify_group_name(app):
    #app.session.login(username = "admin", password = "secret")
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="New Name"))
    #app.group.retrun_to_groups_page()
    #app.session.logout()


def test_test_modify_group_header(app):
    #app.session.login(username="admin", password="secret")
    app.group.open_groups_page()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(header="New Header"))
    #app.group.retrun_to_groups_page()
    #app.session.logout()