# -*- coding: utf-8 -*-

class GrouptHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # создание новой группы
        wd.find_element_by_name("new").click()
        # заполнение формы
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name_group)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # нажатие кнопки создать
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        #выбрать первый элемент
        wd.find_element_by_name("selected[]").click()
        #нажать кнопку удаления
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def edit_first(self, group):
        wd = self.app.wd
        self.open_group_page()
        # выбрать первый элемент
        wd.find_element_by_name("selected[]").click()
        # нажать кнопку edit
        wd.find_element_by_name("edit").click()
        # изменить форму группы
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name_group)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        #нажать кнопку update
        wd.find_element_by_name("update").click()
        self.return_to_group_page()


    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
