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
    helper_text_mode: "on_error"
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

standard_icon_button = """
MDIconButton:
    icon: "human"
    pos_hint: {"center_x": .5, "center_y": .5}
"""
