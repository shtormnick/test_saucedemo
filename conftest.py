import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help="Choose browser: Chrome or Firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ua or us")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    user_language = request.config.getoption("--language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option(
            'prefs', {'intl.accept_languages': user_language})
        print("\n\nStart chrome browser for test...")
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\n\nStart firefox browser for test...")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nQuit browser...")
    browser.quit()

@pytest.fixture(scope="function")
def setup(browser):
    link = "https://www.saucedemo.com/"
    name = "standard_user"
    password = "secret_sauce"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.register_new_user(name, password)
