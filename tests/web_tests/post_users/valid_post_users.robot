*** Settings ***
Documentation   Test case for verifying valid POST users endpoint

Suite Setup     Build Database
Suite Teardown  Delete Database

Library           ../python_libraries/web_requests.py
Resource          ../robot_libraries/common_lib.robot


*** Variables ***
${USERS_POST_ENDPOINT}   http://127.0.0.1:8000/users


*** Test Cases ***
Create Multiple Users From Endpoint
       Log To Console      Start here
