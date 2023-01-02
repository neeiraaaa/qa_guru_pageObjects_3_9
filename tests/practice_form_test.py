from demoqa_tests.model.pages import practice_form


def test_submit_student_registration_form():
    practice_form.given_opened()

    practice_form.set_name('Irina')
    practice_form.set_last_name('Rogova')
    practice_form.set_email('neeiraaaa@gmail.com')
    practice_form.set_gender('Female')
    practice_form.set_phone_number('7925399999')
    practice_form.set_birthday('10', '1997', '25')
    practice_form.set_subjects('English')
    practice_form.set_hobbies('Music')
    practice_form.picture_upload('resources/img1.png')
    practice_form.set_address('Москва')
    practice_form.set_state('Haryana')
    practice_form.set_city('Karnal')

    practice_form.submit_final_button()

    practice_form.should_have_submitted(
        [
            ('Student Name', 'Irina Rogova'),
            ('Student Email', 'neeiraaaa@gmail.com'),
            ('Gender', 'Female'),
            ('Mobile', '7925399999'),
            ('Date of Birth', '25 November,1997'),
            ('Subjects', 'English'),
            ('Hobbies', 'Music'),
            ('Picture', 'img1.png'),
            ('Address', 'Москва'),
            ('State', 'Haryana Karnal'),
        ],
    )
