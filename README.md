# Test Project
This project created as test task

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pytest, selenium, WebDriverManager, 

```bash
pip install pytest
pip install selenium
pip install WebDriverManager
```

### Commands 
you can run autotests by next commands 
and next atributs 
–maxfail=n stops execution after nth failure. n can be any number such as 1.2.3
-rA this gives output of all tests
f- failed
E- error
s- skipped
x- xfailed
X- xpassed
p- passed
P-passed with output
a- all except pP
A- all
-m only the tests defined by the marker will run after this command.
```
pytest .\test_filter.py
