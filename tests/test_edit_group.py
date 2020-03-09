# -*- coding: utf-8 -*-
from models.group import Group
from random import randrange

# def test_edit_first_group(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name_group="First group"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first(Group(name_group="autotest", header="autotest", footer="autotest"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)


def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name_group="First group"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name_group="New name")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name_group="First group"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first(Group(header="New header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_edit_group_footer(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name_group="First group"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first(Group(footer="New footer"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
