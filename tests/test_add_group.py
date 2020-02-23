# -*- coding: utf-8 -*-
from models.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name_group="New", header="New group", footer="comment"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name_group="", header="", footer=""))
    app.session.logout()