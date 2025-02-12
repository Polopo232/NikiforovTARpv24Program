from calendar import *
from datetime import date
from math import *


#ulesanne 10
try:
    aeg = int(input("Sisesta aeg minutites: "))
    if aeg > 0:
        tunnid = aeg // 60
        minute = aeg % 60
        print(f"Tunnid: {tunnid}:{minute}")
    else:
        print("Arvud peavad sureem kui 0 olla!")
except:
    print("Sisesta täisarv!")

#ulesanne 9

kiirus = 29.9
kiirus = kiirus / 60 * 1000
print(f"Kiirus on {kiirus}m/s") 

#ulesanne 8

try:
    liit = float(input("Liitrid: "))
    km = float(input("Kilomeetrid: "))
    if liit > 0 and km > 0:
        kogus = liit / km * 100
        print(f"Kütusekulu 100 km kohta {kogus}l")
    else:
        print("Arvud peavad sureem kui 0 olla!")
except:
    print("Sisesta ujukomaarvud!")


#ulesanne 7
try:
    a = float(input("a: "))
    b = float(input("b: "))
    if a>0 and b>0:
        print("Pindala ja umbermoodu rvutamine: ")
        S = a * b
        P = 2 * (a + b)
    else:
        print("Arvud peavad sureem kui 0 olla!")

    print(f"Vastus:\nRistküliku pindala on {S}, ristküliku ümbermõõt on {P}.")
except :
    print("Sisesta ujukomaarvud!")

#ulesanne 6

stih = "Koosta programm, mis väljastaks järgmised laulusõnad suurte tähtedega:\nRong see sõitis tsuhh tsuhh tsuhh,\npiilupart oli rongijuht.\nRattad tegid rat tat taa,\nrat tat taa ja tat tat taa.\nAga seal rongi peal,\nkas sa tead, kes olid seal?\nRong see sõitis tuut tuut tuut,\npiilupart oli rongijuht.\nRattad tegid kill koll koll,\nkill koll koll ja kill koll kill.\n....Sisend, väljund, tingimus....".upper()
print(stih)

# ulesanne 5

a = "kill-koll ".capitalize()
b = "killadi-koll ".capitalize()
print(a*2,b,a*2,b,a*4)

#ulesanne 4

deuro = 2.575
maaR = 6378
maaR *= 100000
Pmaa = 2 * pi * maaR
Peuro = Pmaa / deuro
print(f"Mooda ekvaatorit jaotamiseks 2 euro munti. See votab {int(Peuro):,d} munte")
print(f"Meil on vaja {int(Peuro*2):,d} euro")


#ulesanne 3
try:
    R = float(input("R: "))
    Sruduu = round((2*R) ** 2)
    Sringi = round(pi * R ** 2)
    Pruudu = round(8*R)
    Pringi = round(2*pi*R)
    print(f"Vastus:\nRuudu pindala on {Sruduu}, ruudu umbermoot on {Pruudu}, \nringi pindala on {Sringi}, Ringi umbermoot on {Pringi}.")

except:
    print("Sisesta ujukomaarvud!")


#ulesanne 2
a = 3 + 8 / (4 - 2) * 4
print(f"3 + 8 / (4 - 2) * 4 = {a}")

a = (3 + 8) / 4 - 2 * 4
print(f"(3 + 8) / 4 - 2 * 4 = {a}")

a = 3 + 8 / (4 - 2 * 4)
print(f"3 + 8 / (4 - 2 * 4) = {a}")

a = 3 + 8 / 4 - 2 * 4
print(f"3 + 8 / 4 - 2 * 4 = {a}")

#ulesanne 1

# tana = date.today()
# print(f"Tere, tana on {tana}")

# tana_ = tana.strftime("%B %d, %Y")
# print(f"Tere! Tana on {tana}")

# tana_ = tana.strftime("%m/%d/%y")
# print(f"Tere! Tana on {tana_}")

# tana_ = tana.strftime("%b-%d-%y")
# print(f"Tere! Tana on {tana_}")

# tana_ = tana.strftime("%d/%m/%Y")
# print(f"Tere! Tana on {tana_}")

# paeva = monthrange(2025,1)[1]
# print(f"Jaanusris on {paeva} paeva")
# paevad = tana.day
# onjaanud = paeva - paevad
# print(f"Jaanuaris on jaanud {onjaanud} paeva")

# paeva1 = 365 - monthrange(2025, 1)[1] + onjaanud
# print(f"Aasta lopuni on jaanud {paeva1}")

