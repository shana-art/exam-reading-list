from playwright.sync_api import expect
from .base_page import BasePage
from features.environment import BASE_URL

class HomePage(BasePage):
    NAV = {
        "Catalog": "catalog",
        "Favorites": "favorites",
        "AddBook": "add-book",
    }

    def open(self):
        self.goto(BASE_URL)

    def nav_button(self, view: str):
        return self.by_testid(self.NAV[view])

    def go_to(self, view: str):
        btn = self.nav_button(view)
        # Om vi redan är på vyn är knappen disabled → klicka inte
        if btn.is_disabled():
            return
        btn.click()

    def assert_view(self, view: str):
        # På aktiv vy är dess nav-knapp disabled (enligt din logg)
        expect(self.nav_button(view)).to_be_disabled()
