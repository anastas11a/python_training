def test_edit_first_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group()
    app.session.logout()