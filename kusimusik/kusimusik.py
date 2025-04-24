import random
import datetime
import smtplib
import ssl
from email.message import EmailMessage

kus_vas = {
    "Mis on Python?": "programmeerimiskeel",
    "Mis värvi on lumi?": "valge",
    "Kui palju planeete on päikesesüsteemis?": "8",
    "Kes kirjutas 'Sõda ja rahu'?": "Lev Tolstoi",
    "Mis on Prantsusmaa pealinn?": "Pariis",
    "Mis on maailma kõrgeim mägi?": "Everest",
    "Kes oli esimene inimene Kuu peal?": "Neil Armstrong",
    "Kuidas kutsutakse peategelast romaanis '1984'?": "Winston Smith"
}

koik_vastajad = []
edukad = []

KUSIMUSED_FAIL = "kusimused_vastu.txt"
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_FROM = "nikiforovnikita08@gmail.com"
EMAIL_PASSWORD = 'yksj yudm flgi nyqx'
EMPLOYER_EMAIL = "tootaja@firma.ee"

def lisa_kusimus():
    print("\nUue küsimuse lisamine:")
    kusimus = input("Sisesta uus küsimus: ").strip()
    
    if not kusimus:
        print("Küsimus ei tohi olla tühi!")
        return
        
    if kusimus in kus_vas:
        print("See küsimus on juba olemas!")
        return
    
    vastus = input("Sisesta õige vastus: ").strip()
    if not vastus:
        print("Vastus ei tohi olla tühi!")
        return
    
    with open(KUSIMUSED_FAIL, "a", encoding="utf-8") as f:
        f.write(f"{kusimus}:{vastus}\n")
    
    kus_vas[kusimus] = vastus
    print("Küsimus lisatud edukalt!")

