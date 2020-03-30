# -*- coding: utf-8 -*-
from models.group import Group
from random import randrange


def test_edit_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name_group="First group"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name_group="New name")
    group.id_group = old_groups[index].id_group
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
