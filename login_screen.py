from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen

from generic_kvs import standard_vbox, standard_textfield, standard_button
from submission_functions import login, back
from textfield_filters import emailPattern
from generic_form_screen import GenericFormScreen


class LoginScreenBase(GenericFormScreen):
    def __init__(self, **kwargs):
        super(LoginScreenBase, self).__init__(**kwargs)

        self.emailTextField = Builder.load_string(standard_textfield)  # type: MDTextField
        self.emailTextField.hint_text = "Email"
        self.emailTextField.helper_text = "Incorrect email"
        self.emailTextField.helper_text_mode = "on_error"
        self.emailTextField.max_text_length = 100
        self.emailTextField.icon_right = "email"
        self.contentBox.add_widget(self.emailTextField)

        self.passwordTextField = Builder.load_string(standard_textfield)  # type: MDTextField
        self.passwordTextField.hint_text = "Password"
        self.passwordTextField.helper_text = "Alphanumeric and special characters only. Between 10 and 50 characters."
        self.passwordTextField.helper_text_mode = "on_error"
        self.passwordTextField.max_text_length = 50
        self.passwordTextField.password = True
        self.passwordTextField.icon_right = "onepassword"
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

        if emailPattern.search(self.emailTextField.text):
            self.emailTextField.error = False
        else:
            self.emailTextField.error = True
            found_error = True
        self.emailTextField.focus = True  # email verified
        self.emailTextField.focus = False

        if len(self.passwordTextField.text) < 10:
            self.passwordTextField.error = True
            found_error = True
        else:
            self.passwordTextField.error = False
        self.passwordTextField.focus = True  # password at minimum length
        self.passwordTextField.focus = False

        return not found_error

    def get_form_values(self):
        loginDict = {
            "Email": self.emailTextField.text,
            "Password": self.passwordTextField.text
        }

        return loginDict