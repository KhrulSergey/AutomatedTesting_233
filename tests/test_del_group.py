__author__ = 'Sergey Khrul'


def test_del_first_group(app):
    app.session.login(user_name="admin", password="secret")
    app.group_page.delete_first()
    app.session.logout()
