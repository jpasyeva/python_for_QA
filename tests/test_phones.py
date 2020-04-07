# -*- coding: utf-8 -*-
from models.contact import Contact
from random import randrange
import re


def test_contact_on_home_page(app):
    contact = app.contact.get_contact_list()
    index = randrange(len(contact))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_contact_like_db_and_home(app, db):
    contacts_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contacts_on_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contacts_on_home_page)):
        contact_from_home_page = contacts_on_home_page[i]
        contact_from_db = contacts_db[i]
        assert contact_from_home_page.id_contact == contact_from_db.id_contact
        assert contact_from_home_page.firstname == contact_from_db.firstname
        assert contact_from_home_page.lastname == contact_from_db.lastname



def test_phones_on_contact_view_page(app):
    contact = app.contact.get_contact_list()
    index = randrange(len(contact))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.home_phone, contact.mobile_phone,
                                                            contact.work_phone, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                      [contact.email, contact.email2, contact.email3])))
