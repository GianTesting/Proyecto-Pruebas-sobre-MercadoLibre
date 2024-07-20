import pytest
import time
from pages.inicio_pagina import PaginaInicio
from pages.pagina_resultados import PaginaResultados
import allure


@allure.title('Validar que encuentra productos al buscar "iphone" en la barra de búsqueda')
@allure.feature('Búsqueda de productos')
@allure.story('Buscar productos en Mercado Libre')

def test_buscar_productos(browser, pagina_inicio, pagina_resultados):
    with allure.step("Dado que navego a la página de mercado libre"):
        pagina_inicio.navigate_mercadolibre()
        browser.maximize_window()
    with allure.step("Cuando escribo Iphone en la barra de busqueda y clickeo el boton 'buscar'"):
        pagina_inicio.type_text(PaginaInicio.SEARCH_BAR, "Iphone")
        browser.get("https://listado.mercadolibre.com.ar/iphone#D[A:Iphone]")
        pagina_inicio.click_boton_busqueda()

    with allure.step("Puedo verificar que hay resultados obtenidos"):
        # Espera y obtiene los resultados de búsqueda
        resultados = pagina_resultados.esperar_y_obtener_resultados()
        
        # Verifica que la lista de resultados no esté vacía
        assert len(resultados) > 0, "No se encontraron resultados"

        # si se ejecuta el archivo usando pytest -s test_busqueda.py va a mostrar los resultados encontrados por consola.
        #for index, resultado in enumerate(resultados):
            #print(f"Resultado {index + 1}: {resultado.text}")


@allure.title('Validar que el dropdown "Ordenar por" funciona correctamente')
@allure.feature('Búsqueda de productos')
@allure.story('Ordenar productos de menor a mayor precio')
@pytest.mark.ordenar
def test_ordenar_productos_manor_a_mayor(browser, pagina_inicio, pagina_resultados):
    with allure.step("Dado que navego a la página de Mercado Libre"):
        pagina_inicio.navigate_mercadolibre()
        browser.maximize_window()

    with allure.step("Cuando escribo 'Iphone' en la barra de búsqueda y clickeo el botón 'buscar'"):
        pagina_inicio.type_text(PaginaInicio.SEARCH_BAR, "Iphone")
        browser.get("https://listado.mercadolibre.com.ar/iphone#D[A:Iphone]")
        pagina_inicio.click_boton_busqueda()


    with allure.step("Y uso el dropdown para ordenar de menor a mayor"):
        pagina_resultados.ordenar_de_menor_precio_a_mayor()

    with allure.step("Obtener precios después de ordenar"):
        precios_despues = pagina_resultados.obtener_precios()
        assert len(precios_despues) > 0, "No se encontraron precios después de ordenar"
        print("Precios después de ordenar:")
        pagina_resultados.imprimir_precios()

    with allure.step("Verificar que los precios están ordenados de menor a mayor"):
        precios_ordenados = sorted(precios_despues)
        assert precios_despues == precios_ordenados, "Los precios no están ordenados de menor a mayor"


@allure.title('Validar que el dropdown "Ordenar por" funciona correctamente')
@allure.feature('Búsqueda de productos')
@allure.story('Ordenar productos de mayor a menor precio')
@pytest.mark.ordenar
def test_ordenar_productos_mayor_menor(browser, pagina_inicio, pagina_resultados):
    with allure.step("Dado que navego a la página de Mercado Libre"):
        pagina_inicio.navigate_mercadolibre()
        browser.maximize_window()

    with allure.step("Cuando escribo 'Iphone' en la barra de búsqueda y clickeo el botón 'buscar'"):
        pagina_inicio.type_text(PaginaInicio.SEARCH_BAR, "Iphone")
        browser.get("https://listado.mercadolibre.com.ar/iphone#D[A:Iphone]")
        pagina_inicio.click_boton_busqueda()
    
    with allure.step("Y uso el dropdown para ordenar de mayor a menor"):
        pagina_resultados.ordenar_de_mayor_precio_a_menor()

    with allure.step("Obtener precios después de ordenar"):
        precios_despues = pagina_resultados.obtener_precios()
        assert len(precios_despues) > 0, "No se encontraron precios después de ordenar"
        print("Precios después de ordenar:")
        pagina_resultados.imprimir_precios()

    with allure.step("Verificar que los precios están ordenados de mayor a menor"):
        precios_ordenados = sorted(precios_despues, reverse=True)
        assert precios_despues == precios_ordenados, "Los precios no están ordenados de mayor a menor"

    with allure.step("Verificar que los precios están ordenados de menor a mayor"):
        precios_ordenados = sorted(precios_despues)
        assert precios_despues == precios_ordenados, "Los precios no están ordenados de mayor a menor"