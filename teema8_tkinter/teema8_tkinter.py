from tkinter import *

k = 0

def vajutatud(event):
    global k
    k += 1
    pealkiri.config(text=f"Nupp vajutatud {k} korda")
    pealkiri.config(fg="black", font=("Arial", 20), bg="pink")

def vajutatud2(event):
    global k
    k -= 1
    pealkiri.config(text=f"Nupp vajutatud {k} korda")
    pealkiri.config(fg="black", font=("Arial", 20), bg="pink")

def tuhista(event):
    sisetus.delete(0, END)

aken = Tk()
aken.title("Teema 8")
aken.geometry("400x400")
aken.configure(bg="pink")
aken.resizable(width=False, height=False)
aken.iconbitmap("icon.ico")

pealkiri = Label(aken, text="Teema 8", font=("Arial", 20), fg="black", bg="pink")
nupp = Button(aken, text="button", font=("Arial", 15), fg="black", bg="white", 
              activebackground="lightblue", activeforeground="black", relief=GROOVE)

nupp.bind("<Button-1>", vajutatud)
nupp.bind("<Button-3>", vajutatud2)

sisetus = Entry(aken, font=("Arial", 15), fg = "black", bg="white", relief=GROOVE)
sisetus.insert(0, "Sisesta midagi") #END instead of 0
sisetus.bind("<FocusIn>", tuhista)




pealkiri.pack(pady=20)
sisetus.pack(pady=20)
nupp.pack(pady=20)
aken.mainloop()