from playwright.sync_api import Page

from base.page_factory.button import Button
from base.page_factory.input import Input


class PracticeFormPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Форма"""
        self.first_name = Input(page, locator='//*[@id="firstName"]', name='Имя')
        self.last_name = Input(page, locator='//*[@id="lastName"]', name='Фамилия')
        self.email = Input(page, locator='//*[@id="userEmail"]', name='Email')
        self.gender = Button(page, locator='//*[@for="gender-radio-1"]', name='Радио кнопка: Gender -> Male')
        self.number = Input(page, locator='//*[@id="userNumber"]', name='Мобильный номер')
        self.calendar_input = Input(page, locator='//*[@id="dateOfBirthInput"]', name='Проверка функционала календаря')
        self.select_month = page.locator('//*[@class="react-datepicker__month-select"]')
        self.select_year = page.locator('//*[@class="react-datepicker__year-select"]')
        self.select_day_11 = page.locator('//*[@class="react-datepicker__day react-datepicker__day--011"]')
        self.subject = Input(page, locator='//*[@id="subjectsInput"]', name='Предмет')
        self.english = Button(page, locator='//*[@id="react-select-2-option-0"]', name='English')
        self.checkbox_1 = Button(page, locator='//*[@for="hobbies-checkbox-1"]', name='Чекбокс - Sports')
        self.checkbox_2 = Button(page, locator='//*[@for="hobbies-checkbox-2"]', name='Чекбокс - Reading')
        self.checkbox_3 = Button(page, locator='//*[@for="hobbies-checkbox-3"]', name='Чекбокс - Music')
        self.document = Button(page, locator='//*[@for="uploadPicture"]', name='Кнопка загрузки файла')
        self.adress = Input(page, locator='//*[@id="currentAddress"]', name='Current Address')
        self.state_inp = Button(page, locator='//*[@id="state"]', name='Select state - выпадающий список')
        self.haryana = Button(page, locator='//*[@id="react-select-3-option-2"]', name='Haryana - выбор из выпадающего списка')
        self.city_inp = Button(page, locator='//*[@id="city"]', name='Select city - выпадающий список')
        self.panipat = Button(page, locator='//*[@id="react-select-4-option-1"]', name='Panipat - выбор из выпадающего списка')
        self.submit = Button(page, locator='//*[@id="submit"]', name='Submit')
        self.close = Button(page, locator='//*[@id="closeLargeModal"]', name='Close')

        """Ожидания"""
        self.Wait_first_name = '//*[@id="firstName"]'
        self.Wait_last_name = '//*[@id="lastName"]'
        self.Wait_number = '//*[@id="userNumber"]'
        self.Wait_calendar = '//*[@id="dateOfBirthInput"]'
        self.Wait_haryana = '//*[@id="react-select-3-option-0"]'
