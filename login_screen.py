from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen

from generic_kvs import standard_vbox, standard_textfield, standard_button
from submission_functions import login, back
from generic_form_screen import GenericFormScreen


class LoginScreenBase(GenericFormScreen):
    def __init__(self, **kwargs):
        super(LoginScreenBase, self).__init__(**kwargs)

        self.emailTextField = self.create_email_field()
        self.contentBox.add_widget(self.emailTextField)

        self.passwordTextField = self.create_password_field()
        self.contentBox.add_widget(self.passwordTextField)

        self.submit = Builder.load_string(standard_button)
        self.submit.text = "Login"
        self.submit.bind(on_press=login)

        self.back = Builder.load_string(standard_button)
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

        self.verify_email(self.emailTextField, found_error)

        self.verify_password(self.passwordTextField, found_error)

        return not found_error

    def get_form_values(self):
        loginDict = {
            "Email": self.emailTextField.text,
            "Password": self.passwordTextField.text
        }

        return loginDict
