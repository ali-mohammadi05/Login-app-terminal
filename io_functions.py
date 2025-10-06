from os import system
from sys import platform
from pwinput import pwinput
from validators import *
from models import User



def clear():
    if platform == "linux" or platform == "linux2":
        system("clear")
    elif platform == "darwin":
        system("clear")
    elif platform == "win32":
        system("cls")


def get_firstname(prompt, error):
    while True:
        firstname = input(prompt)
        if is_name(firstname):
            return firstname
        else:
            print(error)
            

def get_lastname(prompt, error):
    while True:
        lastname = input(prompt)
        if is_name(lastname):
            return lastname
        else:
            print(error)


def get_email(prompt , error):
    while True:
        email = input(prompt)
        if is_email(email):
            return email
        print(error)


def get_otp(prompt , error):
    while True:
        otp = input(prompt)
        if is_otp(otp):
            return otp
        else:
            print(error)


def get_phone(prompt , error):
    while True:
        phone_number = input(prompt)
        if is_phone(phone_number):
            return phone_number
        else:
            print(error)


def get_password(prompt, prompt2 , error1 , error2):
    while True:
        password = pwinput(prompt)
        if is_password(password):
            double_check = pwinput(prompt2)
            if password == double_check:
                return password
            else:
                print(error2)
        else:
            print(error1)


def get_username(prompt , error):
    while True:
        username = input(prompt)
        if is_username(username):
            return username
        else:
            print(error)


def back_type(value:str):
    if str(value).lower() == "back":
        clear()
        return True