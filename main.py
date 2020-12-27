from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import MDScreen
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.selectioncontrol import MDCheckbox
from customTextFields import *
import re

screen_helper = """
ScreenManager:
    RegisteredScreen:
    LoginScreen:
    RegisterScreen:
    
<RegisteredScreen>:
    name: 'registered'
    MDBoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 5
        pos_hint: {'center_y' : 1}
        MDRectangleFlatButton:
            text: 'Login'
            on_press: root.manager.current = 'login'
            pos_hint: {'center_x' : .5}
        MDRectangleFlatButton:
            text: 'Register'
            on_press: root.manager.current = 'register'
            pos_hint: {'center_x' : .5}
        
<RegisterScreen>:
    name: 'register'
    
<LoginScreen>:
    name: 'login'

        
"""

standard_vbox = """    
MDBoxLayout:
    orientation: 'vertical'
    padding: 40
    spacing: 5
    pos_hint: {'center_y' : .5}
"""

standard_textfield = """
MDTextField:
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    required: True
"""

standard_checkbox = """
MDCheckbox:
    size_hint: None, None
    size: dp(48), dp(48)
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    required: True

"""

standard_button = """
MDRectangleFlatButton:
    pos_hint: {'center_y' : .5}
"""


class RegisteredScreen(MDScreen):
    pass


def back(instance):
    instance.parent.parent.parent.manager.current = 'registered'


def register(instance):
    screen = instance.parent.parent.parent  # type: RegisterScreen
    if screen.verify_registration_inputs():
        form_dict = screen.get_form_values()
        # TODO: DB stuff goes here.


def login(instance):
    screen = instance.parent.parent.parent  # type: LoginScreen
    if screen.verify_registration_inputs():
        login_dict = screen.get_form_values()
        # TODO: DB stuff goes here.


class RegisterScreen(MDScreen):

    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)

        self.contentBox = Builder.load_string(standard_vbox)  # type: MDBoxLayout
        self.add_widget(self.contentBox)

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

        self.nameTextField = Builder.load_string(standard_textfield)  # type: MDTextField
        self.nameTextField.hint_text = "Name"
        self.nameTextField.helper_text = "Alphabet characters only. Minimum 2 characters."
        self.nameTextField.helper_text_mode = "on_error"
        self.nameTextField.max_text_length = 100
        self.nameTextField.icon_right = "human"
        self.nameTextField.input_filter = name_filter
        self.contentBox.add_widget(self.nameTextField)

        self.weightTextField = Builder.load_string(standard_textfield)  # type: MDTextField
        self.weightTextField.hint_text = "Weight (KG)"
        self.weightTextField.helper_text = "Numbers only"
        self.weightTextField.helper_text_mode = "on_error"
        self.weightTextField.max_text_length = 3
        self.weightTextField.icon_right = "scale"
        self.weightTextField.input_filter = 'int'
        self.contentBox.add_widget(self.weightTextField)

        self.heightTextField = Builder.load_string(standard_textfield)  # type: MDTextField
        self.heightTextField.hint_text = "Height (cm)"
        self.heightTextField.helper_text = "Numbers only. Minimum is 40. Max is 251."
        self.heightTextField.helper_text_mode = "on_error"
        self.heightTextField.max_text_length = 3
        self.heightTextField.icon_right = "ruler"
        self.heightTextField.input_filter = 'int'
        self.contentBox.add_widget(self.heightTextField)

        self.dobTextField = Builder.load_string(standard_textfield)  # type: MDTextField
        self.dobTextField.hint_text = "Date of birth (DD/MM/YYYY)"
        self.dobTextField.helper_text = "DD/MM/YYYY Format"
        self.dobTextField.helper_text_mode = "on_error"
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

    def verify_registration_inputs(self):
        found_error = False
        if datePattern.search(self.dobTextField.text):
            self.dobTextField.error = False
        else:
            self.dobTextField.error = True
            found_error = True
        self.dobTextField.focus = True  # Date verified

        if emailPattern.search(self.emailTextField.text):
            self.emailTextField.error = False
        else:
            self.emailTextField.error = True
            found_error = True
        self.emailTextField.focus = True  # email verified

        if len(self.passwordTextField.text) < 10:
            self.passwordTextField.error = True
            found_error = True
        else:
            self.passwordTextField.error = False
        self.passwordTextField.focus = True  # password at minimum length

        if len(self.nameTextField.text) < 2:
            self.nameTextField.error = True
            found_error = True
        else:
            self.nameTextField.error = False
        self.nameTextField.focus = True  # name at minimum length

        if self.heightTextField.text != "" and (int(self.heightTextField.text) < 40 or int(self.heightTextField.text) > 251):
            self.heightTextField.error = True
            found_error = True
        else:
            self.heightTextField.error = False
        self.heightTextField.focus = True  # height not empty and bigger than 40

        if self.weightTextField.text == "":
            self.weightTextField.error = True
            found_error = True
        else:
            self.weightTextField.error = False
        self.weightTextField.focus = True  # weight not empty

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

        print(formDict)
        return formDict


class LoginScreen(MDScreen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        self.contentBox = Builder.load_string(standard_vbox)
        self.add_widget(self.contentBox)

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
    def verify_registration_inputs(self):
        found_error = False

        if emailPattern.search(self.emailTextField.text):
            self.emailTextField.error = False
        else:
            self.emailTextField.error = True
            found_error = True
        self.emailTextField.focus = True  # email verified

        if len(self.passwordTextField.text) < 10:
            self.passwordTextField.error = True
            found_error = True
        else:
            self.passwordTextField.error = False
        self.passwordTextField.focus = True  # password at minimum length

        return not found_error

    def get_form_values(self):
        loginDict = {
            "Email": self.emailTextField.text,
            "Password": self.passwordTextField.text
        }

        print(loginDict)
        return loginDict


class MedX(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = 'Dark'
        screen = Builder.load_string(screen_helper)
        return screen


App = MedX()
App.run()
