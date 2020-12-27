def back(instance):
    instance.parent.parent.parent.manager.current = 'registered'


def register(instance):
    screen = instance.parent.parent.parent  # type: RegisterScreen
    if screen.verify_inputs():
        form_dict = screen.get_form_values()
        print(form_dict)
        # TODO: DB stuff goes here.


def login(instance):
    screen = instance.parent.parent.parent  # type: LoginScreen
    if screen.verify_inputs():
        login_dict = screen.get_form_values()
        # TODO: DB stuff goes here.