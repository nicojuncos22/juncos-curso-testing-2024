import pytest
import allure
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

    destin_destac = (
        By.XPATH, "//a[@href='https://www.aerolineas.com.ar/descubri-tu-destino-con-millas']")

    destin_destac = (
        By.XPATH, "//a[@href='https://www.aerolineas.com.ar/compra-o-transferi-millas']")


def test_estructura(self):
    driver = webdriver.Chrome(service=Service(
        chrome.ChromeDriverManager().install))
    driver.get("")


if __name__ == "__main__":
    pytest.main()
