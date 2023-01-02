from selene import command, have
from selene.support.shared import browser

from demoqa_tests.model import controls
from demoqa_tests.model.controls import radiobutton, datepicker, checkbox, dropdown,  modal
from demoqa_tests.utils import path


def given_opened():
    browser.open("/automation-practice-form")


def set_name(value):
    browser.element('#firstName').type(value)


def set_last_name(value):
    browser.element('#lastName').type(value)


def set_email(value):
    browser.element('#userEmail').type(value)


def set_gender(gender):
    radiobutton.set_value(browser.all('#gender-radio-2'), gender) #у нее другой селектор и был просто клик


def set_phone_number(value):
    browser.element('#userNumber').type(value)


def set_birthday(month, year, day):
    datepicker.set_birthday_date(month, year, day)


def set_hobbies(hobby):
    browser.element('[for="hobbies-checkbox-3"]').perform(command.js.scroll_into_view)
    checkbox.checkboxes_click(browser.all('[for="hobbies-checkbox-3"]'), hobby)


def set_subjects(subject):
    browser.element('#subjectsInput').type(subject).press_enter()


def set_state(value):
    dropdown.select(browser.element('#state'), value) #у меня немного по другому


def set_city(value):
    dropdown.select(browser.element('#city'), value) #у меня немного по другому


def picture_upload(path_to_pic):
    path.create_path('#uploadPicture', path_to_pic)


def set_address(value):
    browser.element('#currentAddress').type(value)


def submit_final_button():
    browser.element('#submit').with_(click_by_js=True).click()


def should_have_submitted(data):
    rows = controls.modal.dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))