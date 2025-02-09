# Discord: Miru K.

from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()




# Test 1: Ověření načtení hlavní stránky Seznam.cz
def test_homepage_loads(page):
    page.goto("https://www.seznam.cz")
    assert page.title() != "", "Stránka se nenačetla správně."




# Test 2: Ověření funkce vyhledávání
def test_search_functionality(page):
    page.goto("https://www.seznam.cz")

    search_box = page.locator(".search-form__input")
    search_box.wait_for(state="attached", timeout=5000)
    search_box.wait_for(state="visible", timeout=5000)

    search_box.click()

    search_box.fill("Playwright test")

    search_box.press("Enter")

    page.wait_for_load_state("domcontentloaded", timeout=10000)

    # Ověř, že URL obsahuje hledaný výraz
    assert "Playwright+test" in page.url or "Playwright%20test" in page.url, "Vyhledávání nefunguje správně – URL neobsahuje hledaný dotaz."

    # Najdi kontejner s výsledky hledání
    results_locator = page.locator(".search-results") 




# Test 3: Ověření existence odkazu na Seznam Email
def test_seznam_email_link(page: 'page'):
    page.goto("https://www.seznam.cz")
    email_link = page.locator("a[href='https://email.seznam.cz/?hp']")
    email_link.wait_for(state="visible", timeout=5000)
    assert email_link.is_visible(), "Odkaz na Seznam Email není viditelný."




# Test 4: Kontrola, jestli je logo opravdu videtelné.
def test_logo_visible(page: 'page'):
    page.goto("https://www.seznam.cz/")
    
    # Počkáme na logo, které má id="www-seznam-cz"
    page.wait_for_selector('#www-seznam-cz', timeout=10000)
    
    # Zkontrolujeme, že logo je přítomné a viditelné
    assert page.is_visible('#www-seznam-cz')


    
