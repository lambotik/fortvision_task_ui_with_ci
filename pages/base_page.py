import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.time_out = 10

    def open(self):
        with allure.step(f'Open page: {self.url}'):
            self.driver.get(self.url)

    def get_current_url(self):
        get_url = self.url
        with allure.step(f'Get url: {get_url}'):
            return get_url

    def element_is_visible(self, locator):
        with allure.step(f'Check element is visible: {locator}'):
            return wait(self.driver, self.time_out).until(EC.visibility_of_element_located(locator))

    def element_is_clickable(self, locator):
        with allure.step(f'Check element is clickable: {locator}'):
            return wait(self.driver, self.time_out).until(EC.element_to_be_clickable(locator))

    def element_is_presence(self, locator):
        with allure.step(f'Check element is presence: {locator}'):
            return wait(self.driver, self.time_out).until(EC.presence_of_element_located(locator))

    @allure.step('Check elements are presence.')
    def elements_are_present(self, locator):
        return wait(self.driver, self.time_out).until(EC.presence_of_all_elements_located(locator))

    def action_move_to_element(self, element):
        with allure.step(f'Move to {element}'):
            action = ActionChains(self.driver)
            action.move_to_element(element)
            action.perform()

    def action_double_click(self, element):
        with allure.step(f'Double click {element}'):
            action = ActionChains(self.driver)
            action.double_click(element).perform()

    def go_to_element(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Check elements are presence.')
    def element_visibility_of(self, locator):
        return wait(self.driver, self.time_out).until(EC.visibility_of(locator))

    @allure.step('Attach screenshot')
    def attach_screenshot(self, element):
        """Create screenshot of current window and attach it in allure report
        Args:
         - file_name: str like 'Linkedin_button_not_found'
        """
        element_name = ''.join(element)
        allure.attach(self.driver.get_screenshot_as_png(), name=element_name, attachment_type=AttachmentType.PNG)
