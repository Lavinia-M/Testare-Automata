from pages.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignInPage(BasePage):
    URL = "https://jules.app/sign-in"
    PAGE_TITLE = "Jules"

    def go_to(self, url_text):
        element = self.driver.find_element(By.LINK_TEXT, url_text)
        element.click()

    def input_email(self, email):
        email_element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[1]/div/div/input')
        email_element.send_keys(email)

    def input_password(self, password):
        password_element = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div/div[2]/div/div/input')
        password_element.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div/div[3]/button')
        login_button.click()

    def message_text_error(self):
        message_error = self.driver.find_element(By.CLASS_NAME, "jss6 jss129")
        return message_error.text()

    def sign_up_button(self):
        sign_up_button_selector = self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/form/div/div[4]/a')
        sign_up_button_selector.click()

