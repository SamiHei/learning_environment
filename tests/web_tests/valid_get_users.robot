*** Settings ***
Documentation   Test case for verifying GET endpoint for users

Suite Setup     Build Database And Create Users      5
Suite Teardown  Delete Database

# Library         # Propably some request lib or own custom?
Library           BuiltIn
Library           ../python_libraries/web_requests.py
Resource          ../robot_libraries/common_lib.robot

*** Variables ***
${TEST}                 Testing
${USERS_GET_ENDPOINT}   http://127.0.0.1:8000/users

*** Test Cases ***
# TODO: Suite setup and teardown done now the actual test!
Get And Verify All Users
    # Log To Console      ${TEST}
    ${ANSWER} =         Get Request     ${USERS_GET_ENDPOINT}
    Log to Console      ${ANSWER}
