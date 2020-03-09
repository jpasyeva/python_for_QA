# -*- coding: utf-8 -*-
from models.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name_group="New", header="New group", footer="comment"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name_group="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
