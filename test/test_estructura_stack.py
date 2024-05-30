import pytest
import allure
from selenium import webdriver
from webdriver_manager import chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


class Test:
    btn_locator_formular_pregunta = (
        By.XPATH, "//a[@class='ws-nowrap s-btn s-btn__filled']")
    txt_locator_buscar = (By.NAME, "q")
    btn_locator_aceptar_cookies = (By.ID, "onetrust-accept-btn-handler")
    btn_locator_usuarios = (By.ID, "nav-users")
    btn_locator_iniciar_sesion = (
        By.XPATH, "//a[@data-gps-track='login.click']")

    def test_estructura(self):
        driver = webdriver.Chrome(service=Service(
            chrome.ChromeDriverManager().install()))
        with allure.step("Nos dirigimos a la pagina stackoverflow en espanol"):
            driver.get("https://es.stackoverflow.com/")
        time.sleep(3)
        btn_formular_pregunta = driver.find_element(
            *self.btn_locator_formular_pregunta)
        btn_formular_pregunta.is_enabled
        txt_buscar = driver.find_element(*self.txt_locator_buscar)
        txt_buscar.is_enabled
        btn_aceptar_cookies = driver.find_element(
            *self.btn_locator_aceptar_cookies)
        btn_aceptar_cookies.is_enabled
        btn_usuarios = driver.find_element(*self.btn_locator_usuarios)
        btn_usuarios.is_enabled
        btn_iniciar_sesion = driver.find_element(
            *self.btn_locator_iniciar_sesion)
        btn_iniciar_sesion.is_enabled


if __name__ == "__main__":
    pytest.main()
