from selenium.webdriver.common.by import By
from .base_page import BasePage
import pytest

class PaginaInicio(BasePage):
    SEARCH_BAR = (By.ID, "cb1-edit")

    BUTTON_SEARCH = (By.XPATH, "//div[@class='nav-icon-search' and @role='img']")

    #VALIDAR QUE EL BOTON ESTE MANDA A INICIO
    LOGO_NAVEGAR = (By.CSS_SELECTOR, ".nav-logo")

    DROPDOWN_CATEGORIAS = (By.XPATH, "//a[@class='nav-menu-categories-link' and @data-js='nav-menu-categories-trigger']")

    BUTTON_OFERTAS = (By.XPATH, "//a[text()='Ofertas']")

    def navigate_mercadolibre(self):
        self.navigate_to("https://www.mercadolibre.com.ar")

    def click_boton_busqueda(self):
        self.click(self.BUTTON_SEARCH)


    