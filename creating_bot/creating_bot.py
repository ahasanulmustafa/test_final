from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


class Bot:
    options = Options()
    options.add_argument('--ignore-ssl-error=yes')
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(executable_path="C:\Web Drivers for Selenium\chromedriver_win32 (103)/chromedriver",
                              options=options)

    def __init__(self):
        self.bot_name = "Test Bot"
        self.login_user = self.driver.find_element(By.XPATH,
                                                   "/html/body/app-root/div/app-layout/main/app-navbar/nav/div[4]/ul/li/ul/li[1]/a/div[2]/span[2]").text
        self.home_page = "/html/body/app-root/div/app-dashboard-main/div/app-navbar/nav/div[1]"
        self.bot_create = "/html/body/ngb-modal-window/div/div/app-create-bot-modal/div[1]"

    @classmethod
    def creating_a_bot(cls, bot_name, login_user, home_page, bot_create):

        # Verifying homepage load
        if cls.driver.find_element(By.XPATH, home_page):
            print("Home Page successfully loaded.")
        else:
            print("Home Page did not load.")

        # Verify login
        cls.driver.find_element(By.XPATH,
                                "/html/body/app-root/div/app-dashboard-main/div/app-navbar/nav/div[4]/ul/li/a").click()
        if login_user == "ehsan1014@gmail.com":
            print("Login Successful")
        else:
            print("User login failed")

        # Opening bot option
        cls.driver.find_element(By.XPATH,
                                "/html/body/app-root/div/app-dashboard-main/div/app-navbar/nav/div[3]/div").click()
        cls.driver.find_element(By.XPATH,
                                "/html/body/app-root/div/app-dashboard-main/div/app-navbar/nav/div[3]/ul/li[3]/a/div").click()

        # Verifying bot create dropdown
        if cls.driver.find_element(By.XPATH, bot_create):
            print("Bot create dropdown successfully opened")
        else:
            print("bot create option did not open")

        # Create new bot
        cls.driver.find_element(By.NAME, "botName").clear()
        cls.driver.find_element(By.NAME, "botName").send_keys(bot_name)

        # Verifying new bot name
        name = cls.driver.find_element(By.NAME, "botName")
        bot_value = name.get_attribute('value')
        if bot_value == bot_name:
            print("The bot name verified")
        else:
            print("The bot name not the same as the input")

        # Selecting platform from dropdown
        element = cls.driver.find_element(By.XPATH,
                                          "/html/body/ngb-modal-window/div/div/app-create-bot-modal/div[2]/app-bot-templates/div/div[2]/div[2]/select")
        drop = Select(element)
        drop.select_by_visible_text("Facebook")

        # Selecting the language
        cls.driver.find_element(By.XPATH,
                                "/html/body/ngb-modal-window/div/div/app-create-bot-modal/div[2]/app-bot-templates/div/div[2]/div[2]/div/button[2]").click()

        # Starting with template
        cls.driver.find_element(By.XPATH,
                                "/html/body/ngb-modal-window/div/div/app-create-bot-modal/div[2]/app-bot-templates/div/div[3]/div[2]/div[3]/button").click()
