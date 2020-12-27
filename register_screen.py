from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

from generic_form_screen import GenericFormScreen
from submission_functions import back, register
from generic_kvs import standard_textfield, standard_checkbox, standard_button
from textfield_filters import name_filter, dob_filter, datePattern, emailPattern


class RegisterScreenBase(GenericFormScreen):

    def __init__(self, **kwargs):
        super(RegisterScreenBase, self).__init__(**kwargs)

        self.emailTextField = Builder.load_string(standard_textfield)  # type: MDTextField
        self.emailTextField.hint_text = "Email"
        self.emailTextField.helper_text = "Incorrect email"
        self.emailTextField.max_text_length = 100
        self.emailTextField.icon_right = "email"
        self.contentBox.add_widget(self.emailTextField)

        self.passwordTextField = Builder.load_string(standard_textfield)  # type: MDTextField
        self.passwordTextField.hint_text = "Password"
        self.passwordTextField.helper_text = "Alphanumeric and special characters only. Between 10 and 50 characters."
        self.passwordTextField.max_text_length = 50
        self.passwordTextField.password = True
        self.passwordTextField.icon_right = "onepassword"
        self.contentBox.add_widget(self.passwordTextField)

        self.confirmPasswordTextField = Builder.load_string(standard_textfield)  # type: MDTextField
        self.confirmPasswordTextField.hint_text = "Confirm Password"
        self.confirmPasswordTextField.helper_text = "Repeat the password above"
        self.confirmPasswordTextField.max_text_length = 50
        self.confirmPasswordTextField.password = True
        self.confirmPasswordTextField.icon_right = "onepassword"
        self.contentBox.add_widget(self.confirmPasswordTextField)

        self.nameTextField = Builder.load_string(standard_textfield)  # type: MDTextField
        self.nameTextField.hint_text = "Name"
        self.nameTextField.helper_text = "Alphabet characters only. Minimum 2 characters."
        self.nameTextField.max_text_length = 100
        self.nameTextField.icon_right = "human"
        self.nameTextField.input_filter = name_filter
        self.contentBox.add_widget(self.nameTextField)

        self.weightTextField = Builder.load_string(standard_textfield)  # type: MDTextField
        self.weightTextField.hint_text = "Weight (KG)"
        self.weightTextField.helper_text = "Numbers only"
        self.weightTextField.max_text_length = 3
        self.weightTextField.icon_right = "scale"
        self.weightTextField.input_filter = 'int'
        self.contentBox.add_widget(self.weightTextField)

        self.heightTextField = Builder.load_string(standard_textfield)  # type: MDTextField
        self.heightTextField.hint_text = "Height (cm)"
        self.heightTextField.helper_text = "Numbers only. Minimum is 40. Max is 251."
        self.heightTextField.max_text_length = 3
        self.heightTextField.icon_right = "ruler"
        self.heightTextField.input_filter = 'int'
        self.contentBox.add_widget(self.heightTextField)

        self.dobTextField = Builder.load_string(standard_textfield)  # type: MDTextField
        self.dobTextField.hint_text = "Date of birth (DD/MM/YYYY)"
        self.dobTextField.helper_text = "DD/MM/YYYY Format"
        self.dobTextField.max_text_length = 10
        self.dobTextField.icon_right = "calendar"
        self.dobTextField.input_filter = dob_filter
        self.contentBox.add_widget(self.dobTextField)

        self.genderMale = Builder.load_string(standard_checkbox)  # type: MDCheckbox
        self.genderMale.group = 'gender'
        self.genderMale.radio_icon_normal = 'gender-male'
        self.genderFemale = Builder.load_string(standard_checkbox)
        self.genderFemale.group = 'gender'
        self.genderFemale.radio_icon_normal = 'gender-female'

        self.genderLabel = MDLabel(text="")

        self.genderBox = MDBoxLayout(pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.genderBox.orientation = 'horizontal'
        self.genderBox.adaptive_height = False
        self.genderBox.add_widget(self.genderMale)
        self.genderBox.add_widget(self.genderFemale)
        self.genderBox.add_widget(self.genderLabel)

        self.contentBox.add_widget(self.genderBox)

        self.submit = Builder.load_string(standard_button)  # type: MDFlatButton
        self.submit.text = "Register"
        self.submit.bind(on_press=register)

        self.back = Builder.load_string(standard_button)  # type: MDFlatButton
        self.back.text = "Back"
        self.back.bind(on_press=back)

        self.buttonBox = MDBoxLayout(pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.buttonBox.orientation = 'horizontal'
        self.buttonBox.adaptive_height = False
        self.buttonBox.add_widget(self.back)
        self.buttonBox.add_widget(self.submit)

        self.contentBox.add_widget(self.buttonBox)

    def verify_inputs(self):
        found_error = False
        if datePattern.search(self.dobTextField.text):
            self.dobTextField.error = False
        else:
            self.dobTextField.error = True
            found_error = True
        self.dobTextField.focus = True  # Date verified
        self.dobTextField.focus = False

        if len(self.passwordTextField.text) < 10:
            self.passwordTextField.error = True
            found_error = True
        else:
            self.passwordTextField.error = False
        self.passwordTextField.focus = True  # password at minimum length
        self.passwordTextField.focus = False

        if self.passwordTextField.text != self.confirmPasswordTextField:
            self.confirmPasswordTextField.error = True
            found_error = True
        else:
            self.confirmPasswordTextField.error = False
        self.confirmPasswordTextField.focus = True  # password at minimum length
        self.confirmPasswordTextField.focus = False

        if len(self.nameTextField.text) < 2:
            self.nameTextField.error = True
            found_error = True
        else:
            self.nameTextField.error = False
        self.nameTextField.focus = True  # name at minimum length
        self.nameTextField.focus = False

        if self.heightTextField.text != "" and (
                int(self.heightTextField.text) < 40 or int(self.heightTextField.text) > 251):
            self.heightTextField.error = True
            found_error = True
        else:
            self.heightTextField.error = False
        self.heightTextField.focus = True  # height not empty and bigger than 40
        self.heightTextField.focus = False

        if self.weightTextField.text == "":
            self.weightTextField.error = True
            found_error = True
        else:
            self.weightTextField.error = False
        self.weightTextField.focus = True  # weight not empty
        self.weightTextField.focus = False

        if emailPattern.search(self.emailTextField.text):
            self.emailTextField.error = False
        else:
            self.emailTextField.error = True
            found_error = True
        self.emailTextField.focus = True  # email verified
        self.emailTextField.focus = False

        if self.genderMale.state == "normal" and self.genderFemale.state == "normal":
            self.genderLabel.text = "You must select a gender"
            found_error = True
        else:
            self.genderLabel.text = ""

        return not found_error

    def get_form_values(self):
        gender = "Female"
        if self.genderMale.state == "down":
            gender = "Male"
        formDict = {
            "Email": self.emailTextField.text,
            "Password": self.passwordTextField.text,
            "Name": self.nameTextField.text,
            "Weight": self.weightTextField.text,
            "Height": self.heightTextField.text,
            "DoB": self.dobTextField.text,
            "Gender": gender
        }

        return formDict
