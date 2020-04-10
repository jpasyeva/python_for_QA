import re


def test_phones_on_homepage(app, db):
    contacts_from_homepage = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list_from_db()
    for contact_from_homepage in contacts_from_homepage:
        id_contact = contact_from_homepage.id_contact
        for contact_from_db in contacts_from_db:
            id_contact2 = contact_from_db.id_contact
            if id_contact == id_contact2:
                assert contact_from_homepage.lastname == contact_from_db.lastname
                assert contact_from_homepage.firstname == contact_from_db.firstname
                assert contact_from_homepage.address == contact_from_db.address
                assert contact_from_homepage.all_emails_from_home_page == merge_email_like_on_homepage(contact_from_db)
                assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)



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

