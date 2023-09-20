from pages.main_page import MainPage
import allure
import time
import pytest


@allure.suite('Test Main Page')
class TestMainPage:
    def test_just_open(self, driver):
        test_elements = MainPage(driver, 'https://my.fortvision.com/#/login')
        test_elements.open()
        assert 1==1
    
    @allure.step('Test Authorization.')
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
        result = main_page.create_SMS()
        assert "Success" == result, 'Something went wrong!!!'
