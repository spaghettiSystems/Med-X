from kivymd.uix.button import MDRoundFlatIconButton
from kivymd.uix.filemanager import MDFileManager
from generic_kvs import standard_icon_button
from kivy.lang import Builder


class ImageFilePicker:
    def __init__(self, **kwargs):
        super(ImageFilePicker, self).__init__(**kwargs)

        self.path = '/'
        self.filePath = ""
        self.acceptableFiles = (".png", ".jpg", ".jpeg", ".bmp", ".gif")
        self.file_manager = MDFileManager(
            exit_manager=lambda *args: self.file_manager.close(),
            select_path=self.select_path,
            ext=self.acceptableFiles,
        )

        self.pictureButton = Builder.load_string(standard_icon_button)  # type: MDRoundFlatIconButton
        self.pictureButton.bind(on_press=lambda instance: self.file_manager.show(self.path))

    def select_path(self, *args):
        if args[0].endswith(self.acceptableFiles):
            self.filePath = args[0]
            self.pictureButton.icon = self.filePath
        else:
            self.path = args[0]
        self.file_manager.close()