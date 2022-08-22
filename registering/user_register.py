from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


class Register:
    options = Options()
    options.add_argument('--ignore-ssl-error=yes')
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(executable_path="C:\Web Drivers for Selenium\chromedriver_win32 (103)/chromedriver",
                              options=options)

    def __init__(self):
        self.organisation = "Test Organisation"
        self.bot_name = "Test Bot"

    @classmethod
    def register(cls, organisation, bot_name):
        # Accepting cookies
        cls.driver.find_element(By.XPATH, "/html/body/app-root/app-cookies-banner/div/div[2]/button[2]").click()
        cls.driver.implicitly_wait(10)

        # Organisation
        cls.driver.find_element(By.XPATH, "//*[@id='group_form']/div[1]/input").send_keys(organisation)

        # Agree to the terms and conditions
        cls.driver.find_element(By.NAME, "termsCheckedField").click()

        # Continue button
        cls.driver.find_element(By.XPATH, "//*[@id='group_form']/button").click()

        # Creating first bot
        cls.driver.find_element(By.XPATH, "/html/body/app-root/div/app-layout/main/main/section/section/app-start-bot-creation/section/div/button").click()
        cls.driver.implicitly_wait(10)
        cls.driver.find_element(By.NAME, "botName").clear()
        cls.driver.find_element(By.NAME, "botName").send_keys(bot_name)

        # Selecting from dropdown
        element = cls.driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-create-bot-modal/div[2]/app-bot-templates/div/div[2]/div[2]/select")
        drop = Select(element)
        drop.select_by_visible_text("Facebook")

        # Selecting the language
        cls.driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-create-bot-modal/div[2]/app-bot-templates/div/div[2]/div[2]/div/button[2]").click()

        # Starting with template
        cls.driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-create-bot-modal/div[2]/app-bot-templates/div/div[3]/div[2]/div[3]/button").click()

