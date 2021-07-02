@chrome
Feature:
    Office challenge
    Scenario: Going through the office challenge
        When user successfully created
        Then start the office challenge
        Then answer office challenge question
        Then go to leaderboard page
        Then check your score


