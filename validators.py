import re
from send_otp import otp



def is_name(name:str):
    if name.isalpha():
        if len(name) >= 3:
            return True


def is_email(email):
    pattern = r"^[a-z0-9.-]+@[a-z.-]+\.[a-z]{2,}$"
    if re.match(pattern , email):
        return True
    
    
def is_otp(inputted_code):
    if inputted_code == otp:
        return True
    

def is_phone(phone):
    pattern = r"^09[0-9]{9}$"
    if re.match(pattern , phone):
        return True


def is_password(password):
    pattern = r"^(?=.*[a-z])(?=.*\d)(?=.*[A-Z])[A-Za-z\d]{8,12}$"
    if re.match(pattern , password):
        return True


def is_username(username):
    pattern = r"^[a-z0-9_.]{6,12}$"
    if re.match(pattern , username):
        return True
