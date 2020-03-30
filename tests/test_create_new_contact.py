# -*- coding: utf-8 -*-
from models.contact import Contact


def test_create_new_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.add_new(contact)
    assert len(old_contacts) + 1 == app.contact.count_edit()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max)
