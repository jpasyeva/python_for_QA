from models.group import Group
from models.contact import Contact
import random


def test_add_user_to_group(app, orm):
    if app.contact.get_contact_list() == 0:
        app.contact.add_new(Contact(firstname="Test", lastname="TEST"))
    if app.group.get_group_list() == 0:
        app.group.create(Group(name_group="First group"))
    all_contacts = orm.get_contact_list()
    contact = random.choice(all_contacts)
    groups = orm.get_group_list()
    group_id = random.choice(groups).id
    app.contact.add_contact_to_group(contact.id, group_id)
    new_users = orm.get_contacts_in_group(Group(id_group=group_id))
    assert contact in new_users
