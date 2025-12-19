from playwright.sync_api import expect
from .base_page import BasePage

class FavoritesPage(BasePage):
    BOOK_KEY = {
        "Hur man tappar bort sin TV": "Hur man tappar bort sin TV-fjärr 10 gånger om dagen",
    }

    def fav_testid(self, title_part: str) -> str:
        key = self.BOOK_KEY[title_part]
        return f"fav-{key}"

    # ✅ Gamla namnet (behave verkar hitta detta)
    def assert_book_visible(self, title_part: str, expected: bool):
        loc = self.by_testid(self.fav_testid(title_part))
        if expected:
            expect(loc).to_be_visible()
        else:
            expect(loc).to_have_count(0)

    # ✅ Nya namnet (dina steps anropar detta)
    def expect_book_visible(self, title_part: str, expected: bool):
        self.assert_book_visible(title_part, expected)
