@chrome
Feature:
    Bus challenge
    Scenario: Going through the bus challenge
        When user successfully created
        Then start the bus challenge
        Then answer bus challenge question
        Then go to leaderboard page
        Then check your score


