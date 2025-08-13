import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Executa em modo headless, ideal para rodar em pipelines de CI/CD como o GitHub Actions.
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
