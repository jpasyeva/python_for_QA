# -*- coding: utf-8 -*-
from models.contact import Contact


def test_create_new_contact(app):
    app.session.login("admin", "secret")
    app.contact.add_new(Contact(firstname=u"Фамилия", middlename=u"Отчество", lastname=u"Имя", nickname=u"Никнейм", title =u"Заголовок", company=u"Компания", address=u"Адрес",
                                home_phone=u"Домашний телефон", mobile_phone=u"Мобильный телефон", work_phone=u"Рабочий телефон", fax=u"Факс",
                                email=u"электронная почта", homepage=u"сайт", address2=u"адрес2", phone2=u"дом", notes=u"заметка"))
    app.session.logout()

def test_create_empty_contact(app):
    app.session.login("admin", "secret")
    app.contact.add_new(
        Contact(firstname=u"", middlename=u"", lastname=u"", nickname=u"", title=u"",
                company=u"", address=u"", home_phone=u"", mobile_phone=u"", work_phone=u"",
                fax=u"", email=u"", homepage=u"", address2=u"", phone2=u"", notes=u""))
    app.session.logout()