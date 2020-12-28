from database import Database
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from threading import Thread

database = Database()


def database_register(caller, form_dict):
    email_verification = database.create_an_account(
        form_dict["Email"],
        form_dict["Password"]
    )  # This is to verify that the entered email isn't an existing email in the forms.

    if (email_verification == "Email already exists"):
        show_dialog(email_verification)
        caller.emailTextField.error = True
        caller.emailTextField.focus = True
        caller.emailTextField.error = False
        caller.spinner.active = False
        return
    picture_path = form_dict.pop("Picture")
    name_on_database = str(database.primaryKeyCreator(form_dict["Email"].encode('utf-8'))) + picture_path[-4:]  # This makes the file name of the media on the database with the PK specified with the user and after "+" is to get the picture extention.
    database.upload_media(picture_path, name_on_database)
    show_dialog(database.insertData(form_dict, "CustomersData"))
    caller.spinner.active = False


def show_dialog(output):
    dialog = MDDialog(
        text=output,
    )
    dialog.open()


def database_login(caller, login_dict):
    output = database.login(login_dict["Email"], login_dict["Password"])
    show_dialog(output)
    caller.spinner.active = False
    if output != "Successfully logged in":
        caller.emailTextField.error = True
        caller.emailTextField.focus = True
        caller.emailTextField.focus = False

        caller.passwordTextField.error = True
        caller.passwordTextField.focus = True
        caller.passwordTextField.focus = False
