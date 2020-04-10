# from models.group import Group
# from models.contact import Contact
# from fixture.orm import ORMFixture
# import random
#
# db = ORMFixture(host="127.0.0.1", database="addressbook", user="root", password="")


from models.contact import Contact
from models.group import Group
import random

def test_add_contact_to_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="firstname", lastname="lastname"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name_group="name", header="header", footer="footer"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_contacts_not_in_group(group)) == 0:
        app.contact.create(Contact(firstname="New"))
    contact = random.choice(orm.get_contacts_not_in_group(group))
    app.contact.add_to_group(contact.id, group.id)
    assert contact in orm.get_contacts_in_group(group)



def test_delete_contact_from_group(app, orm):
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="firstname", lastname="lastname"))
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name_group="name", header="header", footer="footer"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_contacts_in_group(group)) == 0:
        contact = random.choice(orm.get_contact_list())
        app.contact.add_to_group(contact.id, group.id)
    else:
        contact = random.choice(orm.get_contacts_in_group(group))
    app.contact.delete_from_group(contact.id, group.id)
    assert contact in orm.get_contacts_not_in_group(group)


# def test_add_user_to_group(app):
#     if app.contact.get_contact_list() == 0:
#         app.contact.add_new(Contact(firstname="Test", lastname="TEST"))
#     if app.group.get_group_list() == 0:
#         app.group.create(Group(name_group="First group"))
#     contacts_not_in_groups = db.get_contacts_not_in_group()
#     contact = random.choice(contacts_not_in_groups)
#     groups = db.get_group_list()
#     group_id = random.choice(groups).id
#     app.contact.add_contact_to_group_by_name(contact.id, group_id)
#     new_users = db.get_contacts_in_group(Group(id_group=group_id))
#     assert contact in new_users
#
#
# # db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
#
#
# def test_add_contact_in_group(app,db):
#     old_db_contact = db.get_contact_list()
#     old_db_group = db.get_group_list()
#     contact = Contact(firstname="Nikolay", lastname="Elagin")
#     group = Group(name_group="New group")
#     if old_db_group:
#         new_db_group = db.get_group_list()
#         random_group = random.choice(new_db_group)
#         group_id = random_group.id
#         if old_db_contact:
#             contacts_not_in_groups = db.get_contacts_not_in_group(random_group)
#             random_contact = random.choice(contacts_not_in_groups)
#             contact_id = random_contact.contact_id
#             app.contact.add_contact_to_group_by_name(contact_id, group_id)
#             app.contact.sort_by_group_by_id(group_id)
#             web_info = [app.contact.get_contact_info_by_id(contact_id)]
#             db_info = db.get_contacts_in_group(Group(id_group=str(group_id)))
#             assert web_info == db_info
#         else:
#             app.contact.create(contact)
#             new_db_contact = db.get_contact_list()
#             contact_id = new_db_contact[0].contact_id
#             app.contact.add_contact_to_group_by_name(contact_id, group_id)
#             app.contact.sort_by_group_by_id(group_id)
#             web_info = [app.contact.get_contact_info_by_id(contact_id)]
#             db_info = db.get_contacts_in_group(Group(id_group=str(group_id)))
#             assert web_info == db_info
#             app.contact.delete_first_contact()
#     else:
#         app.group.create(group)
#         new_db_group = db.get_group_list()
#         group_id = new_db_group[0].group_id
#         if old_db_contact:
#             random_contact = random.choice(old_db_contact)
#             contact_id = random_contact.contact_id
#             app.contact.add_contact_to_group_by_name(contact_id, group_id)
#             app.contact.sort_by_group_by_id(group_id)
#             web_info = [app.contact.get_contact_info_by_id(contact_id)]
#             db_info = db.get_contacts_in_group(Group(id_group=str(group_id)))
#             assert web_info == db_info
#         else:
#             app.contact.create(contact)
#             new_db_contact = db.get_contact_list()
#             contact_id = new_db_contact[0].contact_id
#             app.contact.add_contact_to_group_by_name(contact_id, group_id)
#             app.contact.sort_by_group_by_id(group_id)
#             web_info = [app.contact.get_contact_info_by_id(contact_id)]
#             db_info = db.get_contacts_in_group(Group(id_group=str(group_id)))
#             assert web_info == db_info
#             app.contact.delete_first_contact()
#             app.group.delete_first_group()