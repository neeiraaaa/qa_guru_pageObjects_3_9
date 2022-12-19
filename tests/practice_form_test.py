from selene.support.shared import browser
from selene import have
import os

def test_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Irina')
    browser.element('#lastName').type('Rogova')
    browser.element('#userEmail').type('neeiraaaa@gmail.com')
    browser.element('#gender-radio-2').double_click()
    browser.element('#userNumber').type('79253999999')
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__month-select"]').click()
    browser.element('[value="9"]').click()
    browser.element('[class="react-datepicker__year-select"]').click()
    browser.element('[value="1997"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--025 react-datepicker__day--weekend"]').click()
    browser.element('#subjectsInput').set_value('eng').press_enter()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').set_value(
        os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'tests/img.png')))
    browser.element('#currentAddress').type('Москва')
    browser.element('#state').click()
    browser.element('#react-select-3-input').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').press_enter()
    browser.element('#submit').with_(click_by_js=True).click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive td:nth-child(2)').should(have.texts(
        'Irina Rogova',
        'neeiraaaa@gmail.com',
        'Female',
        '7925399999',
        '25 October,1997',
        'English',
        'Music',
        'img.png',
        'Москва',
        'Haryana Karnal'))