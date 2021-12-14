# Created by ntere at 11/26/2021
Feature: Test case for amazon signin

  # Enter feature description here

  Scenario: Logged out user sees Sign in page when clicking Orders

    Given amazon page
    When click order
    And Verify SignIn page is seen
    Then Validate