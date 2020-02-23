# -*- coding: utf-8 -*-
import pytest
from models.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_create_new_contact(app):
    app.session.login("admin", "secret")
    app.contact.add_new(Contact(firstname=u"Фамилия", middlename=u"Отчество", lastname=u"Имя", nickname=u"Никнейм", title =u"Заголовок", company=u"Компания", address=u"Адрес",
                                home_phone=u"Домашний телефон", mobile_phone=u"Мобильный телефон", work_phone=u"Рабочий телефон", fax=u"Факс",
                                email=u"электронная почта", homepage=u"сайт", address2=u"адрес2", phone2=u"дом", notes=u"заметка"))
    app.session.logout()