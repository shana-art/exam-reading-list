from playwright.sync_api import sync_playwright

BASE_URL = "https://tap-vt25-testverktyg.github.io/exam--reading-list/"

def before_all(context):
    context.pw = sync_playwright().start()
    context.browser = context.pw.chromium.launch(headless=True)

def before_scenario(context, scenario):
    context.ctx = context.browser.new_context()
    context.page = context.ctx.new_page()

    # Snabb feedback i UI-actions:
    context.page.set_default_timeout(5000)

    # Men navigation behöver ofta längre tid:
    context.page.set_default_navigation_timeout(30000)

def after_scenario(context, scenario):
    context.ctx.close()

def after_all(context):
    context.browser.close()
    context.pw.stop()
