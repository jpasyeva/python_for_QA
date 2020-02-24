# -*- coding: utf-8 -*-
from models.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name_group="autotest", header="autotest", footer="autotest"))
    app.session.logout()