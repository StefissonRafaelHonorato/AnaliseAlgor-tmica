from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def create_browser():
    # cria e retorna o navegador configurado
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    diver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)