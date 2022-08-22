from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


class BotOp:
    options = Options()
    options.add_argument('--ignore-ssl-error=yes')
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(executable_path="C:\Web Drivers for Selenium\chromedriver_win32 (103)/chromedriver",
                              options=options)

    def __init__(self):
        self.topic_rename = "Renamed Topic"
        self.sirie_rename = "Rename Serie"
        self.text_change = "Renamed Text"
        self.popup_rename = "Rename Popup"

        self.test_message = "Hello there its test message"
        self.tag_name = "Morning Tag"
        self.actions = ActionChains(self.driver)
        self.plus_button = self.driver.find_element(By.XPATH,
                                          "//*[@id='cdk-drop-list-0']/div[2]/div[2]/div/app-serie-list/div/div[2]")
        self.popup_element = self.driver.find_element(By.XPATH,
                                            "/html/body/ngb-modal-window/div/div/app-popup-modal/div/div[1]/div/select")

        # Mouse actions
        img_placeholder = self.driver.find_element(By.XPATH, "//*[@id='slide-2248']/div/app-generic-message/div[2]/app-cb-file-uploader/span")


    @classmethod
    def bot_operation(cls, plus_button, test_message, popup_element, tag_name):

        # Messanger section
        cls.driver.find_element(By.XPATH, "/html/body/app-root/div/app-dashboard-main/div/main/app-sidebar/aside/nav/ul/li[2]/div/a[2]").click()

        # Creating another topic
        cls.driver.find_element(By.XPATH, "//*[@id='topicGroupScrollEl']/div[2]/div[1]/div[1]/span").click()

        # Creating another serie
        cls.driver.execute_script("arguments[0].scrollIntoView();", plus_button)
        plus_button.click()

        cls.driver.find_element(By.XPATH, "//*[@id='serie-249']/span").click()

        # Creating a text message
        cls.driver.find_element(By.XPATH, "//*[@id='tour-text-create']").click()

        # Writing a text messaga
        cls.driver.find_element(By.XPATH, "//*[starts-with(@id, 'fbm-text-')]").send_keys(test_message)

        # Creating button
        cls.driver.find_element(By.XPATH, "//*[starts-with(@id, 'msg-')]").click()

        # Popup
        cls.driver.find_element(By.XPATH,
                            "//div[contains(@class, 'd-flex align-items-center width-fit popup-reply-add cursor-pointer default-msg-step-2 ug-tour-popup-create py-2 ng-star-inserted')]").click()
        cls.driver.implicitly_wait(10)

        # creating a popup
        popup_element.click()
        drop = Select(popup_element)
        drop.select_by_value("14: 1dcbb71d-4aea-42c9-b98c-77ffbdd97d01")

        # adding the tag
        cls.driver.find_element(By.XPATH, "//*[@id='mat-chip-list-input-0']").send_keys(tag_name)

        # closing the tag window for serie
        cls.driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-popup-modal/div/form/div/a").click()


    @classmethod
    def rename(cls, topic_rename, sirie_rename, text_change, popup_rename, actions, img_placeholder):

        # Rename Topic
        cls.driver.find_element(By.XPATH,
                            "/html/body/app-root/div/app-dashboard-main/div/main/div/app-build/div/div[2]/app-build-detail/div/div[1]/header/div[1]/input").clear()
        cls.driver.find_element(By.XPATH,
                            "/html/body/app-root/div/app-dashboard-main/div/main/div/app-build/div/div[2]/app-build-detail/div/div[1]/header/div[1]/input").send_keys(
            topic_rename)

        # Rename Serie
        cls.driver.find_element(By.XPATH,
                            "/html/body/app-root/div/app-dashboard-main/div/main/div/app-build/div/div[2]/app-build-detail/div/div[1]/div/div/div/div[1]/div/input").clear()
        cls.driver.find_element(By.XPATH,
                            "/html/body/app-root/div/app-dashboard-main/div/main/div/app-build/div/div[2]/app-build-detail/div/div[1]/div/div/div/div[1]/div/input").send_keys(
            sirie_rename)

        # Text Change
        cls.driver.find_element(By.XPATH, "//*[starts-with(@id, 'fbm-text-')]").clear()
        cls.driver.find_element(By.XPATH, "//*[starts-with(@id, 'fbm-text-')]").send_keys(text_change)
        # Popup rename
        cls.driver.find_element(By.XPATH, "//*[starts-with(@id, 'popupElement-')]").click()
        cls.driver.find_element(By.XPATH,
                            "/html/body/ngb-modal-window/div/div/app-popup-modal/div/form/div/div/div[1]/input").clear()
        cls.driver.find_element(By.XPATH,
                            "/html/body/ngb-modal-window/div/div/app-popup-modal/div/form/div/div/div[1]/input").send_keys(
            popup_rename)

        # closing the popup window
        cls.driver.implicitly_wait(10)
        cls.driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-popup-modal/div/form/div/a").click()

        # Filter by topic group name
        cls.driver.find_element(By.XPATH, "//*[@id='topicGroupScrollEl']/div[1]/div/div[2]/input").send_keys("Message Group")
        cls.driver.find_element(By.XPATH, "//*[@id='topicGroupScrollEl']/div[1]/div/div[2]/input").clear()

        # Adding image message
        cls.driver.find_element(By.XPATH, "//*[@id='tour-text-image-create']").click()
        actions.move_element(img_placeholder).click().send_keys("D:/Sample Images/sample_img.jpg").perform()

        # Drag and Drop Message
        source_element = cls.driver.find_element(By.XPATH, "//*[@id='serie-227']/span")
        target_element = cls.driver.find_element(By.XPATH, "//*[@id='serie-216']")

        actions.drag_and_drop(source_element, target_element).perform()

























