# -*- coding: utf-8 -*-
from models.contact import Contact
from random import randrange


def test_edit_some_contact(app):
    if app.contact.count_edit() == 0:
        app.contact.add_new(Contact(firstname="First contact"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="autotest", lastname="autotest", middlename=u"Отчество", nickname=u"Никнейм",
                      title=u"Заголовок", company=u"Компания", address=u"Адрес",
                      home_phone=u"Домашний телефон", mobile_phone=u"Мобильный телефон", work_phone=u"Рабочий телефон",
                      fax=u"Факс",
                      email=u"электронная почта", email2="email2", email3="email3",
                      homepage=u"сайт", address2=u"адрес2", phone2=u"дом", notes=u"заметка")
    contact.id_contact = old_contacts[index].id_contact
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count_edit()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_edit_contact_lastname(app):
#     if app.contact.count_edit() == 0:
#         app.contact.add_new(Contact(firstname=u"First contact"))
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact = Contact(lastname="New lastname")
#     contact.id = old_contacts[index].id
#     app.contact.edit_contact_by_index(index, contact)
#     assert len(old_contacts) == app.contact.count_edit()
#     new_contacts = app.contact.get_contact_list()

