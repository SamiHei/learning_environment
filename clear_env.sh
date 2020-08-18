#! /bin/bash
# Temporal script to clear running environment

DB=~/git/learning_environment/database.db

if [ -f "$DB" ]; then
    rm "$DB"
    echo "Database removed!"
else
    echo "Nothing to remove!"
fi
