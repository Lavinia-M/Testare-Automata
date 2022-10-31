from pages.basepage import BasePage
from selenium.webdriver.common.by import By


class SignUpPage(BasePage):
    URL = "https://jules.app/sign-up"
    PAGE_TITLE = "Jules"

    def go_to(self, url_text):
        element = self.driver.find_element(By.LINK_TEXT, url_text)
        element.click()

    def go_to_login_btn(self):
        login_btn_selector = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[1]/div/div[4]/a/button')
        login_btn_selector.click()

    def person_button(self):
        selector_button = self.driver.find_element(By.XPATH, "//input[@value='personal']")
        selector_button.click()

    def continue_button(self):
        selector_continue_btn = self.driver.find_element(By.CLASS_NAME, "jss12 jss24")
        selector_continue_btn.click()

    def input_field(self, field):
        field_element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[4]/div[2]/div/div[2]/div/div/input')
        field_element.send_keys(field)