Feature: Läslistan – Navigation och Favoriter
  För att kunna använda sidan
  Som besökare
  Vill jag kunna navigera och hantera favoriter

  Background:
    Given I open the app

  @navigation
  Scenario Outline: Navigate between views
    When I go to "<view>"
    Then I should be on "<view>"

    Examples:
      | view      |
      | Catalog   |
      | Favorites |
      | AddBook   |

  @favorites
  Scenario Outline: Favoritmarkering påverkar Mina böcker
    Given I am on the "Catalog" view
    And book "Hur man tappar bort sin TV" is not in favorites
    When I toggle favorite for "Hur man tappar bort sin TV" "<clicks>" times
    Then "Hur man tappar bort sin TV" should be visible in favorites: "<expected>"

    Examples:
      | clicks | expected |
      | 1      | true     |
      | 2      | false    |
      | 3      | true     |
