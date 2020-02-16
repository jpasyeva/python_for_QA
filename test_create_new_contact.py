# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

class CreateNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(50)

    def test_create_new_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.add_new_contact(wd)
        self.return_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def add_new_contact(self, wd):
        #создание нового контакта
        wd.find_element_by_link_text("add new").click()
        #заполнение формы контакта
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(u"Фамилия")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(u"Отчество")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(u"Имя")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(u"Никнейм")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(u"Заголовок")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(u"Компания")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(u"Адрес")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(u"Домашний телефон")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(u"Мобильный телефон")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(u"Рабочий телефон")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(u"Факс")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(u"электронная почта")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(u"сайт")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("14")
        wd.find_element_by_xpath("//option[@value='14']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("October")
        wd.find_element_by_xpath("//option[@value='October']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1990")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("14")
        wd.find_element_by_xpath("(//option[@value='14'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("November")
        wd.find_element_by_xpath("(//option[@value='November'])[2]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2020")
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(u"адрес2")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(u"дом")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(u"заметка")
        #нажатие кнопки submit
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
