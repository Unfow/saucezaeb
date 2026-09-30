from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс страницы с низкоуровневыми обёртками над Selenium WebDriver."""

    def __init__(self, driver: WebDriver, timeout: int = 15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str):
        """Переход по указанному адресу."""
        self.driver.get(url)

    def find_element(self, locator: tuple):
        """Ожидание появления и видимости элемента на странице."""
        return self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Элемент с локатором {locator} не отобразился за {self.wait._timeout} сек.",
        )

    def find_presence(self, locator: tuple):
        """Ожидание присутствия элемента в структуре DOM."""
        return self.wait.until(
            EC.presence_of_element_located(locator),
            message=f"Элемент {locator} отсутствует в DOM.",
        )

    def click(self, locator: tuple):
        """Ожидание кликабельности и клик по элементу."""
        element = self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Элемент {locator} не стал кликабельным.",
        )
        element.click()

    def get_text(self, locator: tuple) -> str:
        """Получение текста элемента."""
        return self.find_element(locator).text

    def switch_to_frame(self, frame_locator: tuple):
        """Ожидание доступности фрейма и переключение в него."""
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(frame_locator),
            message=f"Фрейм {frame_locator} недоступен для переключения.",
        )

    def switch_to_default_content(self):
        """Возврат контекста к основному документу страницы."""
        self.driver.switch_to.default_content()