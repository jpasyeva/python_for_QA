# -*- coding: utf-8 -*-
from models.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count_edit() == 0:
        app.contact.add_new(Contact(firstname=u"First contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)


def test_delete_all_contacts(app):
    if app.contact.count_edit() == 0:
        app.contact.add_new(Contact(firstname=u"First contact"))
    app.contact.delete_all_contacts()
    new_contacts = app.contact.get_contact_list()
    assert len(new_contacts) == 0
