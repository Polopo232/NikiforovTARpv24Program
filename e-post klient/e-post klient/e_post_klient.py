import smtplib
import json
import ssl
import imghdr
from PIL import Image, ImageTk
from email.message import EmailMessage
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import ttkbootstrap as ttk

SAVE_FILE = "draft.json"
file = None

# functions
def load_draft():
    global file
    try:
        with open(SAVE_FILE, "r") as f:
            draft_data = json.load(f)
            email_input.delete(0, END)
            email_input.insert(0, draft_data.get("email", ""))
            tema_input.delete(0, END)
            tema_input.insert(0, draft_data.get("tema", ""))
            kirja_input.delete("1.0", END)
            kirja_input.insert("1.0", draft_data.get("message", ""))
            file = draft_data.get("file", "")
            if file:
                image_path_label.config(text=file.split('/')[-1])
    except FileNotFoundError:
        print("No saved draft found.")
    except json.JSONDecodeError:
        print("Error reading draft.")

def pre_window():
    global file
    new_window = ttk.Window(themename="cosmo")
    new_window.title("Teema 8")
    new_window.geometry("500x500")
    new_window.resizable(width=True, height=True)

    tema = tema_input.get()
    email = email_input.get()
    message = kirja_input.get("1.0", END)

    preview_label = ttk.Label(new_window, text="Eelvaade", font=("Arial", 16))
    tema_label = ttk.Label(new_window, text=f"Tema: {tema}", font=("Arial", 16))
    email_label = ttk.Label(new_window, text=f"Saaja: {email}", font=("Arial", 16))
    message_label = ttk.Label(new_window, text="Kiri:", font=("Arial", 16))
    message_content = ttk.Label(new_window, text=message, font=("Arial", 16), justify=LEFT)

    if not file:
        image_text = "Lisa puudub"
        image_label = ttk.Label(new_window, text=image_text, font=("Arial", 12))
    else:
        image_text = f"Lisa: {file.split('/')[-1]}"
        image_label = ttk.Label(new_window, text=image_text, font=("Arial", 12))

        try:
            img = PhotoImage(file=file)

            max_size = 150
            width, height = img.width(), img.height()
            aspect_ratio = width / height

            if width > max_size or height > max_size:
                if aspect_ratio > 1:
                    new_width = max_size
                    new_height = int(max_size / aspect_ratio)
                else:
                    new_height = max_size
                    new_width = int(max_size * aspect_ratio)

                img = img.subsample(int(width / new_width), int(height / new_height))

            image_display_label = ttk.Label(new_window, image=img)
            image_display_label.image = img
            image_display_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)
        except Exception as e:
            print(f"Error loading image: {e}")
            image_label = ttk.Label(new_window, text="Невозможно загрузить изображение", font=("Arial", 12))

    # function to send email
    def send_email():
        emailNupp()
        new_window.destroy()

    # buttons
    send_button = ttk.Button(new_window, text="Saada", style="success.TButton", command=send_email)
    cancel_button = ttk.Button(new_window, text="Tühista", style="danger.TButton", command=new_window.destroy)

    # output
    preview_label.grid(row=0, column=0, columnspan=2, sticky="w", padx=5, pady=5)
    tema_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)
    email_label.grid(row=2, column=0, columnspan=2, sticky="w", padx=5, pady=5)
    message_label.grid(row=3, column=0, columnspan=2, sticky="w", padx=5, pady=5)
    message_content.grid(row=4, column=0, columnspan=2, sticky="w", padx=5, pady=5)
    image_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    send_button.grid(row=7, column=0, padx=5, pady=10, sticky="e")
    cancel_button.grid(row=7, column=1, padx=5, pady=10, sticky="w")

def vali_pilt(): 
    global file 
    file = filedialog.askopenfilename() 
    if file:
        image_path_label.config(text=file)

def emailNupp():
    teema = tema_input.get()
    kellele = email_input.get()
    kiri = kirja_input.get("1.0", END)
    if (kellele.find(",") == -1):
        saada_kiri(kellele, kiri, teema)
    else:
        for email in kellele.split(","):
            saada_kiri(email.strip(), kiri, teema)

def saada_kiri(kellele, kiri, teema): 
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "nikiforovnikita08@gmail.com"
    password = 'yksj yudm flgi nyqx' #УДАЛИТЬ 
    context = ssl.create_default_context()
    msg = EmailMessage()
    msg.set_content(kiri)
    msg['Subject'] = teema
    msg['From'] = "Nikita"
    msg['To'] = kellele

    if file:
        with open(file, 'rb') as fpilt:
            pilt = fpilt.read()
            msg.add_attachment(pilt, maintype='image', subtype=imghdr.what(None, pilt))

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        messagebox.showinfo("Informatsioon", "Kiri oli saadetud")
    except Exception as e:
        messagebox.showerror("Tekkis viga!", str(e))
    finally:
        server.quit()

def save_draft():
    draft_data = {
        "email": email_input.get(),
        "tema": tema_input.get(),
        "message": kirja_input.get("1.0", END),
        "file": file if file else ""
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(draft_data, f)
    print("Mustand salvestatud!")

def on_closing():
    save_draft()
    aken.quit()

# window
aken = ttk.Window(themename="cosmo")
aken.title("Teema 8")
aken.geometry("500x500")
aken.resizable(width=True, height=True)

# main frame
main_frame = ttk.Frame(aken)
main_frame.pack(expand=True, fill="both")

# input frame
input_frame = ttk.Frame(main_frame)
input_frame.pack(pady=20)

# image path label
image_path_label = ttk.Label(input_frame, text="No image selected")
image_path_label.grid(row=0, column=1, padx=10, pady=10)

image_label = ttk.Label(input_frame)
image_label.grid(row=1, column=0, columnspan=2, pady=10)

# text labels
email_text = ttk.Label(input_frame, text=" Email: ", font=("Arial", 15))
tema_text = ttk.Label(input_frame, text=" Teema: ", font=("Arial", 15))
kirja_text = ttk.Label(input_frame, text=" Kiri: ", font=("Arial", 15))
lisa_text = ttk.Label(input_frame, text=" Lisa: ", font=("Arial", 15))

# input fields
email_input = ttk.Entry(input_frame, width=30, font=("Arial", 14))
tema_input = ttk.Entry(input_frame, width=30, font=("Arial", 14))
kirja_input = Text(input_frame, height=10, width=30, font=("Arial", 14))

# buttons
lisa_button = ttk.Button(input_frame, text="Lisa", style="info.TButton", command=vali_pilt)
Saada_button = ttk.Button(input_frame, text="Saada", style="success.TButton", command=pre_window)

# output layout
email_text.grid(row=0, column=0, sticky="w", padx=5, pady=5)
email_input.grid(row=0, column=1, sticky="w", padx=5, pady=5)

tema_text.grid(row=1, column=0, sticky="w", padx=5, pady=5)
tema_input.grid(row=1, column=1, sticky="w", padx=5, pady=5)

lisa_text.grid(row=2, column=0, sticky="w", padx=5, pady=5)

kirja_text.grid(row=3, column=0, sticky="w", padx=5, pady=5)
kirja_input.grid(row=3, column=1, sticky="w", padx=5, pady=10)

lisa_button.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)
image_path_label.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

Saada_button.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)

load_draft()

aken.protocol("WM_DELETE_WINDOW", on_closing)
aken.mainloop()
