from threading import Thread
from functools import partial

from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.button import MDRoundFlatIconButton
from generic_form_screen import GenericFormScreen
from submission_functions import database_register
from generic_kvs import standard_checkbox, standard_button
from image_file_picker import ImageFilePicker


class RegisterScreenBase(GenericFormScreen):

    def __init__(self, **kwargs):
        super(RegisterScreenBase, self).__init__(**kwargs)

        self.previous = "registered"

        self.filePicker = ImageFilePicker()
        self.contentBox.add_widget(self.filePicker.pictureButton)

        self.emailTextField = self.create_email_field()
        self.contentBox.add_widget(self.emailTextField)

        self.passwordTextField = self.create_password_field()
        self.contentBox.add_widget(self.passwordTextField)

        self.confirmPasswordTextField = self.create_confirm_password_field()
        self.contentBox.add_widget(self.confirmPasswordTextField)

        self.nameTextField = self.create_name_field()
        self.contentBox.add_widget(self.nameTextField)

        self.weightTextField = self.create_weight_field()
        self.contentBox.add_widget(self.weightTextField)

        self.heightTextField = self.create_height_field()
        self.contentBox.add_widget(self.heightTextField)

        self.dobTextField = self.create_date_field()
        self.contentBox.add_widget(self.dobTextField)

        self.maleGenderRadioButton = Builder.load_string(standard_checkbox)  # type: MDCheckbox
        self.maleGenderRadioButton.group = 'gender'
        self.maleGenderRadioButton.radio_icon_normal = 'gender-male'
        self.femaleGenderRadioButton = Builder.load_string(standard_checkbox)
        self.femaleGenderRadioButton.group = 'gender'
        self.femaleGenderRadioButton.radio_icon_normal = 'gender-female'

        self.genderLabel = MDLabel(text="")

        self.genderRadioButtonBox = MDBoxLayout(pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.genderRadioButtonBox.orientation = 'horizontal'
        self.genderRadioButtonBox.adaptive_height = False
        self.genderRadioButtonBox.add_widget(self.maleGenderRadioButton)
        self.genderRadioButtonBox.add_widget(self.femaleGenderRadioButton)
        self.genderRadioButtonBox.add_widget(self.genderLabel)

        self.contentBox.add_widget(self.genderRadioButtonBox)

        self.submitButton = Builder.load_string(standard_button)  # type: MDFlatButton
        self.submitButton.text = "Register"
        self.submitButton.bind(on_press=partial(self.verify_and_submit_values))

        self.backButton = Builder.load_string(standard_button)  # type: MDFlatButton
        self.backButton.text = "Back"
        self.backButton.bind(on_press=partial(self.goto_previous_screen))

        self.buttonBox = MDBoxLayout(pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.buttonBox.orientation = 'horizontal'
        self.buttonBox.adaptive_height = False
        self.buttonBox.add_widget(self.backButton)
        self.buttonBox.add_widget(self.submitButton)

        self.contentBox.add_widget(self.buttonBox)

    def verify_inputs(self):
        found_error = [False]

        self.verify_date(self.dobTextField, found_error)

        self.verify_password(self.passwordTextField, found_error)

        self.verify_confirmed_password(self.passwordTextField, self.confirmPasswordTextField, found_error)

        self.verify_name(self.nameTextField, found_error)

        self.verify_height(self.heightTextField, found_error)

        self.verify_weight(self.weightTextField, found_error)

        self.verify_email(self.emailTextField, found_error)

        if self.maleGenderRadioButton.state == "normal" and self.femaleGenderRadioButton.state == "normal":
            self.genderLabel.text = "You must select a gender"
            found_error[0] = True
        else:
            self.genderLabel.text = ""

        return not found_error[0]

    def get_form_values(self):
        gender = "Female"
        if self.maleGenderRadioButton.state == "down":
            gender = "Male"
        formDict = {
            "Picture": self.filePicker.filePath,
            "Email": self.emailTextField.text,
            "Password": self.passwordTextField.text,
            "Name": self.nameTextField.text,
            "Weight": self.weightTextField.text,
            "Height": self.heightTextField.text,
            "DoB": self.dobTextField.text,
            "Gender": gender
        }

        return formDict

    def submit_form(self, values):
        thread = Thread(target=database_register, args=(self, values,))
        thread.start()


