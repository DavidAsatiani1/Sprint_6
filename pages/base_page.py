import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Найти элемент с локатором: {locator}")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Кликнуть на элемент с локатором: {locator}")
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step("Получить текст элемента с локатором: {locator}")
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Отправить значение '{value}' в элемент с локатором: {locator}")
    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step("Перейти по URL: {url}")
    def cross_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    @allure.step("Переключиться на вкладку: {driver}")
    def tab_switch(self, driver):
        self.driver.switch_to.window(driver.window_handles[1])

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидание видимости элемента с локатором: {locator}")
    def wait_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step("Открыть страницу по URL: {url}")
    def open_page(self, url):
        self.driver.get(url)
