import hashlib
from uuid import uuid4
from database import get_column


class Password:
    def __init__(self, password):
        self.password = password

    def check(self, value):
        if self.password == self.hash(value):
            return True
        return False

    def hash(self, password: str):
        return hashlib.sha256(password.encode()).hexdigest()

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = self.hash(new_password)

    def to_csv(self):
        return self.password

    def __str__(self):
        return self.password


class Username:
    def __init__(self, username: str):
        self.username = username

    def to_csv(self):
        return self.username


class Name:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def to_csv(self):
        return f"{self.first_name},{self.last_name}".lower()


class Email:
    def __init__(self, email):
        self.email = email

    def to_csv(self):
        return self.email


class PhoneNumber:
    def __init__(self, phone):
        self.phone = phone

    def to_csv(self):
        return f"{self.phone}"


class Profile:
    def __init__(
        self,
        first_name="",
        last_name="",
        phone_number=""):
        self.name = Name(first_name, last_name)
        self.phone_number = PhoneNumber(phone_number)

    def to_csv(self):
        return f"{self.name.to_csv()},{self.phone_number.to_csv()}"


class UserManager:
    def all(self):
        pass

    def check_username_exist(self ,username):
        if username in get_column("username"):
            return True

    def check_email_exist(self , email):
        if email in get_column("email"):
            return True


class User:
    objects = UserManager()

    def __init__(self, username, email, password, id=""):
        if id:
            self.id = id
        else:
            self.id = uuid4()
        self.username = Username(username)
        self.email = Email(email)
        self.password = Password(password)
        self.profile = Profile()
        self.is_authenticate = False


    def to_csv(self):
        return f"{self.profile.to_csv()},{self.email.to_csv()},{self.password.to_csv()},{self.username.to_csv()},{self.id},{self.is_authenticate}"


    def save(self):
        with open("data.csv" , "a") as file:
            file.write(self.to_csv() + "\n")


    @staticmethod
    def user_instance(firstname , lastname, phone_number , email , password , username):
        user = User(username , email , password )
        user.profile = Profile(firstname , lastname , phone_number) 
        return user

    