# -*- coding: utf-8 -*-
from models.contact import Contact
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def fill_form_contact(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_phone)
        self.change_field_value("mobile", contact.mobile_phone)
        self.change_field_value("work", contact.work_phone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def add_new(self, contact):
        wd = self.app.wd
        # создание нового контакта
        wd.find_element_by_link_text("add new").click()
        # вызов функции заполнения формы контакта
        self.fill_form_contact(contact)
        # нажатие кнопки submit
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        # нажать кнопку удалить
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # закрытие диалогового окна, в котором пользователь подтверждает удаление контакта
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.contact_cache = None

    def delete_all_contacts(self):
        wd = self.app.wd
        # выбрать все элементы
        wd.find_element_by_id("MassCB").click()
        # нажать кнопку удалить
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # закрытие диалогового окна, в котором пользователь подтверждает удаление контакта
        wd.switch_to_alert().accept()
        wd.find_elements_by_css_selector("div.msgbox")
        self.contact_cache = None

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        # нажатие икноки редактирования
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # вызов функции заполнения формы контакта
        self.fill_form_contact(contact)
        # нажатие кнопки update
        wd.find_element_by_name("update").click()
        self.app.return_home_page()
        self.contact_cache = None

    def count_select_checkbox(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def count_edit(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_xpath("//img[@alt='Edit']"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name('td')
                text_lastname = cells[1].text
                text_firstname = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                text_address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(lastname=text_lastname, firstname=text_firstname, id_contact=id,
                                                  address=text_address,
                                                  all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id_contact = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").text
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id_contact=id_contact, address=address,
                       home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, phone2=phone2,
                       email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone, phone2=phone2)
