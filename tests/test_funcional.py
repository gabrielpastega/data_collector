import os
import pytest
import subprocess

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():
    # iniciar o streamlit em backgroun
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)
    # iniciar o webdriver usando GeckoDriver
    driver.set_page_load_timeout(5)
    yield driver

    # fechar o webdriver e o streamlit após o test
    driver.quit()
    process.kill()

def test_app_open(driver):
    # verificar se a página abre
    driver.get("http://localhost:8501")
    sleep(2)

def test_check_title_is(driver):
    # verificar se apágina abre
    driver.get("http://localhost:8501")
    # verifica se o título da página é
    sleep(2)
    # capturar o título da página
    page_title = driver.title
    # verificar se o título da página é o esperado
    expected_title = "Validador de schema Excel" 
    assert page_title == expected_title

# def test_check_streamlit_h1(driver):
#     # acessar a página do Streamlit
#     driver.get("http://localhost:8501")

#     # aguardar para garantir que a página foi carregada
#     sleep(2)

#     # capturar o primeiro elemento <h1> da página
#     h1_element = driver.find_element(By.TAG_NAME, "h1")

#     # verificar se o texto do elemento <h1> é o esperado
#     expected_text = "Insira o seu Excel para validação"
#     assert h1_element.text == expected_text