import random

sportlased = []
tulemused = []

def random_name(n) -> None:
    """
    Loob juhuslikud sportlaste nimed ja lisab need nimekirja sportlased.
    """
    names = ["Jaan", "Kalle", "Mati", "Toomas", "Jüri", "Karl", "Joosep", "Kaido"]
    for i in range(n):
        valik = random.choice(names)
        sportlased.append(valik)

def random_numbers(n) -> None:
    """
    Loob juhuslikud tulemused ja lisab need nimekirja tulemused.
    """
    for i in range(n):
        tulemused.append(random.randint(1, 100))

def show_best_results() -> None:
    """
    Sorteerib tulemused parimatest halvimateks ja kuvab need koos sportlaste nimedega.
    """
    sport_cop = []
    for i in range(len(tulemused)):
        sport_cop.append((tulemused[i], sportlased[i]))
    sport_cop.sort(reverse=True)
    for i in range(len(sport_cop)):
        print(f"{i+1}. {sport_cop[i][1]}: {sport_cop[i][0]}")

def sort_results() -> None:
    """
    Sorteerib tulemused halvimatest parimateni ja kuvab need koos sportlaste nimedega.
    """
    andmed = []
    for i in range(len(tulemused)):
        andmed.append((tulemused[i], sportlased[i]))
    andmed.sort()
    for i in range(len(andmed)):
        print(f"{i+1}. {andmed[i][1]}: {andmed[i][0]}")

def ots_athlete() -> None:
    """
    Otsib ja kuvab konkreetse sportlase tulemuse tema nime alusel.
    """
    nimi = input("Sisestage sportlase nimi: ")
    for i in range(len(sportlased)):
        if sportlased[i] == nimi:
            print(f"{nimi} tulemus on {tulemused[i]}")

def disqualify_athletes() -> None:
    """
    Eemaldab nimekirjadest sportlased ja nende tulemused, kui need on allpool määratud kriteeriumi.
    """
    try:
        del_person = int(input("Sisestage kriteerium: "))
        del_index = []

        for i in range(len(tulemused)):
            if tulemused[i] <= del_person:
                del_index.append(i)

        if del_index:
            for index in sorted(del_index, reverse=True):
                del sportlased[index]
                del tulemused[index]
            print("Diskvalifitseerimine lõpetatud.")
        else:
            print("Ei leitud sportlasi.")
    except :
        print("Vigane sisend!")

def show_all_athletes() -> None:
    """
    Kuvab kõigi sportlaste nimekirja ja nende tulemused.
    """
    for i in range(len(sportlased)):
        print(f"{sportlased[i]}: {tulemused[i]}")

def menu() -> None:
    """
    Kuvab tegevuste menüü ja võimaldab valida tegevuse.
    """
    while True:
        print("\nValige tegevus:")
        print("1. Näita parimaid tulemusi")
        print("2. Sorteeri tulemused")
        print("3. Otsi sportlast")
        print("4. Diskvalifitseeri")
        print("5. Näita kõiki")
        print("6. Välju")
        
        valik = input("Teie valik: ")
        
        if valik == "1":
            show_best_results()
        elif valik == "2":
            sort_results()
        elif valik == "3":
            ots_athlete()
        elif valik == "4":
            disqualify_athletes()
        elif valik == "5":
            show_all_athletes()
        elif valik == "6":
            print("Head aega!")
            break
        else:
            print("Vale valik!")    