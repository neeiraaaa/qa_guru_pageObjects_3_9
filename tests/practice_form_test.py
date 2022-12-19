from selene.support.shared import browser

from tests.encapsulation import element_type, upload_file, add_name, add_email, \
    add_gender, date_of_birth, add_hobbies, add_subjects, data_validation, add_state_and_city, submit_final_button


def test_form():
    browser.open('/automation-practice-form')
    add_name()
    add_email()
    add_gender()
    element_type('#userNumber', '79253999999')
    date_of_birth()
    add_subjects()
    add_hobbies()
    upload_file()
    element_type('#currentAddress', 'Москва')
    add_state_and_city()
    submit_final_button()
    data_validation()