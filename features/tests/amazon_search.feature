# Created by ntere at 11/23/2021
Feature: Tests for amazon search


  Scenario: User can search a product on amazon
    Given Open Amazon page
    When Search for table
    And Click search icon
    Then Search result have table