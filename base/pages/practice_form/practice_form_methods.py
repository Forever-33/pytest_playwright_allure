import time

import allure

from base.pages.practice_form.practice_form_page import PracticeFormPage
from src.config.expectations import Wait

class PracticeFormMethods:

    @staticmethod
    def fill_name_input(practice_form: PracticeFormPage):
        errors = []
        Wait.set_page(practice_form.page)
        try:
            with allure.step("Ввод имени и фамилии"):
                practice_form.first_name.fill("хочу")
                practice_form.last_name.fill("спать")
                practice_form.gender.click()
                practice_form.email.fill("hochyspat@gmail.com")
                practice_form.number.fill("79993338877")
                practice_form.calendar_input.click()
                practice_form.select_month.select_option("3")
                practice_form.select_year.select_option("2005")
                practice_form.select_day_11.click()
                Wait.visible(practice_form.Wait_calendar)
                practice_form.subject.fill("English")
                practice_form.english.click()
                practice_form.checkbox_1.click()
                practice_form.checkbox_2.click()
                practice_form.checkbox_3.click()
                practice_form.document.click()
                practice_form.adress.fill("Адрес")
                practice_form.state_inp.click()
                practice_form.haryana.click()
                practice_form.city_inp.click()
                practice_form.panipat.click()
                practice_form.submit.click()
                practice_form.close.click()

                time.sleep(2)


        except AssertionError as e:
            errors.append(str(e))