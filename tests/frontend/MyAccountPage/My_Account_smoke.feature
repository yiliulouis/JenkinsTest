
@my_account_smoke @smoke
Feature: My Account Smoke Tests
    @TCID10
    Scenario:  valid user should be able to login
        Given I go to the 'my account' Page
        When I type 'testuser_uokqy@ssqa.com' into username of login form
        And I type 'KhtxfjEv' into password of login form
        And I click on the 'login' button
        Then user should be logged in

    @TCID11
    Scenario: User with wrong password should get correct error message
        Given I go to the 'my account' Page
        When I type 'testuser_uokqy@ssqa.com' into username of login form
        And I type '12345' into password of login form
        And I click on the 'login' button
        Then error message with email 'testuser_uokqy@ssqa.com' should be displayed

    @TCID12
    Scenario: User with non-existing email should get correct error message
        Given I go to the 'my account' Page
        When I type 'testus_uokqy@ssqa.com' into username of login form
        And I type 'KhtxfjEv' into password of login form
        And I click on the 'login' button
        Then error message with 'unknown email' should be displayed