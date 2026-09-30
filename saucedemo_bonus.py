from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_saucedemo_explicit_wait_order_complete(driver):
    """
    Закрывает критерий: 'Добавьте явное ожидание для текста об успешной покупке'.
    """
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    # Авторизация
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Покупка
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # Форма
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Ivan")
    driver.find_element(By.ID, "last-name").send_keys("Ivanov")
    driver.find_element(By.ID, "postal-code").send_keys("101000")
    driver.find_element(By.ID, "continue").click()

    # Оплата и завершение
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

    # Явное ожидание для текста об успешной покупке
    complete_header = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")),
        message="Текст завершения покупки не появился",
    )
    assert complete_header.text == "Thank you for your order!"