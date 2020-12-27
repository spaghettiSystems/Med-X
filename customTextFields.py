import re


datePattern = re.compile('^(0[1-9]|[12][0-9]|3[01])[-/](0[1-9]|1[012])[-/](19|20)\d\d$')
emailPattern = re.compile(
        """(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""")


def name_filter(string, from_undo):
    final_string = ""
    if from_undo:
        return string
    for char in string:
        charcode = ord(char)
        if (65 <= charcode <= 90) or (97 <= charcode <= 122) or charcode == 32:
            final_string = final_string + char
    return final_string


def dob_filter(string, from_undo):
    final_string = ""
    if from_undo:
        return string
    for char in string:
        charcode = ord(char)
        if charcode == 47 or 48 <= charcode <= 57:
            final_string = final_string + char
    return final_string
