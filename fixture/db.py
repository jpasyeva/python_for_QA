import pymysql
from models.group import Group
from models.contact import Contact


class DbFixture:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=database, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id_group, name_group, header, footer) = row
                list.append(Group(id_group=str(id_group), name_group=name_group, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00'")
            for row in cursor:
                (id_contact, firstname, lastname) = row
                list.append(Contact(id_contact=str(id_contact), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_contact_tel_list(self):
        list_tel = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, home, mobile, work, phone2 from addressbook where deprecated='0000-00-00 00:00'")
            for row in cursor:
                (id, firstname, lastname, home, mobile, work, phone2) = row
                list_tel.append(
                    Contact(id_contact=str(id), firstname=firstname, lastname=lastname, home_phone=home, mobile_phone=mobile,
                             work_phone=work, phone2=phone2))
        finally:
            cursor.close()
        return list_tel

    def get_contact_mail_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00'")
            for row in cursor:
                (id, firstname, lastname, email, email2, email3) = row
                list.append(Contact(id_contact=str(id), firstname=firstname, lastname=lastname, email=email, email2=email2,
                                     email3=email3))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
