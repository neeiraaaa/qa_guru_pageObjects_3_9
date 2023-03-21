import allure
from allure_commons.types import Severity

from demoqa_tests.data.user_data import irina_rogova
from demoqa_tests.model.pages.practice_form import Form

@allure.label('owner', 'Irina Rogova')
@allure.severity(Severity.NORMAL)
@allure.tag('web')
@allure.feature('Successful submitting form')
def test_submitting_form():

    form = Form()
    form.submit_form(irina_rogova)
    form.validate_form(irina_rogova)