import smtplib, ssl
from tkinter import filedialog
from email.message import EmailMessage

Login = []
Password = []
gmail = []
login_is = False
Username_l = ""

def loe_fail():
    kasutajad = []
    with open("users.txt", "r", encoding="utf-8-sig") as fail:
        for line in fail:
            name, mail, password = line.strip().split(":")
            kasutajad.append({"login": name, "email": mail, "password": password})
            Login.append(name)
            gmail.append(mail)
            Password.append(password)
    return kasutajad

def salvesta_fail(kasutajad):
    with open("users.txt", "w", encoding="utf-8-sig") as fail:
        for kasutaja in kasutajad:
            fail.write(f"{kasutaja['login']}:{kasutaja['email']}:{kasutaja['password']}\n")
    print("Kasutajad on salvestatud faili users.txt")

def saada_kiri(gmail_send, pealkiri, sisse):
    kellele = gmail_send
    kiri = pealkiri
    sisu = sisse
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    kellelt = "nikiforovnikita08@gmail.com"
    parool = '123'
    msg = EmailMessage()
    msg['Subject'] = kiri
    msg['From'] = kellelt
    msg['To'] = kellele
    msg.set_content(sisu)

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls(context=ssl.create_default_context())
        server.login(kellelt, parool)
        server.send_message(msg)
        print("Email saadetud edukalt")
    except Exception as e:
        print(f"Viga: {e}")

def check_password(password_c: str) -> bool:
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
    return username in Login

def generated_password()-> str:
    import random
    while True:
        str0=".,:;!_*-+()/#¤%&"
        str1 = '0123456789'
        str2 = 'qwertyuiopasdfghjklzxcvbnm'
        str3 = str2.upper()
        str4 = str0+str1+str2+str3
        ls = list(str4)
        random.shuffle(ls)
        psword = ''.join([random.choice(ls) for x in range(12)])
        if check_password(psword) == True:
            print("Sinu parool on ",psword)
            return psword
        else:
            continue

def register() -> None:
    global gmail, Login, Password
    username = input("Kasutajanimi: ")
    gmail_user = input("Gmail: ")
    
    if "@" in gmail_user and "." in gmail_user:
        gmail.append(gmail_user)
    else:
        print("Vale e-post.")
        return register()

    choice1 = input("Kas soovite luua parooli ise või soovite, et programm genereeriks selle? (i/g): ")
    if choice1 == 'i':
        while True:
            Password_r = input("Parool: ")
            if check_password(Password_r):
                if not usernameExists(username):
                    Login.append(username)
                    Password.append(Password_r)
                    print("Registreerimine õnnestus!")
                    mail = saada_kiri(gmail_user, f"Täname registreerimise eest", f"Teie kasutajanimi on {username} ja parool on {Password_r}")
                    kasutajad = loe_fail()
                    kasutajad.append({"login": username, "email": gmail_user, "password": Password_r})
                    salvesta_fail(kasutajad)
                    return
                else:
                    print("Kasutajanimi on juba olemas.")
                    return register()
            else:
                print("Parool ei vasta nõuetele.")
    elif choice1 == 'g':
        Password_r = generated_password()
        Password.append(Password_r)
        Login.append(username)
        mail = saada_kiri(gmail_user, f"Täname registreerimise eest", f"Teie kasutajanimi on {username} ja parool on {Password_r}")
        kasutajad = loe_fail()
        kasutajad.append({"login": username, "email": gmail_user, "password": Password_r})
        salvesta_fail(kasutajad)

def login() -> None:
    global login_is, Username_l, gmail
    Username_l = input("Username: ")
    user_gmail = input("Gmail: ")
    Password_l = input("Password: ")

    if Username_l in Login:
        user_index = Login.index(Username_l)
        if user_gmail == gmail[user_index] and Password_l == Password[user_index]:
            login_is = True
            print("Sisse logitud")
            saada_kiri(user_gmail, "Login", "Keegi on teie kontole sisse loginud. Kui see olite teie, siis ignoreerige seda teadet.")
        else:
            choice = input("Vale parool, kas sa tahad muuda? (y/n): ").lower()
            if choice == 'y':
                print("Saadame sulle e-maili, et muuta oma parool, palun kontrolli oma e-maili aadressi")
                saada_kiri(user_gmail, "Parool on vale", "Palun muuda oma parool www.changepassword.com")
            else:
                print("Vale parool")
    else:
        print("Kasutajat ei eksisteeri")

def change_password() -> None:
    global login_is
    if login_is:
        new_password = input("Uus parool: ")
        if check_password(new_password):
            user_index = Login.index(Username_l)
            Password[user_index] = new_password
            kasutajad = []
            for i in range(len(Login)):
                kasutajad.append({
                    "login": Login[i],
                    "email": gmail[i],
                    "password": Password[i]
                })
            salvesta_fail(kasutajad)
            print("Parool on muudetud")

            saada_kiri(gmail[user_index], "Parool on muudetud", f"Teie uus parool on: {new_password}")
        else:
            print("Parool ei vasta nõuetele")
    else:
        print("Palun logige sisse")

def login_out() -> None:
    global login_is
    if login_is:
        login_is = False
        print("Välja logitud")
    else:
        print("Sa ei ole sisse logitud")

loe_fail()

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
            print(gmail)
        else:
            print("Vale valik, palun proovige uuesti")
