*** Settings ***
Library      ../python_libraries/common.py
Library      ../../create_env.py


*** Variables ***
${CREATE_ENV_COMMAND}           python3
${CREATE_ENV_SCRIPT_FILE}       create_env.py

${DELETE_ENV_COMMAND}           python3
${DELETE_ENV_SCRIPT_FILE}       clear_env.py


*** Keywords ***
Build Database And Create Users
    [Arguments]    ${amount_of_users}
    Build Database
    Create Multiple Users       ${amount_of_users}


Build Database
    Run Shell Script    ${CREATE_ENV_COMMAND}   ${CREATE_ENV_SCRIPT_FILE}


Create Multiple Users
    [Arguments]         ${amount}
    Create Users To Database    ${amount}


Delete Database
    Run Shell Script    ${DELETE_ENV_COMMAND}   ${DELETE_ENV_SCRIPT_FILE}
