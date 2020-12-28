from Database import Database

database = Database()


def back(instance):
    instance.parent.parent.parent.manager.current = 'registered'


def register(instance):
    screen = instance.parent.parent.parent  # type: RegisterScreen
    if screen.verify_inputs():
        form_dict = screen.get_form_values()
        email_verification = database.create_an_account(form_dict["Email"], form_dict[
            "Password"])  # This is to verify that the entered email isn't an existing email in the forms.
        if (email_verification == "Email already exists"):
            return "Email already exists"
        picture_path = form_dict.pop("Picture")
        name_on_database = str(database.primaryKeyCreator(form_dict["Email"].encode('utf-8'))) + picture_path[
                                                                                                 -4:]  # This makes the file name of the media on the database with the PK specified with the user and after "+" is to get the picture extention.
        database.upload_media(picture_path, name_on_database)
        output=database.insertData(form_dict,"CustomersData")
        return output

def login(instance):
    screen = instance.parent.parent.parent  # type: LoginScreen
    if screen.verify_inputs():
        login_dict = screen.get_form_values()
        # TODO: DB stuff goes here.
        database.login(login_dict["Email"],login_dict["Password"])
