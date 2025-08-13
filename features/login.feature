Feature: Login functionality

  Scenario: Successful login
    Given I am on the login page
    When I enter valid credentials
    And I click the login button
    Then I should be redirected to the secure area
    And I should see a success message

  Scenario: Login with invalid username
    Given I am on the login page
    When I enter invalid username
    And I click the login button
    Then I should see an username error message

  Scenario: Login with invalid password
    Given I am on the login page
    When I enter invalid password
    And I click the login button
    Then I should see a password error message

  Scenario: Login with empty username
    Given I am on the login page
    When I enter empty username
    And I click the login button
    Then I should see an username error message

  Scenario: Login with empty password
    Given I am on the login page
    When I enter empty password
    And I click the login button
    Then I should see a password error message

  Scenario: Successful logout
    Given I am logged in the secure page
    When I click the logout button
    Then I should be redirected to the login page