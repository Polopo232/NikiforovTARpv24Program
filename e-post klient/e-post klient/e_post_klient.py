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
files = []

# functions
def load_draft():
    global files
    with open(SAVE_FILE, "r") as f:
        draft_data = json.load(f)
        email_input.delete(0, END)
        email_input.insert(0, draft_data.get("email", ""))
        tema_input.delete(0, END)
        tema_input.insert(0, draft_data.get("tema", ""))
        kirja_input.delete("1.0", END)
        kirja_input.insert("1.0", draft_data.get("message", ""))
        files = draft_data.get("files", [])
        if files:
            image_path_label.config(text=f"Valitud {len(files)} faili")

def pre_window():
    global file, files
    
    preview_window = ttk.Toplevel(aken)
    preview_window.title("Eelvaade")
    preview_window.geometry("600x750")

    tema = tema_input.get()
    email = email_input.get()
    message = kirja_input.get("1.0", END)
    
    # Заголовок окна
    title_label = ttk.Label(preview_window, text="Eelvaade", font=("Arial", 16, "bold"))
    title_label.pack(pady=10)

    email_frame = ttk.Frame(preview_window)
    email_frame.pack(fill='x', padx=10, pady=5)
    ttk.Label(email_frame, text="Saaja:", font=("Arial", 12)).pack(side='left')
    ttk.Label(email_frame, text=email, font=("Arial", 12)).pack(side='left', padx=5)

    tema_frame = ttk.Frame(preview_window)
    tema_frame.pack(fill='x', padx=10, pady=5)
    ttk.Label(tema_frame, text="Teema:", font=("Arial", 12)).pack(side='left')
    ttk.Label(tema_frame, text=tema, font=("Arial", 12)).pack(side='left', padx=5)

    ttk.Label(preview_window, text="Kiri:", font=("Arial", 12)).pack(anchor='w', padx=10, pady=5)
    
    message_frame = ttk.Frame(preview_window)
    message_frame.pack(fill='both', expand=True, padx=10, pady=5)

    message_text = Text(message_frame, wrap='word', font=("Arial", 11))
    message_text.insert('1.0', message)
    message_text.config(state='disabled')
    message_text.pack(side='left', fill='both', expand=True)

    ttk.Label(preview_window, text="Lisa:", font=("Arial", 12)).pack(anchor='w', padx=10, pady=5)
    
    if files:
        for f in files:
            ttk.Label(preview_window, text=f.split('/')[-1]).pack(anchor='w', padx=20)
    elif file:
        ttk.Label(preview_window, text=file.split('/')[-1]).pack(anchor='w', padx=20)
    else:
        ttk.Label(preview_window, text="Puuduvad").pack(anchor='w', padx=20)
    
    buttons_frame = ttk.Frame(preview_window)
    buttons_frame.pack(pady=10)

    def saada_kiri_command():
        emailNupp()
        preview_window.destroy()

    send_button = ttk.Button(buttons_frame, text="Saada", style='success.TButton', command=saada_kiri_command)
    send_button.pack(side='left', padx=5)
    
    cancel_button = ttk.Button(buttons_frame, text="Tühista", style='danger.TButton', command=preview_window.destroy)
    cancel_button.pack(side='left', padx=5)

def vali_pilt(): 
    global files
    selected = filedialog.askopenfilenames()
    if selected:
        files = list(selected)
        image_path_label.config(text=f"Valitud {len(files)} faili")

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
        password = '123' #УДАЛИТЬ 
        context = ssl.create_default_context()
        msg = EmailMessage()
        msg.set_content(kiri)
        msg["Subject"] = teema
        msg["From"] = "Nikita"
        msg["To"] = kellele
        
        for file_path in files:
            with open(file_path, "rb") as f:
                file_data = f.read()
                if file_path.lower().endswith(".jpg"):
                    msg.add_attachment(file_data, maintype="image", subtype="jpeg", filename=file_path.split('/')[-1])
                elif file_path.lower().endswith(".png"):
                    msg.add_attachment(file_data, maintype="image", subtype="png", filename=file_path.split('/')[-1])
                else:
                    msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_path.split('/')[-1])
        
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
        "files": files
    }
    with open(SAVE_FILE, "w") as f:
        json.dump(draft_data, f)

def on_closing():
    save_draft()
    aken.quit()

def few_files():
    global files
    selected = filedialog.askopenfilenames()
    if selected:
        files = list(selected)
        image_path_label.config(text=f"Valitud {len(files)} faili")
    
# window
aken = ttk.Window(themename="cyborg")
aken.title("E-posti klient")
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
