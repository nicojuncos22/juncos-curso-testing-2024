import pytest
import allure
import time
from selenium import webdriver
from webdriver_manager import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


class Test:

    btn_log_in = (By.CLASS_NAME, "styled__MenuItemButton-sc-1vfcng3-0 gsxGtH")
    btn_menu = (By.CLASS_NAME, "styled__MenuDisplayer-sc-22nvvu-20 fYKhfr")
    box_username_input = (By.ID, "userNameInput")
    box_password_input = (By.ID, "passwordInput")
    btn_ingresar = (By.XPATH, "//button[@type='submit']")
    btn_suscribe = (
        By.CLASS_NAME, "button__StyledButton-sc-17uyx03-1 dDPisS button-subscribe")
    main_ppal = (By.ID, "main")
    logo_space = (
        By.CLASS_NAME, "styled__StyledHybridLink-sc-1m5nbej-0 dyXmAb arsa-logo")
    destin_destac_a = (
        By.XPATH, "//a[@href='https://www.aerolineas.com.ar/descubri-tu-destino-con-millas']")
    destin_destac_b = (
        By.XPATH, "//a[@href='https://www.aerolineas.com.ar/compra-o-transferi-millas']")

    @allure.title("Validar estructura en aerolineas")
    @allure.description("Validar que se pueda ingresar a la pagina de aerolineas y que la estructura sea correcta")
    def test_estructura(self):
        driver = webdriver.Chrome(service=Service(
            chrome.ChromeDriverManager().install))
        with allure.step("Nos dirigimos a la pagina aerolineas"):
            driver.get("https://www.aerolineas.com.ar/")
        time.sleep(3)
        with allure.step("Validar que se muestre el boton de log in"):
            btn_log_in = driver.find_element(*self.btn_log_in)
            assert btn_log_in.is_enabled  # Validar que el boton sea visible
        with allure.step("Validar que se muestre el boton de menu"):
            btn_menu = driver.find_element(*self.btn_menu)
            assert btn_menu.is_enabled
        # Validar que los inputs sean visibles
        with allure.step("Validar que se muestre el input de username y password"):
            box_username_input = driver.find_element(*self.box_username_input)
            assert box_username_input.is_enabled
            box_password_input = driver.find_element(*self.box_password_input)
            assert box_password_input.is_enabled
        with allure.step("Validar que se muestre el boton de ingresar"):
            btn_ingresar = driver.find_element(*self.btn_ingresar)
            assert btn_ingresar.is_enabled
        with allure.step("Validar que se muestre el boton de suscribirse"):
            btn_suscribe = driver.find_element(*self.btn_suscribe)
            assert btn_suscribe.is_enabled
        with allure.step("Validar que se muestre el main principal"):
            main_ppal = driver.find_element(*self.main_ppal)
            assert main_ppal.is_enabled
        with allure.step("Validar que se muestre el logo de aerolineas"):
            logo_space = driver.find_element(*self.logo_space)
            assert logo_space.is_enabled
        with allure.step("Validar que se muestren los destinos destacados A y B"):
            destin_destac_a = driver.find_element(*self.destin_destac_a)
            assert destin_destac_a.is_enabled
            destin_destac_b = driver.find_element(*self.destin_destac_b)
            assert destin_destac_b.is_enabled


if __name__ == "__main__":
    pytest.main()
