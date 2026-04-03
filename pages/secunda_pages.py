import re

from playwright.sync_api import Page, expect


class SecundaPage:
    URL = 'https://secunda.com.ua/'
    def __init__(self, page: Page):
        self.page = page

        # -----------------Menu-------------------------------
        self.menu = page.locator("menu.catalog-list")
        # -----------------Menu-------------------------------

        #-----------------Burger menu-------------------------------
        self.burger = page.locator(".header-menu .header-menu__icon")
        self.burger_menu = page.locator("menu.catalog-list.catalog-mobile")
        #-----------------Burger menu-------------------------------

        #-----------------The men's sport watches------------------
        # self.burger_menu = page.locator(".header-menu").get_by_role("link")
        self.man_watches = page.locator(".catalog-list").get_by_role("link", name="Чоловічі годинники")
        self.sport_watches = page.locator(".multi-menu").get_by_role("link", name="Спорт")
        #-----------------The men's sport watches------------------

        #-----------------The women's sport watches------------------
        self.woman_watches = page.locator(".catalog-list").get_by_role("link", name="Жіночі годинники")
        self.classic_watches = page.locator(".multi-menu").get_by_role("link", name="Класика")
        #-----------------The women's sport watches------------------



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
        self.man_watches.click()
        expect(self.sport_watches).to_be_visible()
        self.sport_watches.click()
    #-----------------The men's sport watches------------------

    #-----------------The women's sport watches----------------
    def get_women_classic_watches(self):
        self.woman_watches.click()
        expect(self.classic_watches).to_be_visible()
        self.classic_watches.click()
    #-----------------The women's sport watches----------------
