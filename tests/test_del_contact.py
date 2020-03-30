# -*- coding: utf-8 -*-
from models.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(firstname=u"First contact"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id_contact)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max)


def test_delete_all_contacts(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(firstname=u"First contact"))
    app.contact.delete_all_contacts()
    new_contacts = db.get_contact_list()
    assert len(new_contacts) == 0
