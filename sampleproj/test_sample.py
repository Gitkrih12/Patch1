
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture


def browser():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


def test_open_browser(browser):
    page = browser.new_page()
    page.goto("https://www.github.com/")
    page.screenshot(path="screenshots/example1.png")
    page.close()