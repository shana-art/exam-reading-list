from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        self.page.goto(url)

    def by_testid(self, testid: str):
        return self.page.get_by_test_id(testid)

    def expect_text_visible(self, text: str):
        expect(self.page.get_by_text(text)).to_be_visible()
