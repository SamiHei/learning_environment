*** Settings ***
Documentation   Test case for verifying GET endpoint for users

Suite Setup     Build Database          # Here some setup (build database, create users and start service?)
Suite Teardown  Delete Database         # Here some teardown (Delete database?)

# Library         # Propably some request lib or own custom?
Library           BuiltIn
Resource          ../robot_libraries/common_lib.robot

*** Variables ***
${TEST}        Testing

*** Test Cases ***
Get And Verify All Users
    Log To Console      ${TEST}