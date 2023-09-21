import random
import time
from string import ascii_letters

import allure
from selenium.webdriver import Keys

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from tests.user_data import EMAIL, PASSWORD


class MainPage(BasePage):
    locators = MainPageLocators()

    def authorization(self):
        with allure.step(f'Input email: {EMAIL}.'):
            self.element_is_presence(self.locators.INPUT_EMAIL).send_keys(EMAIL)
        # with allure.step(f'Input password: {PASSWORD}.'):
        self.element_is_presence(self.locators.INPUT_PASSWORD).send_keys(PASSWORD)
        with allure.step(f'Click button: LOG IN.'):
            self.element_is_presence(self.locators.LOG_IN_BUTTON).click()
        with allure.step(f'Check word "Good" is presence in footer.'):
            good_evening_text = self.element_is_presence(self.locators.GOOD_EVENING_TEXT).text
        return good_evening_text

    def create_sms(self):
        sms_button = self.element_is_presence(self.locators.SMS_BUTTON)
        with allure.step(f'Click SMS button.'):
            sms_button.click()
        create_campaning_button = self.element_is_presence(self.locators.CREATE_CAMPANING_BUTTON)
        with allure.step(f'Click campaning button.'):
            create_campaning_button.click()
        messaging_button = self.element_is_presence(self.locators.MESSAGING_BUTTON)
        with allure.step(f'Click messaging button.'):
            messaging_button.click()
        with allure.step(f'Click choose project.'):
            self.element_is_presence(self.locators.CHOSSE_PROJECT).click()
        with allure.step(f'Click create new project button.'):
            self.element_is_presence(self.locators.CREATE_NEW_PROJECT_BUTTON).click()
        with allure.step(f'Input company name: Test Company.'):
            input_campaning_name = self.element_is_presence(self.locators.INPUT_CAMPANING_NAME).send_keys(
                f'Test Company {random.randint(1, 99)}')
        input_project_name = (self.element_is_presence(self.locators.INPUT_PROJECT_NAME))
        random_project_name = [random.choice(ascii_letters) for _ in range(16)]
        with allure.step(f'Input random prject name: {random_project_name}.'):
            input_project_name.send_keys(random_project_name)
        next_button = self.element_is_clickable(self.locators.NEXT_BUTTON)
        with allure.step(f'Click Next.'):
            next_button.click()
        use_sms = self.element_is_presence(self.locators.SELECT_WANT_USE_SMS)
        with allure.step(f'Click want use sms.'):
            use_sms.click()
        button_done = self.element_is_presence(self.locators.BUTTON_DONE)
        with allure.step(f'Click Done.'):
            button_done.click()
        with allure.step(f'Click Marketing.'):
            self.element_is_presence(self.locators.MARKETING).click()
        button_done = self.element_is_presence(self.locators.BUTTON_DONE)
        with allure.step(f'Click Done.'):
            button_done.click()
        self.action_move_to_element(self.element_is_presence(self.locators.SMS_TEMPLATE_DIV))
        design_button = self.element_is_presence(self.locators.BUTTON_DESIGN)
        with allure.step(f'Click Design.'):
            design_button.click()
        with allure.step(f'Click select profile.'):
            self.element_is_visible(self.locators.SELECT_PROFILE).click()
        with allure.step(f'Profile selected.'):
            self.element_is_visible(self.locators.PROFILE).click()
        with allure.step(f'Click add list.'):
            self.element_is_presence(self.locators.ADD_LIST_BUTTON).click()
        time.sleep(0.5)
        with allure.step(f'Click my board checkbox.'):
            self.element_is_presence(self.locators.MY_BOARD_CHECKBOX).click()
        time.sleep(0.5)
        with allure.step(f'Click Done.'):
            self.element_is_presence(self.locators.ADD_RECIPIENCT_DONE_BUTTON).click()
        time.sleep(0.5)
        message_editor = self.element_is_presence(self.locators.MESSAGE_EDITOR)
        message_editor.click()
        with allure.step(f'Clear message editor place.'):
            message_editor.send_keys(Keys.DELETE * 40)
            message_editor.send_keys(Keys.BACKSPACE * 40)
            message_editor.send_keys(Keys.DELETE * 40)
        with allure.step(f'Input text: Hellow world!'):
            message_editor.send_keys('Hellow world!')
        with allure.step(f'Click emoji button.'):
            self.element_is_presence(self.locators.EMOJY_BUTTON).click()
        with allure.step(f'Input random 10 emoji.'):
            emojy_list = self.elements_are_present(self.locators.EMOJY_LIST)
            result = []
            for i in range(10):
                char = emojy_list[random.randint(1, 100)]
                char.click()
                result.append(char.text)
            message_editor.send_keys(Keys.ESCAPE)
        with allure.step(f'Click personalize button.'):
            self.element_is_presence(self.locators.PERSONALIZD_BUTTON).click()
            self.element_is_presence(self.locators.DROP_DOWN_PERSONALIZD).click()
            personalizd_drop_down = self.element_is_presence(self.locators.LIST_PERSONALIZD)
            personalizd_drop_down.click()
        with allure.step(f'Select random value from dropdown: {personalizd_drop_down.text}.'):
            pass
        with allure.step(f'Input random int eight-digit value.'):
            self.element_is_presence(self.locators.INPUT_VALUE).send_keys(random.randint(10000000, 99999999))
        with allure.step(f'Click Insert.'):
            self.element_is_presence(self.locators.INSERT_BUTTON).click()
        message_editor.send_keys(Keys.ESCAPE)
        with allure.step(f'Click Insert Link.'):
            self.element_is_presence(self.locators.INSERT_LINK_BUTTON).click()
        with allure.step(f'Input link: https://www.google.com/.'):
            self.element_is_presence(self.locators.INPUT_URL).send_keys('https://www.google.com/')
        with allure.step(f'Click Insert.'):
            self.element_is_presence(self.locators.INSERT_BUTTON).click()
        message_editor.send_keys(Keys.ESCAPE)
        with allure.step(f'Click publish button.'):
            publish_button = self.element_is_clickable(self.locators.BUTTON_PUBLISH)
            self.go_to_element(publish_button)
            publish_button.click()
        with allure.step(f'Check that Success mesage is presence.'):
            success = self.element_is_visible(self.locators.SUCCESS_MESSAGE)
        with allure.step(f'Click Done.'):
            self.element_is_clickable(self.locators.FINISH_DONE).click()
        return success.text

    def check_sms_button(self):
        self.element_is_clickable(self.locators.SMS_BUTTON).click()
        return self.element_is_clickable(self.locators.SMS_BUTTON).text

    def check_create_campaning_button(self):
        return self.element_is_clickable(self.locators.CREATE_CAMPANING_BUTTON).text
