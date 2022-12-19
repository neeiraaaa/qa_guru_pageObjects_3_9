import os

from selene import command, have
from selene.support.shared import browser


def add_name():
    browser.element('#firstName').type('Irina')
    browser.element('#lastName').type('Rogova')


def add_email():
    browser.element('#userEmail').type('neeiraaaa@gmail.com')


def add_gender():
    browser.element('#gender-radio-2').double_click()


def date_of_birth():
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__month-select"]').click()
    browser.element('[value="9"]').click()
    browser.element('[class="react-datepicker__year-select"]').click()
    browser.element('[value="1997"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--025 react-datepicker__day--weekend"]').click()


def add_hobbies():
    browser.element('[for="hobbies-checkbox-3"]').perform(command.js.scroll_into_view)
    browser.element('[for="hobbies-checkbox-3"]').click()


def add_subjects():
    browser.element('#subjectsInput').set_value('eng').press_enter()


def add_state_and_city():
    browser.element('#state').click()
    browser.element('#react-select-3-input').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').press_enter()


def element_type(selector, data):
    browser.element(selector).type(data)


def upload_file():
    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'tests/img.jpg')))


def submit_final_button():
    browser.element('#submit').with_(click_by_js=True).click()


def data_validation():
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Irina Rogova',
        'neeiraaaa@gmail.com',
        'Female',
        '7925399999',
        '25 October,1997',
        'English',
        'Music',
        'img.jpg',
        'Москва',
        'Haryana Karnal'))