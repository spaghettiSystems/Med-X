import pyrebase

import hashlib

import math


class Database:

    def __init__(self):

        self.firebaseConfig = {
            'apiKey': "AIzaSyBXAtKvoq5GkGBf1eT7OG5kodAOu4i_Y6c",
            'authDomain': "med-x-d762d.firebaseapp.com",
            'databaseURL': "https://med-x-d762d-default-rtdb.europe-west1.firebasedatabase.app/",
            'projectId': "med-x-d762d",
            'storageBucket': "med-x-d762d.appspot.com",
            'messagingSenderId': "539850808518",
            'appId': "1:539850808518:web:b5a2110b34147468300bc7",
            'measurementId': "G-VMR2KY4Q2Q"
        }

        self.firebase = pyrebase.initialize_app(self.firebaseConfig)

        self.db = self.firebase.database()

        self.authe = self.firebase.auth()

        self.storage = self.firebase.storage()  # for storing images and files

    def primaryKeyCreator(self, Email):  # This function creates a unique PK using the users EMAIL.
        sum = 0
        for i in Email:
            if math.isnan(i):
                sum += ord(i)
            else:
                sum += i
        return sum

    def login(self, email, password):
        try:
            self.authe.sign_in_with_email_and_password(email, password)
            output = "Successfully logged in"

        except:
            output = "Invalid Email or password"  # No need to specify exceptions since login problems will always be with email and passwords

        return output

    def create_an_account(self, email, password):

        try:

            self.authe.create_user_with_email_and_password(email, password)

            output = "Successfully created an account"

        except:
            output = "Email already exists"

        return output

    def upload_media(self, media_file_name,
                     media_name_onCloud):  # media file name can be it's path or just the name of the file(if its in the same directory).
        # if file uploaded has same cloud name as a one that alraeady exists an overwrite is done.
        try:
            self.storage.child(media_name_onCloud).put(media_file_name)
            output = "succefully executed"
        except FileNotFoundError:
            output = "File doesn't exist"
        return output

        # media_file_name will be the name of file when its saved
        # path is the path where the file will be saved to (pass an empty string to add it to the same folder as the program)

    def download_media(self, media_name_onCloud, media_file_name,
                       path):  # some what there is no exceptions thrown if any of the parameters is wrong so this function should be used with trusted inputs.

        self.storage.child(media_name_onCloud).download(path, media_file_name)

    def insertData(self, data_dict, table_name):
        PK = self.primaryKeyCreator(
            data_dict['Email'].encode('utf-8'))  # create a primary key using the hash of the email

        try:  # incase that data contains a password.
            hashedPassword = hashlib.md5(
                data_dict['Password'].encode('utf-8'))  # Hashing password for security reasons.
            hashedPassword = int(hashedPassword.hexdigest(), 16)
            data_dict['Password'] = hashedPassword

        except KeyError:
            print("dictionary doesn't contain a password")

        finally:

            self.db.child(table_name).child(PK).set(data_dict)

            return "Registered data succesfully"

    def updateData(self, data_dct, table_name,
                   PK):  # To update data you should enter it in a dictionary in this form {'column name':"data to be changed"}

        self.db.child(table_name).child(PK).update(data_dct)

        return "Updated data succefully"

    def deleteData(self, PK, table_name):  # No exceptions get thrown so it should be used with real care.
        self.db.child(table_name).child(PK).remove()

        return "Deleted succesfully"

    def getData(self, PK, table_name):  # No exceptions get thrown so it should be used with real care.
        data_dct = self.db.child(table_name).child(PK).get()
        return data_dct.val()

        # Note:If time is provided I will comeback to these functions and edit the libary of pyrebase to make them throw exceptions.
