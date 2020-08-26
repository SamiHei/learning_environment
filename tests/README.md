# Test Automation

## Usage

From the root folder run

```
./start_web_env.sh
```

to start the uvicorn server running the endpoints.

From the project root you can run tests

```
robot -d tests/results tests/web_tests/valid_get_users.robot
```

Where:
* -d tells the robot framework result files target folder
* tests/... tells the file to be ran

