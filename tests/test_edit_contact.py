# -*- coding: utf-8 -*-
from models.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count_edit() == 0:
        app.contact.add_new(Contact(firstname=u"First contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname=u"autotest", middlename=u"autotest", lastname=u"autotest",
                                           nickname=u"autotest", title=u"autotest", company=u"autotest",
                                           address=u"autotest", home_phone=u"autotest", mobile_phone=u"autotest",
                                           work_phone=u"autotest", fax=u"autotest", email=u"autotest",
                                           homepage=u"autotest", address2=u"autotest", phone2=u"autotest",
                                           notes=u"autotest"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_lastname(app):
    if app.contact.count_edit() == 0:
        app.contact.add_new(Contact(firstname=u"First contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(lastname=u"New lastname"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
