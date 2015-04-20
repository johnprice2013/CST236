Feature: Initializing the program

    Scenario: Initialization success
        Given file used for initialization is correct
        When initialize is called
        Then the cities will be read from file

    Scenario: Initialization failed
        Given file used for initialization is incorrect
        When initialize is called 2
        Then program will respond with error