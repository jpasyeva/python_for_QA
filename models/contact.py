from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, home_phone=None, mobile_phone=None, work_phone=None, all_phones_from_home_page=None,
                 fax=None, email=None, email2=None, email3=None, all_emails_from_home_page=None,
                 homepage=None, address2=None, phone2=None, notes=None, id_contact=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id_contact = id_contact
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id_contact, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id_contact is None or other.id_contact is None or self.id_contact == other.id_contact) \
               and (self.firstname == other.firstname) and (self.lastname == other.lastname)

    def id_or_max(self):
        if self.id_contact:
            return int(self.id_contact)
        else:
            return maxsize
