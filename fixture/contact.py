# -*- coding: utf-8 -*-
from models.contact import Contact


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
                text = element.text
                element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=text, id_contact=id))
        return list(self.contact_cache)
