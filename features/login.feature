Feature: User authentication

    Background: common step
        Given user is on the login page

    Scenario Outline: Login Test2
        When user enters username "<username>" and password "<password>" and click login
        Then verify the login process
        And close the browser
        
        Examples:
            | username | password |
            | standard_user | secret_sauce |
            | problem_user | secret_sauce |
            | performance_glitch_user | secret_sauce |
            | error_user | secret_sauce |
            | visual_user | secret_sauce |


