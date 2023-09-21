import allure
import pytest

from pages.main_page import MainPage


@allure.suite('Test Main Page')
class TestMainPage:
    @allure.title('Authorization customer')
    @allure.severity('HIGH')
    def test_just_open(self, driver):
        test_elements = MainPage(driver, 'https://my.fortvision.com/#/login')
        test_elements.open()
        assert 1 == 1

    @allure.step('Test Authorization.')
    @allure.severity('HIGH')
    @pytest.mark.xfail
    def test_fill_form(self, driver):
        test_elements = MainPage(driver, 'https://my.fortvision.com/#/login')
        test_elements.open()
        result = test_elements.authorization()
        assert 'Good' in result, 'Something went wrong!!!'

    @allure.step('Test Smoke send sms.')
    @pytest.mark.xfail
    def test_create_sms(self, driver):
        main_page = MainPage(driver, 'https://my.fortvision.com/#/dashboard')
        main_page.open()
        main_page.authorization()
        result = main_page.create_sms()
        assert "Success" == result, 'Something went wrong!!!'

@allure.feature('Test Main Page V2')
class TestMainPageV2:
    @allure.title('Authorization customer')
    @allure.severity('HIGH')
    def test_authorization_form(self, driver_v2):
        assert 'Good' in driver_v2.authorization(), 'Page dose not welcome customer'
        assert 'SMS' == driver_v2.check_sms_button(), 'Button is not presence or clickable'
        assert 'CREATE CAMPAIGN' == driver_v2.check_create_campaning_button(), 'Button is not presence or clickable'

    @allure.step('Check "SMS" button.')
    @allure.severity('NORMAL')
    def test_check_sms_button(self, driver_v2):
        driver_v2.authorization()
        assert 'SMS' == driver_v2.check_sms_button(), 'Button is not presence or clickable'

    @allure.step('Check "CREATE CAMPAIGN" button.')
    @allure.severity('NORMAL')
    def test_check_campaning_button(self, driver_v2):
        driver_v2.authorization()
        driver_v2.check_sms_button()
        assert 'CREATE CAMPAIGN' == driver_v2.check_create_campaning_button(), 'Button is not presence or clickable'
