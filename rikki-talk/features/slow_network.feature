Feature: Scroll Down

  Background: Prepare Network
    Given Intercept and replace http data
      | option                   | value              |
      | host                     | localhost          |
      | path                     | /cars/all          |
      | replace_response_code    | 200                |
      | replace_response_content | %{file.cars.json}% |
    Given Delay request for 5 seconds
      | option | value     |
      | host   | localhost |
    Given relaunch

  Scenario: Request cars list
    Given Wait for cars list loaded
    Given Scroll like a monkey
    Then Verify 1 requests for "Cars List"
      | option | value     |
      | host   | localhost |
      | path   | /cars/all |

