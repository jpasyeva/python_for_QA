# -*- coding: utf-8 -*-
from models.group import Group


def test_add_group(app):
    app.group.create(Group(name_group="New", header="New group", footer="comment"))

def test_add_empty_group(app):
    app.group.create(Group(name_group="", header="", footer=""))