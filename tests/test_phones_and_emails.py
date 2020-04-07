import re
from models.contact import Contact


def test_phones_on_homepage(app, db):
    contact_from_homepage = app.contact.get_contact_list()
    contact_from_db = db.get_contact_tel_list()
    for element in contact_from_homepage:
        user = contact_from_db.index(element)
        assert element.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db[user])


def test_mail_on_homepage(app, db):
    contact_from_homepage = app.contact.get_contact_list()
    contact_from_db = db.get_contact_mail_list()
    for element in contact_from_homepage:
        user = contact_from_db.index(element)
        assert element.all_emails_from_home_page == merge_email_like_on_homepage(contact_from_db[user])



def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.home_phone, contact.mobile_phone,
                                                            contact.work_phone, contact.phone2]))))


def merge_email_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                     filter(lambda x: x is not None,
                            [contact.email, contact.email2, contact.email3])))