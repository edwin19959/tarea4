import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime

@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()

def test_instagram_login(driver):
    
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(2)

    #  elementos de usuario y contraseña 
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    # Introducir credenciales
    username.send_keys("tuRealmalgueton")  
    password.send_keys("bloke23")  
    login_button.click()

    time.sleep(5)

   #verificacion de mensaje deerror con  XPath
    try:
       
        error_message = driver.find_element(By.XPATH, "//div[contains(text(), 'contraseña no es correcta') or contains(text(), 'password was incorrect')]")
        if error_message.is_displayed():
            print(f"Prueba fallida: {error_message.text}")
            raise AssertionError("Credenciales incorrectas detectadas.")
    except NoSuchElementException:
        
        assert "Instagram" in driver.title, "Prueba fallida: No se detectó error ni se inició sesión."
        print("Prueba exitosa: Login realizado con éxito.")

#Reporte
if __name__ == "__main__":
    
    report_name = f"C:/Users/edwin/OneDrive/Escritorio/Nueva carpeta (4)/Reportes/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"

    pytest.main(["--html=" + report_name, 
                 "--maxfail=1", 
                 "--disable-warnings"])