# Created by lenya at 09.11.2020
Feature: Lab4 Behavior Driven Development

  Scenario: Test set intersection operation
    Given I have sets {1, 'C', -2.1, 36, "1-h", -3} and {"6jsQ", -3, 11, "C"}
    When I intersect them with discrete numbers strategy
    Then I expect the result to be {-3}

  Scenario:
    Given I have sets {18, 324.7, "123x", -7, 6.13871245} and {"Hello, unittest world!", "hey", -7.62, 1, 18}
    When I intersect them with discrete numbers strategy
    Then I expect the result to be {18}