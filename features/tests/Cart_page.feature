# Created by ntere at 12/11/2021
Feature: Amazon page search

  Scenario: User can add a product to the cart
    Given Open Amazon page
    When Search for shoes
    And click search icon
    And click first product
    And click on add to card button
    Then verify cart has 1 item(s)