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
    page.goto("https://www.google.com/")
    page.screenshot(path="screenshots/example.png")
    page.close()



""""
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
    page.goto("https://www.google.com/")

    page.screenshot(path="screenshots/example.png")



from playwright.sync_api import sync_playwright
    page.wait_for_timeout(3000)
def test_capture_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        

        page.goto('https://github.com/')
        page.screenshot(path='screenshot.png')
        browser.close()
        
        """












"""
thi is 
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com/")
    print(page.title())
    browser.close()


import  re
from playwright.sync_api import Page, expect
def test_has_title(page: Page):
    page.goto("https://www.google.com/")

    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    page.get_by_role("link", name="Get started").click()

    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
    
    """




