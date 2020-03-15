
from models.contact import Contact


def test_create_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname=u"Фамилия", middlename=u"Отчество", lastname=u"Имя", nickname=u"Никнейм",
                      title=u"Заголовок", company=u"Компания", address=u"Адрес",
                      home_phone=u"Домашний телефон", mobile_phone=u"Мобильный телефон", work_phone=u"Рабочий телефон",
                      fax=u"Факс",
                      email=u"электронная почта", email2="email2", email3="email3",
                      homepage=u"сайт", address2=u"адрес2", phone2=u"дом", notes=u"заметка")
    app.contact.add_new(contact)
    assert len(old_contacts) + 1 == app.contact.count_edit()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



# def test_create_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     app.contact.add_new(Contact())
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
