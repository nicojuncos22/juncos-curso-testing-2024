import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test:

    btn_aceptar_cookies = (
        By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
    buscador = (By.XPATH, "//input[@placeholder='Buscar…']")

    @pytest.fixture(autouse=True)  # Se ejecuta antes y despues de cada test
    def setup_teardown(self):  # Esta funcion sirve para inicializar y cerrar el driver
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        self.driver.maximize_window()
        self.driver.get("https://es.stackoverflow.com/")
        yield  # Lo que este despues de yield se ejecuta despues de cada test
        print("Cerrar Browser")
        self.driver.quit()

    @allure.title("Validar busqueda en stackoverflow")
    @allure.description("Validar que se pueda buscar en stackoverflow")
    def test_busqueda(self):
        driver = self.driver
        WebDriverWait(driver, 10).until(  # Espera...
            # ...hasta que el boton sea clickeable
            EC.element_to_be_clickable(self.btn_aceptar_cookies))
        # Paso de allure para reporte
        with allure.step("Validar que se muestre el boton de aceptar cookies"):
            btn_cookies = driver.find_element(*self.btn_aceptar_cookies)
            # si no estuviera assert, no se mostraria en el reporte
            assert btn_cookies.is_displayed()
        with allure.step("Aceptar cookies"):
            btn_cookies.click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(self.buscador))
        with allure.step("Validar que se muestre el buscador"):
            caja_busqueda = driver.find_element(*self.buscador)
            assert caja_busqueda.is_displayed()
        with allure.step("Realizar busqueda"):
            caja_busqueda.clear()
        with allure.step("Validamos que la caja de busqueda este vacia"):
            assert caja_busqueda.get_attribute("value") == ""
        with allure.step("Validamos que el len de la caja de busqueda sea 0"):
            assert len(caja_busqueda.get_attribute("value")) == 0
            caja_busqueda.send_keys("python")
        with allure.step("Validamos que la caja de busqueda contenga la palabra python"):
            assert caja_busqueda.get_attribute("value") == "python"
            caja_busqueda.send_keys(Keys.ENTER)
        with allure.step("Validar que se muestre el resultado de la busqueda"):
            assert "python" in driver.title


if __name__ == "__main__":
    pytest.main()
