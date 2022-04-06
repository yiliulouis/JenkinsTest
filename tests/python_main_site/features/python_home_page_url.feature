
Feature: Verifying the home page url goes to the right place

    Feature Description
    Scenario: The Python home page should have correct title

        Given I go to the site "python.org"
        When the page is loaded
        Then the page title should be "Welcome to Python.org"

    Scenario: The python home page should have correct url

        Given I go to the site "python.org"
        Then current url should be "www.python.org"