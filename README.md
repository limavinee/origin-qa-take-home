# origin-qa-take-home

# Description
This repository contains code for automating saving goals functionality of a website using Selenium and Pytest.

# Installation
Clone the repository from Github
Install Python 3.x
Install the required packages using the following command:
Copy code
pip install -r requirements.txt

# Usage
Navigate to the cloned directory using command prompt
Run the following command to execute all tests:
Copy code
pytest -v -s test_saving_goals.py
If you want to execute specific tests, use the following command:
arduino
Copy code
pytest -v -s test_saving_goals.py::test_tc_0001
The above command will execute the test_tc_0001 test function. Replace the function name to execute any specific test.
If you want to skip a test, use the following command:
arduino
Copy code
pytest -v -s test_saving_goals.py -m "not tc_0007"
The above command will skip the test_tc_0007 test function. Replace the function name to skip any specific test.

# Contributing
Fork the repository.
Make your changes and create a pull request.

# License
This project is licensed under the MIT License - see the LICENSE.md file for details.