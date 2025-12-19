from behave import given, when, then
from pages.home_page import HomePage
from pages.catalog_page import CatalogPage
from pages.favorites_page import FavoritesPage

@given("I open the app")
def step_open(context):
    context.home = HomePage(context.page)
    context.catalog = CatalogPage(context.page)
    context.favorites = FavoritesPage(context.page)
    context.home.open()

@given('I am on the "{view}" view')
def step_on_view(context, view):
    context.home.go_to(view)
    context.home.assert_view(view)

@when('I go to "{view}"')
def step_go(context, view):
    context.home.go_to(view)

@then('I should be on "{view}"')
def step_assert(context, view):
    context.home.assert_view(view)

@given('book "{title_part}" is not in favorites')
def step_ensure_not_in_favs(context, title_part):
    # Gå till Favorites och om den finns: toggla bort från Catalog
    context.home.go_to("Favorites")
    context.home.assert_view("Favorites")

    try:
        # Om den är synlig, ta bort den genom att gå till Catalog och klicka stjärnan
        if context.page.get_by_test_id(context.favorites.fav_testid(title_part)).count() > 0:
            context.home.go_to("Catalog")
            context.home.assert_view("Catalog")
            context.catalog.toggle_favorite(title_part)
            context.home.go_to("Favorites")
            context.home.assert_view("Favorites")
    except Exception:
        pass

@when('I toggle favorite for "{title_part}" "{clicks}" times')
def step_toggle(context, title_part, clicks):
    context.home.go_to("Catalog")
    context.home.assert_view("Catalog")
    for _ in range(int(clicks)):
        context.catalog.toggle_favorite(title_part)

@then('"{title_part}" should be visible in favorites: "{expected}"')
def step_check_in_favs(context, title_part, expected):
    expected_bool = expected.lower() == "true"
    context.home.go_to("Favorites")
    context.home.assert_view("Favorites")
    context.favorites.expect_book_visible(title_part, expected_bool)
