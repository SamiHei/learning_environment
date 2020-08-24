# --------------------------------------------------------
# Author: SamiHei
# 
# Common Python test automation libraries to be used
# with Robot Framework
#
# Contains:
#     - Run shell scripts
# --------------------------------------------------------

import subprocess
import os
import re

from config import DB_NAME
from data_structures.user import User
from services.users import Users


# REGEX for project root directory
REGEX = '.*/git/[^/]+'

'''
Runs the given command and script file

Arguments:
    - command = Command line command (example. 'ls' or 'python3'
    - script_path = Path to the script from the project root folder (if the script is in the root folder just script file name
'''
def run_shell_script(command, script_path):
    wd = os.getcwd()
    root = re.match(REGEX, wd)
    os.chdir(root.group(0))
    subprocess.run([command, script_path], check=True)


def create_users_to_database(amount):
    users = Users(DB_NAME)
    for x in range(int(amount)):
        print("Round {}".format(x))
        l_name = "User{}".format(x)
        email = "test.user{}@email.lol".format(x)
        new_user = User(first_name="Test", last_name=l_name, email=email)
        users.create_user(new_user)

