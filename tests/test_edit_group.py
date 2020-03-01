# -*- coding: utf-8 -*-
from models.group import Group


def test_edit_first_group(app):
    app.group.edit_first(Group(name_group="autotest", header="autotest", footer="autotest"))

def test_edit_group_name(app):
    app.group.edit_first(Group(name_group="New name"))

def test_edit_group_header(app):
    app.group.edit_first(Group(header="New header"))

def test_edit_group_footer(app):
    app.group.edit_first(Group(footer="New footer"))