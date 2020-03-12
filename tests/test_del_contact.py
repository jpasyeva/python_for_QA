# -*- coding: utf-8 -*-
from models.contact import Contact
from random import randrange


def test_delete_some_contact(app):
    if app.contact.count_edit() == 0:
        app.contact.add_new(Contact(firstname=u"First contact"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count_edit()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_delete_all_contacts(app):
    if app.contact.count_edit() == 0:
        app.contact.add_new(Contact(firstname=u"First contact"))
    app.contact.delete_all_contacts()
    new_contacts = app.contact.get_contact_list()
    assert len(new_contacts) == 0
