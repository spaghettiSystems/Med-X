from functools import partial
from threading import Thread

from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen

from generic_kvs import standard_vbox, standard_textfield, standard_button
from submission_functions import database_login
from generic_form_screen import GenericFormScreen


class LoginScreenBase(GenericFormScreen):
    def __init__(self, **kwargs):
        super(LoginScreenBase, self).__init__(**kwargs)

        self.previous = "registered"

        self.emailTextField = self.create_email_field()
        self.contentBox.add_widget(self.emailTextField)

        self.passwordTextField = self.create_password_field()
        self.contentBox.add_widget(self.passwordTextField)

        self.submitButton = Builder.load_string(standard_button)
        self.submitButton.text = "Login"
        self.submitButton.bind(on_press=partial(self.verify_and_submit_values))

        self.backButton = Builder.load_string(standard_button)
        self.backButton.text = "Back"
        self.backButton.bind(on_press=partial(self.back_func))

        self.buttonBox = MDBoxLayout(pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.buttonBox.orientation = 'horizontal'
        self.buttonBox.adaptive_height = False
        self.buttonBox.add_widget(self.backButton)
        self.buttonBox.add_widget(self.submitButton)

        self.contentBox.add_widget(self.buttonBox)

    def verify_inputs(self):
        found_error = [False]

        self.verify_email(self.emailTextField, found_error)

        self.verify_password(self.passwordTextField, found_error)

        return not found_error[0]

    def get_form_values(self):
        loginDict = {
            "Email": self.emailTextField.text,
            "Password": self.passwordTextField.text
        }

        return loginDict

    def submit_form(self, values):
        thread = Thread(target=database_login, args=(self, values,))
        thread.start()