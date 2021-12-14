# Created by ntere at 12/2/2021
Feature: Cancel order tests


  Scenario: User able to see Cancel items or orders
    Given Open the amazon help link
    When type in cancel order on the search bar

    Then Verify result have "Cancel Items or Orders"
