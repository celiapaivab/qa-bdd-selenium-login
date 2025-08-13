from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_scenario(context, scenario):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # roda sem interface gráfica
    chrome_options.add_argument("--no-sandbox")  # necessário no Actions
    chrome_options.add_argument("--disable-dev-shm-usage")  # evita problemas de memória
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--remote-allow-origins=*")
    chrome_options.add_argument("--user-data-dir=/tmp/temp-chrome-profile")  # diretório único

    context.driver = webdriver.Chrome(options=chrome_options)

def after_scenario(context, scenario):
    # Fecha o navegador após cada cenário
    if hasattr(context, "driver"):
        context.driver.quit()
