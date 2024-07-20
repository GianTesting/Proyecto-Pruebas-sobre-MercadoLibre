from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



import pytest


class PaginaResultados(BasePage):

    RESULTADOS_BUSQUEDA = (By.CSS_SELECTOR, ".ui-search-layout__item")

    ORDENAR_POR_BUTTON = (By.CSS_SELECTOR, "button.andes-dropdown__trigger[aria-haspopup='listbox']")


    MENOR_PRECIO_XPATH = (By.XPATH, "//span[@class='andes-list__item-primary' and text()='Menor precio']")

    MAYOR_PRECIO_XPATH = (By.XPATH, "//span[@class='andes-list__item-primary' and text()='Mayor precio']")

    PRECIOS_BUSQUEDA = (By.XPATH, 
                        "//div[@class='poly-price__current']/span[@class='andes-money-amount andes-money-amount--cents-superscript']/span[@class='andes-money-amount__fraction']") 


    def esperar_y_obtener_resultados(self, timeout=10):
        # Realizo una espera explícita para esperar que aparezcan los elementos de la página
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(self.RESULTADOS_BUSQUEDA)
        )
        # Obtén todos los elementos de búsqueda
        return self.driver.find_elements(*self.RESULTADOS_BUSQUEDA)
    

    def ordenar_de_menor_precio_a_mayor(self):

        self.esperar_a_que_sea_clickeable(self.ORDENAR_POR_BUTTON)
        
        self.esperar_a_que_sea_clickeable(self.MENOR_PRECIO_XPATH)
             
    def ordenar_de_mayor_precio_a_menor(self):
        self.esperar_a_que_sea_clickeable(self.ORDENAR_POR_BUTTON)
        
        self.esperar_a_que_sea_clickeable(self.MAYOR_PRECIO_XPATH)

    def obtener_precios(self, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(self.PRECIOS_BUSQUEDA)
            )
            elementos_precios = self.driver.find_elements(*self.PRECIOS_BUSQUEDA)
            precios = []
            for elemento in elementos_precios:
                precio_texto = elemento.text.replace(".", "").replace(",", ".")
                try:
                    precio_numero = float(precio_texto)
                    precios.append(precio_numero)
                except ValueError:
                    print(f"Error al convertir el precio: {precio_texto}")
                    continue
            return precios
        except Exception as e:
            print(f"Excepción capturada: {str(e)}")
            return []
        
    def imprimir_precios(self):
        precios = self.obtener_precios()
        if precios:
            for index, precio in enumerate(precios):
                print(f"Precio {index + 1}: {precio}")
        else:
            print("No se encontraron precios.")

