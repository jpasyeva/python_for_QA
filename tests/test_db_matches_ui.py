from models.group import Group
from models.contact import Contact


def test_group_list_compare_ui_and_db(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name_group="Test", header="Test", footer="Test"))
    ui_group = app.group.get_group_list()

    def clean (group):
        return Group(id_group=group.id_group, name_group=group.name_group.strip())
    db_groups = map(clean, db.get_group_list())
    assert sorted(ui_group, key=Group.id_or_max) == sorted(db_groups, key=Group.id_or_max)


def test_contacts_list_compare_ui_and_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test", lastname="TEST"))
    ui_contact = app.contact.get_contact_list()

    def clean(contact):
        return Contact(id_contact=contact.id_contact, lastname=contact.lastname.strip())
    db_contact = map(clean, db.get_contact_list())
    assert sorted(ui_contact, key=Contact.id_or_max) == sorted(db_contact, key=Contact.id_or_max)
