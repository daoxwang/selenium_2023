import os

from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    # без отрисовки браузера
    parser.addoption("--headless", action="store_true", default=False)


@pytest.fixture()
def browser(request):
    _browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = None

    if _browser == "chrome":
        options = ChromeOptions()
        options.headless = headless
        driver = webdriver.Chrome(options=options)

    elif _browser == "edge":
        options = EdgeOptions()
        options.headless = headless
        driver = webdriver.Edge(options=options)

    driver.maximize_window()
    yield driver
    driver.close()
