import time


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

# Открытие гл. страницы, ввод в поиск, переход на 1 страницу, картинки, видео.
def testOne():
    # Вход на сайт.
    driver.get('https://yandex.ru/')
    time.sleep(2)

    # Добавление поисковой строки в переменную.
    SearchField = driver.find_element(By.ID, "text")

    # Ввод значений в поисковую строку.
    SearchField.send_keys('Selenium 4', Keys.ENTER)
    time.sleep(3)

    # Скролл страницы до футера.
    footer = driver.find_element(By.CSS_SELECTOR, "body > div.b-page__footer.serp.i-bem")
    ActionChains(driver) \
        .scroll_to_element(footer) \
        .perform()
    time.sleep(3)

    # Клик в футере "2".
    driver.find_element(By.CSS_SELECTOR, "body > main > div.main__center > div.main__content > div.content.i-bem > "
                                         "div.content__left > div.pager.i-bem > div > a:nth-child(2)").click()
    time.sleep(3)

    # Нажатие на вкладку "Картинки" в хедере.
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[2]/div[1]/a/span").click()
    time.sleep(3)

    # Нажатие на вкладку "Видео"
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[3]/div[1]/a/span").click()
    time.sleep(3)


testOne()

# Выход из браузера
driver.quit()
