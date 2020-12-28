from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from register_screen import RegisterScreenBase
from login_screen import LoginScreenBase

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


class RegisteredScreen(MDScreen):
    pass


class RegisterScreen(RegisterScreenBase):
    pass


class LoginScreen(LoginScreenBase):
    pass


class MedX(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = 'Dark'
        screen = Builder.load_string(screen_helper)
        return screen


App = MedX()
App.run()
