#V5 3
from time import sleep

for x in range(20):
    print(f"sooritab eksamit {x+1}. õpilane")
    for y in range(3):
        print(f"{y+1}. eksam")

#V4 2
vastus = 0
try:
    P = int(input("Mitu korda kordame?: "))
    while P > 0:
        arv = float(input("Sisestav arv: "))
        if arv < 0:
            vastus += arv
        P -= 1
    print(f"Summa on {vastus}")
except ValueError:
    print("Viga! Sisesta korrektne arv.")

#V1 4
try:
    kokku = int(input("Sisestaja kokku: "))
    panni_maht = int(input("Panni maht: "))
    aeg = 1

    lahenemine = kokku // panni_maht
    jaak = kokku % panni_maht
    if jaak > 0:
        lahenemine += 1
    print(f"Kokku on {lahenemine} panni")

    for x in range(lahenemine):
        if jaak > 0 and x == lahenemine - 1:
            print(f"Panni peale on {jaak} kotletit")
        else:
            print(f"Panni peale on {panni_maht} kotletid")
        print(f"{x+1}. lahenemine. esimene pool")
        sleep(aeg)
        print("Ümberpööramine")
        print(f"{x+1}. lahenemine. teine pool")
        sleep(aeg)
        print("Valmis")

    print("Kõik valmis")
except ValueError:
    print("Viga! Sisesta korrektne arv.")

#V3 1
try:
    Q = int(input("Mitu arvu soovid sisestada?: "))
    pos = 0
    for i in range(Q):
        arv = float(input(f"Sisesta {i + 1}. arv: "))
        if arv > 0:
            pos += arv
    print(f"Positiivsete arvude summa: {pos}")
except ValueError:
    print("Viga! Sisesta korrektne arv.")

#V3 2
try:
    Y = float(input("Sisesta algne summa: "))
    Z = float(input("Sisesta aastane intress: "))
    H = int(input("Sisesta aastate arv: "))
    final = Y * (1 + Z / 100) ** H
    print(f"Summa {H} aasta pärast: {final:.2f} dollarit")
except ValueError:
    print("Viga! Sisesta korrektne arv.")
