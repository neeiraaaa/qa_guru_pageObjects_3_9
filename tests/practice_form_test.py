from demoqa_tests.data.user_data import irina_rogova
from demoqa_tests.model.pages.practice_form import Form


def test_submitting_form():

    form = Form()
    form.submit_form(irina_rogova)
    form.validate_form(irina_rogova)