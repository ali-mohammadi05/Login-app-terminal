from io_functions import *
from models import *
from send_otp import send_otp
from pwinput import pwinput
from database import *
from logs_base import *



def login():
    clear()
    while True:
        username = get_username("enter your username: " , "\033[31musername format is not valid.\033[0m")
        if User.objects.check_username_exist(username):
            break
        else:
            print("\033[31musername doesn't exist.\033[0m")
            continue
    user_password = get_user_by("username" , "password",username)
    while True:
        password = pwinput("enter your password: ")
        if str(Password(password)) == user_password:
            change_data(username , "authentication" , f"{str(True)}\n")
            return user_dict(username)
        else:
            print("\033[31mpassword is incorrect.\033[0m")
            
        
                
    

def sign_up():
    clear()
    firstname = get_firstname("firstname(type <back> for main menu): " , "\033[31mfirstname format is not correct.\033[0m")
    if back_type(firstname):
        return False
    lastname = get_lastname("lastname: " , "\033[31mlastname format is not correct.\033[0m")
    phone_number = get_phone("phone number: " , "\033[31mphone number format is not correct.\033[0m")
    while True:
        user_email = get_email("email(write in small case): " , "\033[31myour email is not valid.\033[0m")
        if User.objects.check_email_exist(user_email):
            print("email has already used.")
            continue
        send_otp(user_email)
        verification_code = get_otp("enter the verification code(type <back> for re-entering your email): ", "\033[31myour entered code isn't correct.\033[0m")
        if back_type(verification_code):
            continue
        break
    password = get_password("password (your password must be between 8-12 characters and SHOULD include capital and small letters and digits.): " , "re-enter your password:" , "\033[31mpassword format is not correct.\033[0m" , "\033[33myour re-entered password isn't correct\033[0m")
    while True:
        username = get_username("your chosen username \n(your username must only contain small case letters,digits and <_> character and be between 6-12 characters.): " , "\033[31mUsername format is not correct.\033[0m")
        if User.objects.check_username_exist(username):
            print("\033[31mthis username has already used.\033[0m")
            continue
        break
    user = User.user_instance(firstname , lastname , phone_number , user_email , password , username)
    user.save()
    clear()
    return user_dict(username)


def forgot_password():
    clear()
    while True:
        email = get_email("enter your email: " , "\033[31memail format is not valid.\033[0m")
        if not User.objects.check_email_exist(email):
            print("email doesn't exist.")
            continue
        send_otp(email)
        verification_code = get_otp("enter the verification code(type <back> for re-entering your email): ", "\033[31myour entered code isn't correct\033[0m")
        if back(verification_code):
            continue
        break
    previous_password = get_user_by("email" , "password" , email)
    while True:
        new_password = get_password("set your new password (your password must be between 8-12 characters and SHOULD include capital and small letters and digits.): " , "re-enter your password:" , "\033[31mpassword format is not correct.\033[0m" , "\033[33myour re-entered password isn't correct\033[0m")
        if previous_password == str(Password(new_password)):
            print("\033[31mthis password is your previous password!\033[0m")
            choice = input("\033[30mdo you want to go to login page?(y/n): \033[0m").lower()
            match choice:
                case 'y':
                    login()
                    return False
                case _:
                    continue
        break
    change_data(email , "password" , str(Password(new_password)))
    return user_dict(email) 


def quit():
    reassure_prompt = "Are you sure you wanna \033[33mquit\033[0m the app?(y/<else key>)"
    choice = input(reassure_prompt)
    match choice:
        case 'y':
            exit()
        case _:
            clear()
            return False


def show_profile(user:dict):
    clear()
    temp = user.copy()
    temp.pop("password")
    temp.pop("id")
    temp.pop("authentication")
    for key,value in temp.items():
        print(f" {key}: {value}")
    while True:
        exitt = input("\npress enter for going to dashboard menu: ")
        if not exitt:
            return user
        print("\033[31mpress ENTER!\033[0m")
        continue
    

def edit_profile(user:dict):
    return user


def change_firstname(user:dict):
    clear()
    new_firstname = get_firstname("enter your new firstname: " , "\033[31mnew firstname format is not correct.\033[0m")
    change_data(user["id"],"firstname" , new_firstname)
    user["firstname"] = new_firstname
    save_logs(user["email"] , user["username"] , user["id"] , change_firstname)
    return user


def change_lastname(user:dict):
    clear()
    new_lastname = get_lastname("enter your new lastname: " , "\033[31mnew lastname format is not correct.\033[0m")
    change_data(user["id"], "lastname" , new_lastname)
    user["lastname"] = new_lastname
    save_logs(user["email"] , user["username"] , user["id"] , change_lastname)
    return user


def change_username(user:dict):
    clear()
    while True:
        new_username = get_username("enter your new username \n(your username must only contain small case letters,digits and <_> character and be between 6-12 characters.): " , "\033[31mUsername format is not correct.\033[0m")
        if User.objects.check_username_exist(new_username):
            print("this username has already used.")
            continue
        break
    change_data(user["id"], "username" , new_username)
    user["username"] = new_username
    save_logs(user["email"] , user["username"] , user["id"] , change_username)
    return user


def change_password(user:dict):
    clear()
    new_password= get_password("enter your new password \n(your password must be between 8-12 characters and SHOULD include capital and small letters and digits.): " , "re-enter your new password:" , "\033[31mpassword format is not correct.\033[0m" , "\033[33myour re-entered password isn't correct\033[0m")
    change_data(user["id"],"password" , str(Password(new_password)))
    user["password"] = str(Password(new_password))
    save_logs(user["email"] , user["username"] , user["id"] , change_password)
    return user


def change_phone_number(user:dict):
    clear()
    new_phone_number = get_phone("enter your new phone number: " , "\033[31mnew phone number format is not valid.\033[0m")
    change_data(user["id"] , "phone number" , new_phone_number)
    user["phone number"] = new_phone_number
    save_logs(user["email"] , user["username"] , user["id"] , change_phone_number)
    return user
            
            
def logs(user:dict):
    clear()
    userlog = user_logs(user["id"])
    show_logs(userlog)
    save_logs(user['email'] , user['username'] , user['id'] , logs)
    while True:
        backtomenu = input("\npress enter for going to dashboard menu: ")
        if not backtomenu:
            return user
        print("\n\033[31mpress ENTER!\033[0m")
        continue


def delete_account(user:dict):
    reassure_prompt = "\nAre you sure you wanna \033[31mDELETE\033[0m your account?!(y/<else key>)"
    while True:
        choice = input(reassure_prompt).lower()
        match choice:
            case 'y':
                change_data(user["id"] , "authentication" , f"{str(False)}\n" )
                save_logs(user["email"] , user["username"] , user["id"] , delete_account)
                remove_account(user)
                clear()
                return False
            case _:
                clear()
                return user


def logout(user:dict):
    reassure_prompt = "\nAre you sure you wanna \033[33mlogout\033[0m from your account?(y/<else key>)"
    while True:
        choice = input(reassure_prompt).lower()
        match choice:
            case 'y':
                change_data(user["id"] , "authentication" , f"{str(False)}\n" )
                save_logs(user["email"] , user["username"] , user["id"] , logout)
                clear()
                return False
            case _:
                clear()
                return user


def back(user:dict):
    return user

