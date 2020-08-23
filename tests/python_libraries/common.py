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


# REGEX for project root directory
REGEX = '.*/git/[^/]+'


def run_shell_script(command, script_path):
    wd = os.getcwd()
    root = re.match(REGEX, wd)
    os.chdir(root.group(0))
    subprocess.run([command, script_path], check=True)
