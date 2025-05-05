import numpy as np
from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#functions
def clear_b(event):
    b_inp.delete(0, END)
def clear_a(event):
    a_inp.delete(0, END)
def clear_c(event):
    c_inp.delete(0, END)

#main function
def saadamutuja():
    try:
        a = int(b_inp.get())
        b = int(a_inp.get())
        c = int(c_inp.get())

        if a == 0:
            solve_text.config(text="Ei saa jagada nulliga")
        else:
            d = b ** 2 - 4 * a * c
            solve_text.config(text=f"Diskrimineeriv = {d}")

            if d < 0:
                solve_text.config(text=f"Puuduvad reaalsed lahendid, Diskrimineeriv = {d}")

            elif d == 0:
                x = -b / (2 * a)
                solve_text.config(text=f"Lahend: {x}")
            else:
                x1 = (-b + d ** 0.5) / (2 * a)
                x2 = (-b - d ** 0.5) / (2 * a)
                solve_text.config(text=f"Diskrimineeriv = {d}\nLahendid: x1 = {x1} ja x2 = {x2}")
    except ValueError:
        solve_text.config(text="Sisestatud on vale väärtus")

def draw_graph():
    try:
        a = int(b_inp.get())
        b = int(a_inp.get())
        c = int(c_inp.get())

        x_vertex = -b / (2 * a)

        x_values = np.arange(x_vertex-12, x_vertex+12, 0.1)
        y_values = a * x_values**2 + b * x_values + c 

        fig, ax = plt.subplots()

        ax.plot(x_values, y_values, label=f'y = {a}x² + {b}x + {c}')

        ax.grid(True)
        ax.set_title('Graph of the Quadratic Equation')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.axhline(0, color='black',linewidth=1)
        ax.axvline(0, color='black',linewidth=1)
        ax.legend()
        fig.show()

        
    except ValueError:
        solve_text.config(text="Sisestatud on vale väärtus")

#windows
aken = Tk()
aken.title("Teema 8")
aken.geometry("1000x600")
aken.configure(bg="pink")
aken.resizable(width=True, height=True)

pealkiri = Label(aken, text="Ruutvõrrandi lahendamine", font=("Arial", 20), fg="black", bg="pink")


#texts
fir_text = Label(aken, text=" **2 - 4 * ", font=("Arial", 15), fg="black", bg="white")
sec_text = Label(aken, text=" * ", font=("Arial", 15), fg="black", bg="white")
solve_text = Label(aken, text=saadamutuja, font=("Arial", 15), fg="black", bg="white")

#input b,a,c
b_inp = Entry(aken, font=("Arial", 15), fg="black", bg="white", relief=GROOVE)
b_inp.insert(0, "b")
b_inp.bind("<FocusIn>", clear_b)
a_inp = Entry(aken, font=("Arial", 15), fg="black", bg="white", relief=GROOVE)
a_inp.insert(0, "a")
a_inp.bind("<FocusIn>", clear_a)
c_inp = Entry(aken, font=("Arial", 15), fg="black", bg="white", relief=GROOVE)
c_inp.insert(0, "c")
c_inp.bind("<FocusIn>", clear_c)

solve_button = Button(aken, text="Lahenda", font=("Arial", 15), fg="black", bg="white",
                      activebackground="lightblue", activeforeground="black", relief=GROOVE)
graphic_button = Button(aken, text="Graphic", font=("Arial", 15), fg="black", bg="white",
                      activebackground="lightblue", activeforeground="black", relief=GROOVE)

solve_button.config(command=saadamutuja)
graphic_button.config(command=draw_graph)

#output
pealkiri.pack(pady=20)
b_inp.pack(pady=20, side=LEFT)
fir_text.pack(pady=20, side=LEFT)
a_inp.pack(pady=20, side=LEFT)
sec_text.pack(pady=20, side=LEFT)
c_inp.pack(pady=20, side=LEFT)
solve_button.pack(pady=20, side=LEFT)
graphic_button.pack(pady=20, side=LEFT)
solve_text.pack(pady=20, side="bottom", fill="x")
aken.mainloop()