import re

from playwright.async_api import Page

class SecundaPage(Page):
    URL = 'https://secunda.com.ua/'
    def __init__(self, page: Page):
        self.page = page


        #-----------------Burger menu-------------------------------
        self.menu = page.locator("menu.catalog-list")
        self.burger = page.locator(".header-menu .header-menu__icon")
        self.burger_menu = page.locator("menu.catalog-list.catalog-mobile")
        #-----------------Burger menu-------------------------------

        #-----------------The men's sport watches------------------
        # self.burger_menu = page.locator(".header-menu").get_by_role("link")
        self.man_watches = page.locator(".catalog-list").get_by_role("link", name="Чоловічі годинники")
        self.sport_watches = page.locator(".multi-menu").get_by_role("link", name="Спорт")
        #-----------------The men's sport watches------------------


    def open(self):
        self.page.goto(self.URL)


    #-----------------Menu-------------------------------
    def get_menu(self):
        return self.menu
    #-----------------Menu-------------------------------

    #-----------------Burger menu-------------------------------
    def get_burger_menu(self):
        return self.burger
    def click_burger_menu(self):
        self.burger.click()
    def get_burger_menu_items(self):
        return self.burger_menu
    #-----------------Burger menu-------------------------------

    # -----------------The men's sport watches------------------
    def get_mens_sport_watches(self):
        # self.burger_menu.click()
        self.man_watches.click()
        self.sport_watches.click()
    #-----------------The men's sport watches------------------
