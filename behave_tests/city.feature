Feature: Adding a new city

    Scenario: Adding successful
        Given all details given are valid
        When the new city is submitted
        Then the new city will be written to file

    Scenario: Adding Failed
        Given one or more details are invalid
        When the new city is submitted
        Then the new city will not be written to file