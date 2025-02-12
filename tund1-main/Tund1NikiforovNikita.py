#10 harjutus

pitsa = 12.90
napunaiteid = 0.10
summa = pitsa * napunaiteid
kogusumma = pitsa + summa
summa = kogusumma / 2
print(f"Summa on {summa} euro")

#9 hartujus

a = float(input("Mitu sentimeetrit on külg a: "))
b = float(input("Mitu sentimeetrit on külg b: "))
c = float(input("Mitu sentimeetrit on külg c: "))

print("Perimeeter on ", a+b+c , "cm")

#8 harjutus


print("   @..@")
print("  (----)")
print(" ( \__/ )")
print("  ^^ "" ^^ ")


#7 harjutus

num1 = int(input("Esimene täisarv: "))
num2 = int(input("Teine täisarv: "))
num3 = int(input("Kolmas täisarv: "))
num4 = int(input("Neljas täisarv: "))
num5 = int(input("Viies täisarv: "))

kesk = (num1 + num2 + num3 + num4 + num5) / 5

print(f"Aritmeetiline keskmine on: {kesk}")


#6 harjutus

aeg = float(input("Mitu tundi kulus soiduks? "))
teepikkus = float(input("Mitu kilomeetrit soitsid? "))
kiirus = teepikkus / aeg # Неправильная последовательность действий. Расстояние делиться на время, а не наоборот
print("Sinu kiirus oli " + str(kiirus) + " km/h")

#5 harjutus
from math import *

N = float(input("Sisesta ristkuliku pikkus (m): "))
M = float(input("Sisesta ristkuliku laius (m): "))

diagonaal = sqrt(N**2 + M**2)

print(f"Ristkuliku diagonaali pikkus on {diagonaal} meetrit.")


#4 harjutus
from math import *

C = int(input("Mis on puu pikkus: "))
print(f"Puu labimoot on {C / pi}")

#3 harjutus
from random import *

komm = randint(10, 100)
print(f"Laua peal on {komm}")
taha = int(input("Kui palju kommid sa tahad vota?: "))
print(f"Laua peal on jaanud {komm-taha}")

#2 harjutus

vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_kaib_koolis = True

print(f"Muutuja {vanus} on {type(vanus)}")
print(f"Muutuja {eesnimi} on {type(eesnimi)}")
print(f"Muutuja {pikkus} on {type(pikkus)}")
print(f"Muutuja {kas_kaib_koolis} on {type(kas_kaib_koolis)}")

#1 harjutus

print("Tere, maailm")

nimi = input("Tere kuidas sinu nimi?: ").capitalize()
v = int(input("Kui vana sa oled?: "))

print(f"Tere maailm! Tere {nimi} ! Sinu on {v} aastat vana")