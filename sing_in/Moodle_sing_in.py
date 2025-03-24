Login = ['1']
Password = ['1']
login_is = False
Username_l = ""

def check_password(password_c: str) -> bool:
    """Check the password

    password_c: str
    :rtype: bool
    """
    upper = 0
    for x in password_c:
        if x.isupper():
            upper += 1

    digit = 0
    for x in password_c:
        if x.isdigit():
            digit += 1

    special_symbols = 0
    for x in password_c:
        if not x.isalpha() and not x.isdigit():
            special_symbols += 1

    many_letters = len(password_c)
    if many_letters >= 8 and special_symbols >= 1 and upper >= 1:
        return True
    else:
        return False

def usernameExists(username: str) -> bool:
    """
    Check if the username exists
    """
    return username in Login

def generated_password()-> str:
    """
    Generate password
    """
    import random
    while True:
        str0=".,:;!_*-+()/#¤%&"
        str1 = '0123456789'
        str2 = 'qwertyuiopasdfghjklzxcvbnm'
        str3 = str2.upper()
        str4 = str0+str1+str2+str3
        ls = list(str4)
        random.shuffle(ls)
        # Извлекаем из списка 12 произвольных значений
        psword = ''.join([random.choice(ls) for x in range(12)])
        # Пароль готов
        if check_password(psword) == True:
            print("Sinu parool on ",psword)
            return psword
        else:
            continue


def register() -> None:
    Username_r = input("Username: ")
    choice1 = input("Kas soovite luua parooli ise või soovite et programm genereeriks parooli ise? (i/g): ")
    if choice1 == 'i':
        while True:
            Password_r = input("Password: ")
            if check_password(Password_r):
                if not usernameExists(Username_r):
                    Login.append(Username_r)
                    Password.append(Password_r)
                    print("Edukalt sisse registeri")
                    return
                else:
                    print("Kasutajanimi on juba olemas")
                    return register()
            else:
                print("Parool ei vasta nõuetele")
    if choice1 == 'g':
        generated_password()

def login() -> None:
    global login_is, Username_l
    Username_l = input("Username: ")
    Password_l = input("Password: ")

    if Username_l in Login:
        if Password_l == Password[Login.index(Username_l)]:
            login_is = True
            print("Sisse logitud")
        else:
            choice = input("Vale parool, kas sa tahad muuda? (y/n): ")
            if choice == 'y':
                if Username_l in Login:
                    change_password()
                else:
                    print("Kasutajat ei eksisteeri")
            if choice == 'n':
                print("Vale parool")
            print("Vale parool")

def change_password() -> None:
    global login_is
    if login_is:
        new_password = input("Uus parool: ")
        if check_password(new_password):
            Password[Login.index(Username_l)] = new_password
            print("Parool on muudetud")
        else:
            print("Parool ei vasta nõuetele")
    else:
        print("Palun logige sisse")

def login_out() -> None:
    global login_is
    if login_is == True:
        login_is = False
        print("Välja logitud")
    else:
        print("Sa ei ole sisse logitud")


def menu() -> None:
    global login_is
    while True:
        if login_is:
            print(f"Tere, {Username_l}!")
        print("1. Logi sisse")
        print("2. Registreeri")
        print("3. Muuda parooli")
        print("4. Logi välja")
        print("5. Välju")
        user_menu_choice = input(": ")

        if user_menu_choice == '1':
            login()
        elif user_menu_choice == '2':
            register()
        elif user_menu_choice == '3':
            change_password()
        elif user_menu_choice == '4':
            login_out()
        elif user_menu_choice == '5':
            break
        elif user_menu_choice == '6':
            print(Login)
            print(Password)
        else:
            print("Vale valik, palun proovige uuesti")
