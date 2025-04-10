import random 
import pyttsx3

sonad = [
    {'est': 'koer', 'rus': 'собака', 'eng': 'dog'},
    {'est': 'kass', 'rus': 'кошка', 'eng': 'cat'},
    {'est': 'maja', 'rus': 'дом', 'eng': 'house'},
    {'est': 'auto', 'rus': 'машина', 'eng': 'car'},
    {'est': 'päike', 'rus': 'солнце', 'eng': 'sun'}
]

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
    if uus_est.isalpha() and uus_rus.isalpha() and uus_eng.isalpha == True:
        sonad.append({'est': uus_est, 'rus': uus_rus, 'eng': uus_eng})
        print("Uus sõna on lisatud!")
    else:
        print("Teie kirjes on numbreid, asendage need tähtedega!")

def otsi_sona(sona:str):
    for kirje in sonad:
        if sona in kirje.values():
            for keel, s in kirje.items():
                print(f"{keel} : {s}")

def paranda_sona():
    try:
        sona = kysi_kasutajalt_sisestus("Sona : ")
    except:
        print("Viga!")
    for kirje in sonad:
        if sona in kirje.values():
            for keel, s in kirje.items():
                try:
                    sona_est = kysi_kasutajalt_sisestus("Paranda : ").lower()
                    sona_rus = kysi_kasutajalt_sisestus("Paranda : ").lower()
                    sona_eng = kysi_kasutajalt_sisestus("Paranda : ").lower()
                except:
                    print("Viga!")
                if sona_est != "":
                    if sona_est.isdigit() == True:
                        kirje["est"] = sona_est
                if sona_rus != "":
                    if sona_rus.isdigit() == True:
                        kirje["rus"] = sona_rus
                if sona_eng != "":
                    if sona_eng.isdigit() == True:
                        kirje["eng"] = sona_eng

def kuva_sona():
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
    except:
        print("Viga!")
        return None
    if valik in [1, 2, 3]:
        return keeled[valik-1]
    else:
        print("Vale valik!")
        return None
oige = 0
vale = 0
def testi_teadmisi():
    global oige, vale
    valik = vali_keelt_suund()
    valik1 = random.choice(["est", "rus", "eng"])
    while valik1 == valik:
        valik1 = random.choice(["est", "rus", "eng"])
    if valik not in ["est", "rus", "eng"]:
        print("Vale valik!")
        return
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

def text_to_speech():
    kuva_sona()
    valik = vali_keelt_suund()
    print("Mis keelde tõlge tehakse: ")
    valik1 = vali_keelt_suund
    for kirje in sonad:
        speech = f"{kirje[valik]} - {kirje[valik1]}"
        print(f"{kirje[valik]} - {kirje[valik1]}")
        volume = float(input("Sisestage helitugevus"))
        if volume.isdigit == True:
            engine = pyttsx3.init()

            engine.setProperty('rate', 150)
            engine.setProperty('volume', volume)

            engine.say(speech)
            engine.runAndWait()

def kysi_kasutajalt_sisestus():
    while True:
        sona = input("Sisesta sõna: ").strip().lower()
        if len(sona) > 1:
            return sona

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
    valjasta_tervitus()
    choice = input("Sisesta valik: ")
    if choice == "1":
        lisa_sona(sonad)
    elif choice == "2":
        sona = kysi_kasutajalt_sisestus("Sisesta otsitav sõna: ")
        otsi_sona(sona)
    elif choice == "3":
        paranda_sona()
    elif choice == "4":
        kuva_sona()
    elif choice == "5":
        vali_keelt_suund()
    elif choice == "6":
        testi_teadmisi()
    elif choice == "7":
        kuva_tulemus()
    elif choice == "8":
        text_to_speech()
    elif choice == "0":
        print("Välja!")
        exit()
    else:
        print("Vale valik!")

kuva_menuu()