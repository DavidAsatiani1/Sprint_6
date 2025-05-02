from selenium.webdriver.common.by import By


class HomePageLocators:
    HEADER_ORDER_BUTTON = [By.XPATH, './/div[contains(@class, "Header_Nav")]/button[text()="Заказать"]'] #кнопка Заказать в шапке
    PAGE_ORDER_BUTTON = [By.XPATH, './/div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]'] #кнопка Заказать на странице сайта
    QUESTION = [By.XPATH, './/div[@id = "accordion__heading-{}"]'] #вопрос
    ANSWER = [By.XPATH, './/div[@id="accordion__panel-{}"]/p'] #ответ
    COOKIE = [By.ID, 'rcc-confirm-button'] #принять куки
    LAST_QUESTION = [By.XPATH, '(.//div[contains(@id,"accordion__heading-")])[last()]'] #последний вопрос в разделе "Вопросы о важном"
    LOGO_SCOOTER = [By.XPATH, './/a[@href = "/"]'] #логотип Самокат
    LOGO_YANDEX = [By.XPATH, './/a[@href = "//yandex.ru"]'] #логотип Яндекс