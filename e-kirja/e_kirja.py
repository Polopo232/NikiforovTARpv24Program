import smtplib, ssl
from tkinter import filedialog
from email.message import EmailMessage

def saada_kiri():
    kellele = input("Sisestage e-posti aadress: ")
    pealkiri = input("Sisestage e-kirja pealkiri: ")
    sisu = input("Sisestage e-kirja sisu: ")
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    kellelt = "nikiforovnikita08@gmail.com"
    parool = input("Sisestage parool: ")
    msg = EmailMessage()
    msg['Subject'] = pealkiri
    msg['From'] = kellelt
    msg['To'] = kellele

    try:
        with open('message.html', 'r') as file:
            file_content = file.read()
            msg.add_alternative(file_content, subtype='html')
    except FileNotFoundError:
        print("HTML Viga!")
        msg.set_content(sisu)

    fail = filedialog.askopenfilename(title="Vali fail", filetypes=[("All files", "*.*")])
    if fail:
        with open(fail, 'rb') as f:
            fail_data = f.read()
            fail_nimi = fail.split("/")[-1]
            msg.add_attachment(fail_data, maintype='application', subtype='octet-stream', filename=fail_nimi)
    else:
        print("Faili ei valitud.")

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(kellelt, parool)
            server.send_message(msg)
            print("E-kiri saadetud!")
    except Exception as e:
        print(f"Viga: {e}")

saada_kiri()