def saada_kiri(kellele, pealkiri, sisu):
    msg = EmailMessage()
    msg['Subject'] = pealkiri
    msg['From'] = EMAIL_FROM
    msg['To'] = kellele
    msg.set_content(sisu)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(EMAIL_FROM, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email saadetud edukalt aadressile {kellele}")
        return True
    except Exception as e:
        print(f"Emaili saatmine ebaõnnestus: {e}")
        return False

def saada_tulemus_kasutajale(nimi, email, oiged, kokku, edukas):
    pealkiri = "Teie testi tulemused"
    
    if edukas:
        sisu = f"""Tere, {nimi}!

Õigete vastuste arv: {oiged} ({oiged}/{kokku}).
Te olete testi edukalt läbinud.

Parimate soovidega,
Küsitluse meeskond"""
        edukad.append((nimi, f"{oiged}/{kokku}"))
    else:
        sisu = f"""Tere, {nimi}!

Õigete vastuste arv: {oiged} ({oiged}/{kokku}).
Kahjuks te ei läbinud testi.

"""
    
    return saada_kiri(email, pealkiri, sisu)

def saada_aruanne_tööandjale():
    try:
        with open("koik.txt", "r", encoding="utf-8") as f:
            koik_sisu = f.readlines()

        if not koik_sisu:
            print("Fail koik.txt on tühi")
            return False

        nimed = {
            rida.split("❘")[1].strip()
            for rida in koik_sisu
            if "❘" in rida and len(rida.split("❘")) > 1
        }

        if len(nimed) < 10:
            print(f"Aruannet ei saadeta — leiti ainult {len(nimed)} unikaalset nime.")
            return False

        pealkiri = "Küsitluse tulemuste aruanne"
        sisu = f"""Tere!

Kõikide testis osalenud tulemused:

{''.join(koik_sisu)}

"""
        tulemus = saada_kiri(EMPLOYER_EMAIL, pealkiri, sisu)
        
        if tulemus:
            with open("koik.txt", "w", encoding="utf-8") as f:
                f.write("")
            print("Fail koik.txt on tühjendatud.")
        
        return tulemus

    except Exception as e:
        print(f"Aruande koostamine ebaõnnestus: {e}")
        return False


def loo_email(nimi):
    qwe = nimi.split()
    if len(qwe) == 2:
        return f"{qwe[0].lower()}@example.com"
    else:
        return f"{qwe[0].lower()}@example.com"

def mangu():
    oige_kus = 0

    while True:
        nimi = input("Sisestage oma nimi: ").strip()
        pere_nimi = input("Sisestage oma perekonnanimi: ").strip()

        if len(nimi) < 2 or len(pere_nimi) < 2:
            print("Nimi ja perekonnanimi peavad olema vähemalt 2 tähemärki pikad!")
            continue

        täisnimi = f"{nimi} {pere_nimi}"

        with open("koik.txt", "r", encoding="utf-8") as f:
            koik_sisu = f.readlines()

        unikaalsed_nimed = set()

        for rida in koik_sisu:
            if "❘" in rida:
                osad = rida.split("❘")
                if len(osad) > 1:
                    nimi_failist = osad[1].strip()
                    unikaalsed_nimed.add(nimi_failist)

        if täisnimi in unikaalsed_nimed:
            print("See nimi on juba registreeritud. Palun sisestage teine nimi.")
            continue

        break

    max_kus = len(kus_vas)
    n = int(input(f"Kui palju küsimusi soovite esitada? (max {max_kus}): "))

    if n < 1 or n > max_kus:
        print("Palun sisestage korrektne arv küsimusi.")
        return
        
    random_questions = random.sample(list(kus_vas.keys()), n)

    for question in random_questions:
        print(f"\nKüsimus: {question}")
        user_answer = input("Teie vastus: ")
        
        if user_answer.strip().lower() == kus_vas[question].lower():
            print("Õige vastus!")
            oige_kus += 1
        else:
            print(f"Vale vastus! Õige vastus oleks olnud: {kus_vas[question]}")

    print(f"\n{täisnimi}, teie tulemus: {oige_kus}/{n} õiget vastust")

    email = loo_email(täisnimi)
    
    with open("koik.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.date.today()} ❘ {täisnimi} ❘ {oige_kus}/{n} ❘ {email}\n")

    edukas = oige_kus > n // 2
    if edukas:
        with open("oiged.txt", "a", encoding="utf-8") as f:
            f.write(f"{täisnimi} ❘ {oige_kus} õige, kokku oli {n}\n")
    else:
        with open("valed.txt", "a", encoding="utf-8") as f:
            f.write(f"{täisnimi} ❘ {n - oige_kus} vale, kokku oli {n}\n")

    saada_tulemus_kasutajale(täisnimi, email, oige_kus, n, edukas)
    saada_aruanne_tööandjale()
    sort_oiged()
    sort_vale()

def extract_name(line):
    return line.split(" ❘ ")[0].strip().lower()

def sort_vale():
    try:
        with open("valed.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        lines.sort(key=extract_name)

        with open("valed.txt", "w", encoding="utf-8") as f:
            f.writelines(lines)
    except:
        print("Faili 'valed.txt' pole olemas!")

def extract_score(line):
    return int(line.split(" ❘ ")[1].split("õige")[0].strip())

def sort_oiged():
    try:
        with open("oiged.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        lines.sort(key=extract_score, reverse=True)
        
        with open("oiged.txt", "w", encoding="utf-8") as f:
            f.writelines(lines)
    except:
        print("Faili 'oiged.txt' pole olemas!")


def genereeri_andmed(arv=10):
    """Genereerib testandmed ja täidab kõik failid"""
    eesnimed = ["Mari", "Jaan", "Kati", "Tõnu", "Liisa", "Peeter", "Anna", "Martin"]
    perenimed = ["Tamm", "Saar", "Kask", "Sepp", "Mets", "Kukk", "Pärn", "Rebane"]
    tulemused = []

    for i in range(arv):
        nimi = f"{random.choice(eesnimed)} {random.choice(perenimed)}"
        kokku = random.randint(5, 10)
        oiged = random.randint(0, kokku)
        email = f"{nimi.split()[0].lower()}@example.com"
        tulemused.append((nimi, oiged, kokku, email))

        with open("koik.txt", "a", encoding="utf-8") as f:
            f.write(f"{datetime.date.today()} ❘ {nimi} ❘ {oiged}/{kokku} ❘ {email}\n")

        if oiged > kokku // 2:
            with open("oiged.txt", "a", encoding="utf-8") as f:
                f.write(f"{nimi} ❘ {oiged} õige, kokku oli {kokku}\n")
        else:
            with open("valed.txt", "a", encoding="utf-8") as f:
                f.write(f"{nimi} ❘ {kokku - oiged} vale, kokku oli {kokku}\n")

    sort_oiged()
    sort_vale()
    
    print(f"Genereeriti {arv} testandmet. Failid on täidetud!")

while True:
    print("\n=== MENÜÜ ===")
    print("1. Alusta testi")
    print("2. Lisa küsimus")
    print("3. Näita tulemusi ja välju")
    
    valik = input("Valik: ").strip()
    
    if valik == "1":
        mangu()
    elif valik == "2":
        lisa_kusimus()
    elif valik == "3":
        print("\n=== EDUKAD VASTANUD ===")
        for i, (nimi, tulemus) in enumerate(edukad, 1):
            print(f"{i}. {nimi}: {tulemus}")
        print("\nTulemused saadetud e-posti aadressidele.")
        break
    elif valik == "4": 
        try:
            arv = int(input("Kui palju testandmeid genereerida?: "))
            genereeri_andmed(arv)
        except ValueError:
            print("Palun sisesta number!")
    else:
        print("Vale valik! Palun proovige uuesti.")
