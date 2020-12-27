from abc import ABCMeta, abstractmethod

from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from generic_kvs import standard_vbox


class GenericFormScreen(MDScreen):
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