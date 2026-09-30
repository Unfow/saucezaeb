from pages.main_page import MainPage


def test_python_stable_download_link_in_second_frame(driver, base_url):
    """
    Проверка нахождения корректной ссылки на скачивание стабильной
    версии Selenium для Python во втором фрейме.
    """
    main_page = MainPage(driver)

    # 1. Открытие страницы (фикстуры driver и base_url независимы)
    main_page.open(base_url)

    # 2. Получение ссылки из инкапсулированного объекта second_frame
    python_link = main_page.get_python_download_link_from_second_frame()

    # 3. Проверка правильности полученной ссылки
    assert python_link is not None, "Ссылка на Python-пакет не была найдена!"
    assert "pypi.org/project/selenium" in python_link, (
        f"Ожидалась ссылка на PyPI Selenium, фактически получено: '{python_link}'"
    )