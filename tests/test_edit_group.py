# -*- coding: utf-8 -*-
from models.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name_group="autotest", header="autotest", footer="autotest"))
    app.session.logout()

def test_edit_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name_group="New name"))
    app.session.logout()

def test_edit_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(header="New header"))
    app.session.logout()

def test_edit_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(footer="New footer"))
    app.session.logout()