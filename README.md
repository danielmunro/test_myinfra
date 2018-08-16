# test_myinfra
A demo of test_infra, the python infrastructure testing framework. Uses docker-compose, and assumes python and py.test are available.

## Run the Demo
`docker-compose up` from the repository root will start the demo app. Load up `localhost:5000` in a browser to observe the demo running.

## Run the test_infra tests
`cd web` and `py.test test_webinfra.py`:

```
host $ py.test test_webinfra.py
================================================================= test session starts =================================================================
platform darwin -- Python 3.7.0, pytest-3.7.1, py-1.5.4, pluggy-0.7.1
rootdir: /test_myinfra/web, inifile:
plugins: testinfra-1.14.1
collected 3 items

test_webinfra.py ...                                                                                                                            [100%]

============================================================== 3 passed in 36.14 seconds ==============================================================
```