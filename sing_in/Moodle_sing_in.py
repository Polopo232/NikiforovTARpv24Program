import re


Login = []
Password = []

def check_password(password_c:str) -> bool:
    """Check the password

    password_c: str
    :rtype: bool
    """
    upper = 0
    for x in password_c:
        if x.isupper():
            upper += 1

    special_sumbols = 0
    for x in password_c:
        if not x.isalpha() and not x.isdigit():
            special_sumbols += 1

    many_letters = x.count(password_c)
    if many_letters >= 8 and special_sumbols >= 1 and upper >= 1:
        return True
    else:
        return False

def usernameExists(username:str)->bool:
    """
    """
    return username in Login

def register(Username:str, Password:str) -> any:
    Usermame_r = input("Username: ")
    Password_r = input("Password: ")

    if check_password(Password_r) == True:
        Password.append(Password_r)
        if Username(usernameExists) == True:
            print("Edukalt sisse registeri")
            return
def login():
    Usermame = input("Username: ")
    Password = input("Password: ")

def menu():
    print("1. Logi sisse")
    print("2. Registreeri")
    print("3. Väljuda")
    user_menu_choice = input(": ")

    if user_menu_choice == 1:
        
    if user_menu_choice == 2:
        register()
    if user_menu_choice == 3:
        break


