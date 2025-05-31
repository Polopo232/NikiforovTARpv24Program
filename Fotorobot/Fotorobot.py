import tkinter as tk
from tkinter import colorchooser
from PIL import Image, ImageTk, ImageOps
import customtkinter
from CTkColorPicker import * # download CTkColorPicker

customtkinter.set_appearance_mode("dark")  

root = customtkinter.CTk()
root.title("Fotorobot")
root.geometry("950x1030")

canvas = tk.Canvas(root, width=700, height=700, bg="white")
canvas.pack(side="right", padx=10, pady=10)

control_frame = customtkinter.CTkFrame(root, width=400)
control_frame.pack(side="left", fill="y", padx=10, pady=10)

current_images = {}
skin_color = "#FFDBAC"

def lae_pilt(pilti_tee, kiht):
    try:
        img = Image.open(pilti_tee)
        
        if kiht == "Näo kuju":
            img = img.convert("RGBA")
            andmed = img.getdata()
            uued_andmed = []
            for piksel in andmed:
                if piksel[3] > 0:
                    r = int(skin_color[1:3], 16)
                    g = int(skin_color[3:5], 16)
                    b = int(skin_color[5:7], 16)
                    uued_andmed.append((r, g, b, piksel[3]))
                else:
                    uued_andmed.append(piksel)
            img.putdata(uued_andmed)
        
        foto = ImageTk.PhotoImage(img)
        current_images[kiht] = {"foto": foto, "pilt": img, "tee": pilti_tee}
        uuenda_liin()
    except Exception as e:
        print(f"Viga pildi laadimisel: {e}")

def uuenda_liin():
    canvas.delete("all")
    
    kihid = [
        "Näo kuju",
        "Kulmud",
        "Silmad",
        "Nina",
        "Suu",
        "Habe"
    ]
    
    for kiht in kihid:
        if kiht in current_images:
            canvas.create_image(350, 350, image=current_images[kiht]["foto"])

def tyhjenda_liin():
    global current_images
    canvas.delete("all")
    current_images = {}

def vali_nahavarv(valitud_varv=None):
    global skin_color
    if valitud_varv:
        skin_color = valitud_varv
    else:
        varv = colorchooser.askcolor(title="Vali nahavärv")
        if varv[1]:
            skin_color = varv[1]

    if "Näo kuju" in current_images:
        lae_pilt(current_images["Näo kuju"]["tee"], "Näo kuju")


def loo_kategooria(vanem, pealkiri, esemed):
    raam = customtkinter.CTkFrame(vanem)
    raam.pack(fill="x", padx=5, pady=5)

    pealkiri_label = customtkinter.CTkLabel(raam, text=pealkiri, padx=5, pady=5)
    pealkiri_label.pack(fill="x")

    for nimi, tee in esemed.items():
        def loo_klahvi_kaivitus(p=tee, k=pealkiri):
            return lambda: lae_pilt(p, k)

        klahv = customtkinter.CTkButton(raam, text=nimi, command=loo_klahvi_kaivitus())
        klahv.pack(fill="x", pady=2)


näo_kujud = {
    "1 Shape": "213/naovorm1.png",
    "2 Shape": "463/faceshape.png",
    "3 Shape": "534/faceshape.png"
}

silmad = {
    "Silmad 1": "213/eyes.png",
    "Silmad 2": "463/eyes.png",
    "Silmad 3": "534/eyes.png"
}

kulmud = {
    "Kulmud 1": "213/brows.png",
    "Kulmud 2": "463/brows.png",
    "Kulmud 3": "534/brows.png"
}

ninad = {
    "Nina 1": "213/nose.png",
    "Nina 2": "463/nose.png",
    "Nina 3": "534/nose.png"
}

suud = {
    "Suu 1": "213/mouth.png",
    "Suu 2": "463/mouth.png",
    "Suu 3": "534/mouth.png"
}

habemed = {
    "Habe 1": "213/moustashe.png",
    "Habe 2": "463/moustashe.png",
    "Habe 3": "534/moustashe.png"
}

loo_kategooria(control_frame, "Näo kuju", näo_kujud)
loo_kategooria(control_frame, "Kulmud", kulmud)
loo_kategooria(control_frame, "Silmad", silmad)
loo_kategooria(control_frame, "Nina", ninad)
loo_kategooria(control_frame, "Suu", suud)
loo_kategooria(control_frame, "Habe", habemed)

#color picker

colorpicker = CTkColorPicker(control_frame,
                             width=100,
                             height=30,
                             command=vali_nahavarv)
colorpicker.pack(fill="x", pady=5)

tyhjenda_klahv = customtkinter.CTkButton(control_frame, text="Tühjenda kõik", command=tyhjenda_liin)
tyhjenda_klahv.configure(fg_color="#FF0000", hover_color="#610000")
tyhjenda_klahv.pack(fill="x", pady=5)


root.mainloop()
