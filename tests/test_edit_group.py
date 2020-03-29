# -*- coding: utf-8 -*-
from models.group import Group
import random


def test_edit_group_name(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name_group="First group"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    edit_group = Group(name_group="New name")
    app.group.edit_group_by_id(group.id_group, edit_group)
    new_groups = db.get_group_list()
    pos = old_groups.index(group)
    old_groups[pos] = edit_group
    assert old_groups == new_groups
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

