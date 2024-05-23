import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta

# Función para obtener la fecha actual más un mes


def obtener_proximo_mes():
    hoy = datetime.now()
    proximo_mes = hoy + timedelta(days=30)
    return proximo_mes.strftime("%d/%m/%Y")

# Función para obtener la fecha de regreso (7 días después)


def obtener_fecha_regreso():
    fecha_regreso = datetime.now() + timedelta(days=37)  # 30 días + 7 días
    return fecha_regreso.strftime("%d/%m/%Y")


# Configuración de Selenium
# Asegúrate de tener el driver de Chrome instalado y en el PATH
driver = webdriver.Chrome()
driver.get("https://www.aerolineas.com.ar/")


@allure.feature("Evaluación de vuelos en el sitio web de Aerolíneas Argentinas")
class TestEvaluacionAerolineas:

    @allure.story("Buscar vuelos desde Córdoba a Buenos Aires")
    def test_buscar_vuelos(self):
        desde = "Córdoba"
        hacia = "Aeroparque"

        # Ingresar las ubicaciones y las fechas en la página
        driver.find_element_by_id("from_search").send_keys(desde)
        driver.find_element_by_id("to_search").send_keys(hacia)
        driver.find_element_by_id("departure_date").clear()
        driver.find_element_by_id(
            "departure_date").send_keys(obtener_proximo_mes())
        driver.find_element_by_id("return_date").clear()
        driver.find_element_by_id("return_date").send_keys(
            obtener_fecha_regreso())

        # Buscar vuelos
        driver.find_element_by_id("btn-search").click()

        # Esperar a que los resultados de la búsqueda se carguen
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "segment-fare")))

        # Obtener los precios de los vuelos
        fares = driver.find_elements_by_class_name("segment-fare")
        for fare in fares:
            precio = fare.find_element_by_class_name("flight-price").text
            precio = float(precio.replace("$", "").replace(
                ".", "").replace(",", "."))  # Convertir a float
            with allure.step(f"Verificar vuelo de {desde} a {hacia}"):
                assert precio > 0, f"El precio del vuelo de {
                    desde} a {hacia} es menor o igual a 0"

        # Limpiar los campos para la próxima iteración
        driver.find_element_by_id("from_search").clear()
        driver.find_element_by_id("to_search").clear()

    def teardown_method(self, method):
        driver.quit()


if __name__ == "__main__":
    import pytest
    pytest.main()
