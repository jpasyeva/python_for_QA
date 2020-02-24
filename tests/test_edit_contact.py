# -*- coding: utf-8 -*-
from models.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(Contact(firstname=u"", middlename=u"", lastname=u"", nickname=u"", title=u"", company=u"", address=u"", home_phone=u"", mobile_phone=u"", work_phone=u"",
                fax=u"", email=u"", homepage=u"", address2=u"", phone2=u"", notes=u""))
    app.contact.edit_first_contact(Contact(firstname=u"autotest", middlename=u"autotest", lastname=u"autotest", nickname=u"autotest", title =u"autotest", company=u"autotest", address=u"autotest",
                                home_phone=u"autotest", mobile_phone=u"autotest", work_phone=u"autotest", fax=u"autotest",
                                email=u"autotest", homepage=u"autotest", address2=u"autotest", phone2=u"autotest", notes=u"autotest"))
    app.session.logout()