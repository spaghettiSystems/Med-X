import re
from abc import ABCMeta, abstractmethod

from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from generic_kvs import standard_vbox

from generic_kvs import standard_textfield


class GenericFormScreen(MDScreen):
    datePattern = re.compile('^(0[1-9]|[12][0-9]|3[01])[-/](0[1-9]|1[012])[-/](19|20)\d\d$')
    emailPattern = re.compile(
        """(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""")

    def __init__(self, **kwargs):
        super(GenericFormScreen, self).__init__(**kwargs)
        self.contentBox = Builder.load_string(standard_vbox)  # type: MDBoxLayout
        self.add_widget(self.contentBox)

    @abstractmethod
    def verify_inputs(self):
        pass

    @abstractmethod
    def get_form_values(self):
        pass

    def verify_and_get_values(self):
        if self.verify_inputs():
            return self.get_form_values()

    @staticmethod
    def name_filter(string, from_undo):
        final_string = ""
        if from_undo:
            return string
        for char in string:
            charcode = ord(char)
            if (65 <= charcode <= 90) or (97 <= charcode <= 122) or charcode == 32:
                final_string = final_string + char
        return final_string

    @staticmethod
    def dob_filter(string, from_undo):
        final_string = ""
        if from_undo:
            return string
        for char in string:
            charcode = ord(char)
            if charcode == 47 or 48 <= charcode <= 57:
                final_string = final_string + char
        return final_string

    @staticmethod
    def verify_date(date_text_field, found_error):
        if GenericFormScreen.datePattern.search(date_text_field.text):
            date_text_field.error = False
        else:
            date_text_field.error = True
            found_error = True
        date_text_field.focus = True  # Date verified
        date_text_field.focus = False

    @staticmethod
    def verify_email(email_text_field, found_error):
        if GenericFormScreen.emailPattern.search(email_text_field.text):
            email_text_field.error = False
        else:
            email_text_field.error = True
            found_error = True
        email_text_field.focus = True  # email verified
        email_text_field.focus = False

    @staticmethod
    def verify_weight(weight_text_field, found_error):
        if weight_text_field.text == "":
            weight_text_field.error = True
            found_error = True
        else:
            weight_text_field.error = False
        weight_text_field.focus = True  # weight not empty
        weight_text_field.focus = False

    @staticmethod
    def verify_height(height_text_field, found_error):
        if height_text_field.text != "" and (
                int(height_text_field.text) < 40 or int(height_text_field.text) > 251):
            height_text_field.error = True
            found_error = True
        else:
            height_text_field.error = False
        height_text_field.focus = True  # height not empty and bigger than 40
        height_text_field.focus = False

    @staticmethod
    def verify_name(name_text_field, found_error):
        if len(name_text_field.text) < 2:
            name_text_field.error = True
            found_error = True
        else:
            name_text_field.error = False
        name_text_field.focus = True  # name at minimum length
        name_text_field.focus = False

    @staticmethod
    def verify_confirmed_password(password_field, verified_password_field, found_error):
        if password_field.text != verified_password_field.text:
            verified_password_field.error = True
            found_error = True
        else:
            verified_password_field.error = False
        verified_password_field.focus = True  # password at minimum length
        verified_password_field.focus = False

    @staticmethod
    def verify_password(password_field, found_error):
        if len(password_field.text) < 10:
            password_field.error = True
            found_error = True
        else:
            password_field.error = False
        password_field.focus = True  # password at minimum length
        password_field.focus = False

    @staticmethod
    def create_date_field():
        date_text_field = Builder.load_string(standard_textfield)  # type: MDTextField
        date_text_field.hint_text = "Date of birth (DD/MM/YYYY)"
        date_text_field.helper_text = "DD/MM/YYYY Format"
        date_text_field.max_text_length = 10
        date_text_field.icon_right = "calendar"
        date_text_field.input_filter = GenericFormScreen.dob_filter
        return date_text_field

    @staticmethod
    def create_height_field():
        height_text_field = Builder.load_string(standard_textfield)  # type: MDTextField
        height_text_field.hint_text = "Height (cm)"
        height_text_field.helper_text = "Numbers only. Minimum is 40. Max is 251."
        height_text_field.max_text_length = 3
        height_text_field.icon_right = "ruler"
        height_text_field.input_filter = 'int'
        return height_text_field

    @staticmethod
    def create_weight_field():
        weight_text_Field = Builder.load_string(standard_textfield)  # type: MDTextField
        weight_text_Field.hint_text = "Weight (KG)"
        weight_text_Field.helper_text = "Numbers only"
        weight_text_Field.max_text_length = 3
        weight_text_Field.icon_right = "scale"
        weight_text_Field.input_filter = 'int'
        return weight_text_Field

    @staticmethod
    def create_name_field():
        name_text_field = Builder.load_string(standard_textfield)  # type: MDTextField
        name_text_field.hint_text = "Name"
        name_text_field.helper_text = "Alphabet characters only. Minimum 2 characters."
        name_text_field.max_text_length = 100
        name_text_field.icon_right = "human"
        name_text_field.input_filter = GenericFormScreen.name_filter
        return name_text_field

    @staticmethod
    def create_confirm_password_field():
        confirm_password_text_field = Builder.load_string(standard_textfield)  # type: MDTextField
        confirm_password_text_field.hint_text = "Confirm Password"
        confirm_password_text_field.helper_text = "Repeat the password above"
        confirm_password_text_field.max_text_length = 50
        confirm_password_text_field.password = True
        confirm_password_text_field.icon_right = "onepassword"
        return confirm_password_text_field

    @staticmethod
    def create_password_field():
        password_text_field = Builder.load_string(standard_textfield)  # type: MDTextField
        password_text_field.hint_text = "Password"
        password_text_field.helper_text = "Alphanumeric and special characters only. Between 10 and 50 characters."
        password_text_field.max_text_length = 50
        password_text_field.password = True
        password_text_field.icon_right = "onepassword"
        return password_text_field

    @staticmethod
    def create_email_field():
        email_text_field = Builder.load_string(standard_textfield)  # type: MDTextField
        email_text_field.hint_text = "Email"
        email_text_field.helper_text = "Incorrect email"
        email_text_field.max_text_length = 100
        email_text_field.icon_right = "email"
        return email_text_field
