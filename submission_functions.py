def back(instance):
    instance.parent.parent.parent.manager.current = 'registered'


def register(instance):
    screen = instance.parent.parent.parent  # type: RegisterScreen
    form_dict = screen.verify_and_get_values()
    print(form_dict)
        # TODO: DB stuff goes here.


def login(instance):
    screen = instance.parent.parent.parent  # type: LoginScreen
    login_dict = screen.verify_and_get_values()
    print(login_dict)
        # TODO: DB stuff goes here.