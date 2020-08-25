*** Settings ***
Documentation   Test case for verifying invalid cases for GET endpoint

Suite Setup     Build Database And Create Users      3
Suite Teardown  Delete Database

Library           ../python_libraries/web_requests.py
Resource          ../robot_libraries/common_lib.robot


*** Variables ***
${USERS_GET_ENDPOINT}   http://127.0.0.1:8000/users

${USERS_GET_ENDPOINT_INVALID}   http://127.0.0.1:8000/user

${USERS_DATA}  [[1,"Test","User0","test.user0@email.testing"],[2,"Test","User1","test.user1@email.testing"],[3,"Test","User2","test.user2@email.testing"]]

${USERS_INVALID_DATA}   [[1,"Test","User3","test.user0@email.testing"],[2,"Test","User2","test.user1@email.testing"],[3,"Test","User1","test.user2@email.testing"]]


*** Test Cases ***
Invalid Endpoint Address
    ${ANSWER} =         Get Request     ${USERS_GET_ENDPOINT_INVALID}
    Should Be Equal As Strings          404                     ${ANSWER}[0]    


Invalid Users Data
    [Documentation]     This is pretty much useless case because we already test valid data from users
    ...                 but it is here more like a showcase
    ${ANSWER} =         Get Request     ${USERS_GET_ENDPOINT}
    Should Be Equal As Strings          200                     ${ANSWER}[0]
    Should Not Be Equal As Strings      ${USERS_INVALID_DATA}   ${ANSWER}[2]

