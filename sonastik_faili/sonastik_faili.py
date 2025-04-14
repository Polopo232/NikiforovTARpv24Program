import random
import pyttsx3

def loe_fail():
    sonad = []
    with open("sonastik.txt", "r", encoding="utf-8-sig") as fail:
        for line in fail:
            sona = line.strip().split("-")
            if len(sona) == 3:
                sonad.append({'est': sona[0], 'rus': sona[1], 'eng': sona[2]})
    return sonad
def salvesta_fail(sonad):
    with open("sonastik.txt", "w", encoding="utf-8-sig") as fail:
        for kirje in sonad:
            fail.write(f"{kirje['est']}-{kirje['rus']}-{kirje['eng']}\n")
    print("Sõnad on salvestatud faili sonastik.txt")

def tolkija(sonad, allikas, siht, sona):
    for kirje in sonad:
        if kirje[allikas] == sona.lower():
            return kirje[siht]
    return "Sõna ei leitud!"

def lisa_sona(sonad):
    print("Lisame uue sõna sõnastikku!")
    try:
        uus_est = kysi_kasutajalt_sisestus("Sisesta sõna eesti keeles: ").strip().lower()
        uus_rus = kysi_kasutajalt_sisestus("Sisesta sõna vene keeles: ").strip().lower()
        uus_eng = kysi_kasutajalt_sisestus("Sisesta sõna inglise keeles: ").strip().lower()
    except:
        print("Viga!")
    if uus_est.isalpha() and uus_rus.isalpha() and uus_eng.isalpha():
        sonad.append({'est': uus_est, 'rus': uus_rus, 'eng': uus_eng})
        print("Uus sõna on lisatud!")
        salvesta_fail(sonad)
    else:
        print("Teie kirjes on numbreid, asendage need tähtedega!")

def otsi_sona(sonad, sona:str):
    for kirje in sonad:
        if sona in kirje.values():
            for keel, s in kirje.items():
                print(f"{keel} : {s}")

def paranda_sona(sonad):
    try:
        sona = kysi_kasutajalt_sisestus("Sona: ").strip().lower()
    except:
        print("Viga!")
    for kirje in sonad:
        if sona in kirje.values():
            print("Leitud sõna! Paranda:")
            try:
                sona_est = kysi_kasutajalt_sisestus("Paranda eesti keeles: ").strip().lower()
                sona_rus = kysi_kasutajalt_sisestus("Paranda vene keeles: ").strip().lower()
                sona_eng = kysi_kasutajalt_sisestus("Paranda inglise keeles: ").strip().lower()
            except:
                print("Viga!")
                return
            if sona_est != "":
                kirje["est"] = sona_est
            if sona_rus != "":
                kirje["rus"] = sona_rus
            if sona_eng != "":
                kirje["eng"] = sona_eng
    salvesta_fail(sonad)

def kuva_sona(sonad):
    for kirje in sonad:
        for keel, s in kirje.items():
            print(f"{keel} : {s}")
        print("----------")

def vali_keelt_suund():
    print("Vali keelt:")
    print("1. Eesti keel")
    print("2. Vene keel")
    print("3. Inglise keel")
    keeled = ["est", "rus", "eng"]
    try:
        valik = int(input("Sisesta valik (1-3): "))
        if valik in [1, 2, 3]:
            return keeled[valik - 1]
        else:
            print("Vale valik!")
            return None
    except ValueError:
        print("Viga! Sisesta number (1-3).")
        return None

oige = 0
vale = 0

def testi_teadmisi(sonad):
    global oige, vale
    valik = vali_keelt_suund()
    if not valik:
        return
    valik1 = random.choice(["est", "rus", "eng"])
    while valik1 == valik:
        valik1 = random.choice(["est", "rus", "eng"])
    print(f"Valitud keel: {valik}, Tõlkimiseks keel: {valik1}")
    for kirje in sonad:
        print(f"Sõna: {kirje[valik]}")
        a = kysi_kasutajalt_sisestus(f"Tõlgi {valik1}: ")
        if kirje[valik1] == a:
            print("ÕIGE!")
            oige += 1
        else:
            print(f"Vale! Õige vastus: {kirje[valik1]}")
            vale += 1
    print("Testi lõpp! Kui sa tahad näitama tulemus sisesta 7")

def kuva_tulemus():
    print(f"Õigeid vastuseid: {oige}")
    print(f"Valeid vastuseid: {vale}")
    print(f"Protsent: {oige / (oige + vale) * 100}%")

def text_to_speech(sonad):
    kuva_sona(sonad)
    valik = vali_keelt_suund()
    if not valik:
        return
    print("Mis keelde tõlge tehakse: ")
    valik1 = vali_keelt_suund()
    for kirje in sonad:
        speech = f"{kirje[valik]} - {kirje[valik1]}"
        print(f"{kirje[valik]} - {kirje[valik1]}")
        try:
            volume = float(input("Sisestage helitugevus: "))
        except ValueError:
            print("Vigane helitugevus!")
            continue
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', volume)
        engine.say(speech)
        engine.runAndWait()

def kysi_kasutajalt_sisestus(sonad):
    while True:
        user_input = input(sonad).strip().lower()
        if len(user_input) > 1:
            return user_input

def valjasta_tervitus():
    print("Tere tulemast sõnastikku!")
    print("Sõnastik toetab kolme keelt: eesti, vene ja inglise.")
    print("Valige tegevus menüüst:")
    print("1. Lisa sõna")
    print("2. Otsi sõna")
    print("3. Paranda sõna")
    print("4. Kuva sõnad")
    print("5. Vali keelt suund")
    print("6. Testi teadmisi")
    print("7. Kuva tulemused")
    print("8. Kuula sõnu")
    print("0. Välja")

def kuva_menuu():
    sonad = loe_fail()
    while True:
        valjasta_tervitus()
        choice = input("Sisesta valik: ")
        if choice == "1":
            lisa_sona(sonad)
        elif choice == "2":
            sona = kysi_kasutajalt_sisestus("Sisesta otsitav sõna: ")
            otsi_sona(sonad, sona)
        elif choice == "3":
            paranda_sona(sonad)
        elif choice == "4":
            kuva_sona(sonad)
        elif choice == "5":
            vali_keelt_suund()
        elif choice == "6":
            testi_teadmisi(sonad)
        elif choice == "7":
            kuva_tulemus()
        elif choice == "8":
            text_to_speech(sonad)
        elif choice == "0":
            print("Välja!")
            break
        else:
            print("Vale valik!")

kuva_menuu()