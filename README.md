# origin-qa-take-home

## Description
This repository contains code for automating test cases for the
Saving Goals functionality of Origin´s website, using **Python**, **Selenium** and **Pytest**.

[Test Case Management Sheet](https://docs.google.com/spreadsheets/d/1KdRh4h6YiLICuqD93Uqb68zFZDJFnNxLLtWxHhwL3TE/edit?usp=sharing)

## Installation

- Clone the repository from Github
- Install Python 3.x
- Install the required packages using the following command:

`pip install -r requirements.txt`

## Usage

- Navigate to the cloned directory using command prompt
- Run the following command to execute all tests:

`pytest saving_goals_test.py`

- If you want to execute specific tests, use the following command:

`pytest saving_goals_test.py::test_tc_0001`

The above command will execute the test_tc_0001 test function. 
Replace the function name to execute any specific test.

If you want to skip a test, use the following command:

`pytest saving_goals_test.py -m "not tc_0007"`

The above command will skip the test_tc_0007 test function. 
Replace the function name to skip any specific test.

## Contributing

- Fork the repository.
- Make your changes and create a pull request.

## How to generate HTML report from your pytest run

- Install pytest-html using pip:

`pip install pytest-html`

- Run pytest with the --html option and specify the path and filename for the HTML report. For example:

`pytest --html=report.html`

This will run your tests and generate an HTML report called report.html in the current directory.

- Open the HTML report in a web browser to view the test results.
