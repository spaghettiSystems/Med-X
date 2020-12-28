from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.button import MDRoundFlatIconButton
from generic_form_screen import GenericFormScreen
from submission_functions import back, register
from generic_kvs import standard_checkbox, standard_button, standard_icon_button


class RegisterScreenBase(GenericFormScreen):

    def __init__(self, **kwargs):
        super(RegisterScreenBase, self).__init__(**kwargs)

        self.path = '/'
        self.filePath = ""
        self.acceptableFiles = (".png", ".jpg", ".jpeg", ".bmp", ".gif")
        self.file_manager = MDFileManager(
            exit_manager=lambda *args: self.file_manager.close(),
            select_path=self.select_path,
            ext=self.acceptableFiles,
        )

        self.pic = Builder.load_string(standard_icon_button)  # type: MDRoundFlatIconButton
        self.pic.bind(on_press=lambda instance: self.file_manager.show(self.path))

        self.contentBox.add_widget(self.pic)

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

        self.verify_date(self.dobTextField, found_error)

        self.verify_password(self.passwordTextField, found_error)

        self.verify_confirmed_password(self.passwordTextField, self.confirmPasswordTextField, found_error)

        self.verify_name(self.nameTextField, found_error)

        self.verify_height(self.heightTextField, found_error)

        self.verify_weight(self.weightTextField, found_error)

        self.verify_email(self.emailTextField, found_error)

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
            "Picture": self.filePath,
            "Email": self.emailTextField.text,
            "Password": self.passwordTextField.text,
            "Name": self.nameTextField.text,
            "Weight": self.weightTextField.text,
            "Height": self.heightTextField.text,
            "DoB": self.dobTextField.text,
            "Gender": gender
        }

        return formDict

    def select_path(self, *args):
        if args[0].endswith(self.acceptableFiles):
            self.filePath = args[0]
            self.pic.icon = self.filePath
        else:
            self.path = args[0]
        self.file_manager.close()
