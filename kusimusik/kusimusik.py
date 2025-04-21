import random
import datetime

kus_vas = {
    "Mis on Python?": "programmeermiskeel",
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
ebaedukad = []

def loo_email(nimi):
    qwe = nimi.split()
    if len(qwe) == 2:
        return f"{qwe[0].lower()}@example.com"
    else:
        return f"{qwe[0].lower()}@example.com"

def check_answer(question, user_answer):
    oige_vastus = kus_vas[question]
    return user_answer.strip().lower() == oige_vastus.lower()

def mangu():
    oige_kus = 0
    nimi = input("Sisestage oma nimi (eesnimi perekonnanimi): ").strip()
    max_kus = len(kus_vas)
    n = int(input(f"Kui palju küsimusi soovite esitada? (max {max_kus}): "))

    if n < 1 or n > max_kus:
        print("Palun sisestage korrektne arv küsimusi.")
        return

    random_questions = random.sample(list(kus_vas.keys()), n)

    for question in random_questions:
        print(f"{nimi}, {question}")
        user_answer = input("Teie vastus: ")

        if check_answer(question, user_answer):
            print("Õige vastus!")
            oige_kus += 1
        else:
            print("Vale vastus!")

    print(f"\n{nimi}, teie tulemus: {oige_kus} õiget vastust {n} küsimusest.")

    if oige_kus > n // 2:
        print("Test on edukas!")
        edukad.append((nimi, oige_kus))
    else:
        print("Test ei ole edukas!")
        ebaedukad.append((nimi, oige_kus))

    email = loo_email(nimi)
    koik_vastajad.append((nimi, email, oige_kus))

    #koik.txt
    with open("koik.txt", "a", encoding="utf-8") as file:
        file.write(f"{datetime.date.today()} ❘ {nimi} ❘ {oige_kus} / {n} ❘ {email}\n")

    # oiged.txt
    with open("oiged.txt", "w", encoding="utf-8") as f:
        # Сортируем по второму элементу кортежа (оценке)
        for name, score in sorted(edukad, reverse=True):
            f.write(f"{name} ❘ {score} \n")

    # valed.txt
    with open("valed.txt", "w", encoding="utf-8") as f:
        f.write(f"{nimi} ❘ {n - oige_kus} \n")

mangu()
