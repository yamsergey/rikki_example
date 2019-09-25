Feature: Scroll Down

  Background: Prepare Network
    Given Intercept and replace http data
      | option                   | value              |
      | host                     | localhost          |
      | path                     | /cars/all          |
      | replace_response_code    | 200                |
      | replace_response_content | %{file.cars.json}% |
    Given relaunch

  Scenario: Request cars list
    Given Wait for cars list loaded
    Given Scroll like a monkey
    Then Verify 1 requests for "Cars List"
      | option | value     |
      | host   | localhost |
      | path   | /cars/all |

  Scenario: No user data in network communication
    Given Wait for cars list loaded
    Then Check no "yamsergey" in any requests/responses because "No email in Network"
