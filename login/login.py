from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Login:

    url = 'https://localhost:4200/login/auth'

    options = Options()
    options.add_argument('--ignore-ssl-error=yes')
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(executable_path="C:\Web Drivers for Selenium\chromedriver_win32 (103)/chromedriver",
                              options=options)

    def __init__(self, email, password):
        self.email = email
        self.password = password

    @classmethod
    def loginGoogle(cls, email, password):
        cls.driver.get(cls.url)
        cls.driver.maximize_window()

        # login
        cls.driver.find_element(By.XPATH, "//*[@id='gapi-signin2']/div[2]").click()
        cls.driver.implicitly_wait(10)

        # Email Fields
        cls.driver.find_element(By.ID, "identifierId").send_keys(email)
        cls.driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button/span").click()
        cls.driver.implicitly_wait(10)

        # Password Field
        cls.driver.find_element(By.NAME, "password").send_keys(password)
        cls.driver.find_element(By.XPATH, "//*[@id='passwordNext']/div/button/span").click()

























