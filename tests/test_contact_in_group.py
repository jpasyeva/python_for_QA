# -*- coding: utf-8 -*-
from models.contact import Contact
from models.group import Group
import random


def test_add_contact_to_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test", lastname="TEST"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name_group="Test", header="Test", footer="Test"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_contacts_not_in_group(group)) == 0:
        app.contact.create(Contact(firstname="New"))
    contact = random.choice(orm.get_contacts_not_in_group(group))
    app.contact.add_to_group(contact.id_contact, group.id_group)
    assert contact in orm.get_contacts_in_group(group)


def test_delete_contact_from_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="firstname", lastname="lastname"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name_group="name", header="header", footer="footer"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_contacts_in_group(group)) == 0:
        contact = random.choice(orm.get_contact_list())
        app.contact.add_to_group(contact.id_contact, group.id_group)
    else:
        contact = random.choice(orm.get_contacts_in_group(group))
    app.contact.delete_from_group(contact.id_contact, group.id_group)
    assert contact in orm.get_contacts_not_in_group(group)
