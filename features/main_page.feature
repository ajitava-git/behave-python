Feature: behave with selenium

  Scenario: Launch selenium tutorial main page
    Given we have navigated to the url
    When we check the title
    Then we verify the title of the page

  Scenario: Fill the text in the main page
    Given we enter name in the name field
    When we enter email in the email field
    Then we enter phone number in the phone number field
    Then we verify the title of the page

  Scenario: Click drop down in the main page
    Given we have navigated to the url
    When we click the drop down
    When we select male from drop down
    Then we verify the title of the page

  Scenario: Enable checkbox in the main page
    Given we have navigated to the url
    When we check the checkbox
    Then we verify the title of the page

  Scenario: Click Click me button
    Given we have navigated to the url
    When we click the click me button
    Then we verify the title of the page