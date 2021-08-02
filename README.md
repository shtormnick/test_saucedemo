# Test Project
This project created as test task

Create Python automation scenarios for checking filtering by price and adding products to the shopping cart on https://www.saucedemo.com/ for standard_user.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pytest, selenium, WebDriverManager, 

```bash
pip install pytest
pip install selenium
pip install WebDriverManager
```

### Commands 
you can run autotests by next commands <br />
and next atributs <br />
–maxfail=n stops execution after nth failure. n can be any number such as 1.2.3 <br />
-rA this gives output of all tests <br />
f- failed <br />
E- error <br /> 
s- skipped <br />
x- xfailed <br />
X- xpassed <br />
p- passed <br />
P-passed with output <br />
a- all except pP <br />
A- all <br />
-m only the tests defined by the marker will run after this command. <br />
```
pytest .\test_filter.py
