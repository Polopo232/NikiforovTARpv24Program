#V5 3

from time import sleep


for x in range (20):
    print(f"sooritab eksamit {x+1}. opilane")
    for y in range (3):
        print(f"{y+1}. eksam")

#V4 2
vastus = 0
P = int(input("Mitu korda kordame?: "))
while True:
    arv = float(input("Sesitav arv: "))
    if arv<0:
        vastus += arv
    P -= 1
    if P == 0:
        break
print(f"Summa on {vastus}")

#V1 4
kokku = int(input("Sesitaja kokku: "))
panni_maht = int(input("Panni maht: "))
aeg = 1

lahenemine = kokku // panni_maht
jaak = kokku % panni_maht
if jaak > 0:
    lahendamine += 1
print(f"Kokku on {lahendamine} panni")
for x in range (lahendamine):
    if jaak > 0 and x == lahendamine - 1:
        print(f"Panni peale on {jaak} kotletid")
    else:
        print(f"Panni peale on {panni_maht} kotletid")
    print(f"{x+1}. laheniane. eesimene pool")
    sleep(aeg)
    print("Ümberpööramine")
    print(f"{x+1}. laheniane. teine pool")
    sleep(aeg)
    print("Valmis")
    print("Kõik valmis")
    
#V3 1
Q = int(input("Mitu arvu soovid sisestada?: "))
pos = 0
for i in range(Q):
    arv = float(input(f"Sisesta {i + 1}. arv: "))
    if arv > 0:
        pos += arv
print(f"Positiivsete arvude summa: {pos}")

#V3 2

Y = float(input("Sisesta algne summa: "))
Z = float(input("Sisesta aastane intress: "))
H = int(input("Sisesta aastate arv: "))
final = Y * (1 + Z / 100) ** H
print(f"Summa {H} aasta pärast: {final} dollarit")
