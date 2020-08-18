#! /bin/bash

# --------------------------------------------------------
# Author: SamiHei
# 
# Script to remove environment (database, ...)
#
# TODO: Maybe do "reset" script here? (Run remove and create_env.py)
# --------------------------------------------------------

DB=~/git/learning_environment/database.db

if [ -f "$DB" ]; then
    rm "$DB"
    echo "Database removed!"
else
    echo "Nothing to remove!"
fi
