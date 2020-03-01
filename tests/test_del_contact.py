# -*- coding: utf-8 -*-
from models.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count_select_checkbox() == 0:
        app.contact.add_new(Contact(firstname=u"First contact"))
    app.contact.delete_first_contact()


def test_delete_all_contacts(app):
    if app.contact.count_select_checkbox() == 0:
        app.contact.add_new(Contact(firstname=u"First contact"))
    app.contact.delete_all_contacts()