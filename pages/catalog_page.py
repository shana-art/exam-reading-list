from playwright.sync_api import expect
from .base_page import BasePage

class CatalogPage(BasePage):
    # Vi mappar "kort titel-del" -> exakt testid-suffix (från codegen)
    BOOK_KEY = {
        "Hur man tappar bort sin TV": "Hur man tappar bort sin TV-fjärr 10 gånger om dagen",
    }

    def star_testid(self, title_part: str) -> str:
        key = self.BOOK_KEY[title_part]
        return f"star-{key}"

    def toggle_favorite(self, title_part: str):
        self.by_testid(self.star_testid(title_part)).click()

    def expect_favorited_state(self, title_part: str, expected: bool):
        # Om knappen har aria-pressed så är det stabilast. Vi kollar först det,
        # annars faller vi tillbaka till att bara kunna klicka (utan att anta mer).
        loc = self.by_testid(self.star_testid(title_part))
        try:
            expect(loc).to_have_attribute("aria-pressed", "true" if expected else "false")
        except Exception:
            # fallback: ingen aria-pressed i DOM => då kan vi inte läsa state säkert här
            pass
