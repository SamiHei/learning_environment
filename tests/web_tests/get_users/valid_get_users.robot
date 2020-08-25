*** Settings ***
Documentation   Test case for verifying GET endpoint for users

Suite Setup     Build Database And Create Users      3
Suite Teardown  Delete Database

Library           ../python_libraries/web_requests.py
Resource          ../robot_libraries/common_lib.robot


*** Variables ***
${USERS_GET_ENDPOINT}   http://127.0.0.1:8000/users

${USERS_DATA}      [[1,"Test","User0","test.user0@email.testing"],[2,"Test","User1","test.user1@email.testing"],[3,"Test","User2","test.user2@email.testing"]]


*** Test Cases ***
Get And Verify All Users
    ${ANSWER} =         Get Request     ${USERS_GET_ENDPOINT}
    Should Be Equal As Strings          200                     ${ANSWER}[0]    
    Should Be Equal As Strings          application/json        ${ANSWER}[1]
    Should Be Equal As Strings          ${USERS_DATA}           ${ANSWER}[2]    
