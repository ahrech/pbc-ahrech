# pbc-ahrech
A repository for Python Boot Camp tasks.

Author: Anastasiya Hrechanova.

Package `pbc.sg` contains the following modules:

- `conftest.py` - a module with test fixtures.

- `connections.py` - a module with SSH Client wrapper.

- `sg.py` - a module for work with Selenium grid.

- `test_sel_grid.py` - a module with tests for Selenium grid.

Package `pbc.tools` contains the following modules:

- `fibonacci.py` - a module with a function which prints desired count of fibonacci numbers 

- `numbers.py` - a module with a function which prints pairs of numbers which sum is = 10 for a given collection of numbers

`func_decorators.py` - a module with decorators.

Package `tests.tools` contains the following unit tests:

- `test_fibonacci.py` - a module with unit tests for fibonacci.py

- `test_numbers.py` - a module with unit tests for numbers_pairs.py



To setup virtual environment execute the commands below:

- python -m venv venv

- source venv/bin/activate

- pip install -r requirements.txt