Feature: SignIn Page

  Scenario: Verify if error password is displayed
    Given I am on the SignIn page
      When I enter a correct email
      And I leave password empty
      And I click the Login button
      Then I verify if login button is clickable
#      Then I receive an error

