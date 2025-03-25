import random

sportlased = []
tulemused = []

def random_name(n:int) -> int:
    names = ["Jaan", "Kalle", "Mati", "Toomas", "Jüri", "Karl", "Joosep", "Kaido"]
    for o in range (n):
        sportlased.append(random.choice(names))

def random_number() -> None:
    for x in range(3):
        return random.randint(1, 100)

def menu(sportlased, tulemused) -> None:
    print("\nMenüü:")
    print("1. Saate teada n parimat tulemust")
    print("2. Sorteerige loend tulemuste kasvavas järjekorras. Kuva sportlased, nende tulemused ja kohad.")
    print("3. Sisestage ühe või mitme sportlase nimi ja näidake nende tulemust")
    print("4. Diskvalifitseeri (nimekirjast eemaldamine) sportlased, kelle tulemused on määratud kriteeriumist kehvemad")
    print("5. Teie enda valik")
    print("6. Välju")

    choice1 = int(input(": "))
    if choice1 == 1: #Saate teada n parimat tulemust
        n = int(input("Sisestage parimate sportlaste arv: "))
        if n > len(tulemused):
            print("Parimate arv ületab tulemuste arvu. Kuvan kõik saadaolevad tulemused.")
        n = len(tulemused)
        parimad = sorted(tulemused, reverse=True)
        for x in range(n):
            print(f"{x+1}. koht: {parimad[x]}")

    elif choice1 == 2: #Sorteerige loend tulemuste kasvavas järjekorras. Kuva sportlased, nende tulemused ja kohad.
        sorteeritud = sorted(tulemused)
        for i in range(len(sorteeritud)):
            print(f"{i+1}. koht: {sorteeritud[i]}")

    elif choice1 == 3: #Sisestage ühe või mitme sportlase nimi ja näidake nende tulemust
        nimi = input("Sisestage sportlase nimi: ")
        if nimi in sportlased:
            print(f"{nimi} tulemus on {tulemused[sportlased.index(nimi)]}")
        else:
            print("Sellist sportlast ei ole")

    elif choice1 == 4: #Diskvalifitseeri (nimekirjast eemaldamine) sportlased, kelle tulemused on määratud kriteeriumist kehvemad
        kriteerium = int(input("Sisestage kriteerium: "))
        for i in range(len(tulemused)):
            if tulemused[i] < kriteerium:
                sportlased.pop(i)
                tulemused.pop(i)

    elif choice1 == 5: #Teie enda valik
        valik = input("Sisestage sportlase nimi: ")
        if valik in sportlased:
            print(f"{valik} tulemus on {tulemused[sportlased.index(valik)]}")
        else:
            print("Sellist sportlast ei ole")

    elif choice1 == 6: #Välju
        return
    elif choice1 == 7:
        print(sportlased)
        print(tulemused)

    else:
        print("Vale valik, proovige uuesti.")


def sport() -> None:
    """
    """
    sportlase = int(input("Sisesta sportlaste arv: "))
    random_number(sportlase)
    # for i in range(sportlase):
    #     sportlane = input("Sisesta sportlase nimi: ")
    #     sportlased.append(sportlane)

    tulemus = random_number()
    tulemused.append(tulemus)
    telimus_max = max(tulemused)

    menu(sportlased, tulemused)