*** Settings ***

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Test Setup  Open test browser
Test Teardown  Close all browsers

*** Test Cases ***

Create content and check history is working
    Given I'm logged in as the site owner 


*** Keywords ***

I'm logged in as the site owner
    Log in as site owner
    Go to homepage
