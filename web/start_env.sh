#! /bin/bash
# Run the uvicorn server

cd web
~/.local/bin/uvicorn main:app --reload
