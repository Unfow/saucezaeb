from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SecondFrame(BasePage):
    """
    Класс для работы со вторым фреймом (Selenium.dev).
    Инкапсулирован внутри класса MainPage.
    """

    # Ссылка на раздел Downloads в навигационном меню Selenium
    DOWNLOADS_NAV_LINK = (
        By.XPATH,
        "//a[contains(@href, '/downloads') and contains(@class, 'nav-link')]",
    )

    # Локатор ссылки на стабильную версию пакета Python на PyPI
    PYTHON_STABLE_LINK = (
        By.XPATH,
        "//a[contains(@href, 'pypi.org/project/selenium')]",
    )

    def go_to_downloads(self):
        """Переход в раздел Downloads внутри фрейма Selenium."""
        self.click(self.DOWNLOADS_NAV_LINK)

    def get_python_download_link(self) -> str:
        """
        Находит элемент со ссылкой на стабильную версию Python
        и возвращает значение атрибута href.
        """
        # Если ссылка ещё не видна (например, мы на главной selenium.dev), переходим в Downloads
        try:
            link_element = self.find_element(self.PYTHON_STABLE_LINK)
        except Exception:
            self.go_to_downloads()
            link_element = self.find_element(self.PYTHON_STABLE_LINK)

        return link_element.get_attribute("href")


class MainPage(BasePage):
    """Класс главной страницы https://practice-automation.com/iframes/"""

    # Селектор второго iframe на странице (поддерживает как id='iframe-2', так и порядковый селектор)
    SECOND_IFRAME_LOCATOR = (
        By.CSS_SELECTOR,
        "iframe#iframe-2, iframe:nth-of-type(2)",
    )

    def __init__(self, driver, timeout: int = 15):
        super().__init__(driver, timeout)
        # Инкапсуляция класса SecondFrame внутри MainPage
        self.second_frame = SecondFrame(driver, timeout)

    def switch_to_second_frame(self):
        """Переключение контекста драйвера во второй фрейм."""
        self.switch_to_default_content()
        self.switch_to_frame(self.SECOND_IFRAME_LOCATOR)

    def get_python_download_link_from_second_frame(self) -> str:
        """
        Комплексный метод: переключается во фрейм, извлекает ссылку
        и возвращает контекст обратно на базовую страницу.
        """
        self.switch_to_second_frame()
        link = self.second_frame.get_python_download_link()
        self.switch_to_default_content()
        return link