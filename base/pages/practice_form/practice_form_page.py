from playwright.sync_api import Page

from base.page_factory.button import Button
from base.page_factory.input import Input


class PracticeFormPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Форма"""
        self.first_name = Input(page, locator='//*[@id="firstName"]', name='имя')
        self.last_name = Input(page, locator='//*[@id="lastName"]', name='фамилия')
        self.email = Input(page, locator='//*[@id="userEmail"]', name='Email')
        self.gender = Button(page, locator='//*[@for="gender-radio-1"]', name='custom-control-label')
        self.number = Input(page, locator='//*[@id="userNumber"]', name='мобильный номер')
        self.calendar = Input(page, locator='//*[@id="dateOfBirthInput"]', name='календарь')
        # self.drop_month = page.locator('//*[starts-with(@class, "react-datepicker__month")]')
        self.subject = Input(page, locator='//*[@id="subjectsInput"]', name='предмет')
        # self.english = Button(page, locator='//*[@for="react-select-2-option-0"]', name='react-select-2-option-0')
        self.checkbox_1 = Button(page, locator='//*[@for="hobbies-checkbox-1"]', name='custom-control-input')
        self.checkbox_2 = Button(page, locator='//*[@for="hobbies-checkbox-2"]', name='custom-control-input')
        self.checkbox_3 = Button(page, locator='//*[@for="hobbies-checkbox-3"]', name='custom-control-input')
        self.document = Button(page, locator='//*[@for="uploadPicture"]', name='doc')
        # self.adress = Input(page, locator='//*[@id="currentAddress"]', name='адрес')
        # self.state_inp = page.locator('//*[starts-with(@class, "css-tlfecz-indicatorContainer")]')
        # self.haryana = Button(page, locator='//*[@id="react-select-3-option-0"]', name='haryana')
        self.submit = Button(page, locator='//*[@id="submit"]', name='submit')

        """Ожидания"""
        self.Wait_first_name = '//*[@id="firstName"]'
        self.Wait_last_name = '//*[@id="lastName"]'
        # self.Wait_drop_month = '(//*[starts-with(@class, "react-datepicker__month")])[2]'
