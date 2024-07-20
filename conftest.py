import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.inicio_pagina import PaginaInicio
from pages.pagina_resultados import PaginaResultados

@pytest.fixture(scope="session")
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

@pytest.fixture
def pagina_inicio(browser):
    return PaginaInicio(browser)

@pytest.fixture
def pagina_resultados(browser):
    return PaginaResultados(browser)