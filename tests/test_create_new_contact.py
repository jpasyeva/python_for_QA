
from models.contact import Contact


def test_create_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Firstname", lastname="Lastname", address="Address", home_phone="home phone",
                      mobile_phone="mobile phone", work_phone="work phone", email="email", address2="address2",
                      phone2="phone2")
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
