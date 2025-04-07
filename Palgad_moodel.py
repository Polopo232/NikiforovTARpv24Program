palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
from random import *

def add_palgad()-> None:
    """
    Lisage nimekirjadesse töötajate nimed ja palgad.
    """
    try:
        u_choice = int(input("1-ise ; 2-auto: "))
        palju = int(input("Sisesta töötajate arv: "))
        if palju <= 0:
            print("Palun sisestage kehtiv töötajate arv.")
    except:
        print("Viga!")
    else:
        if u_choice == 1:
            for i in range(palju):
                nimi = input("Sisesta töötaja nimi: ")
                if nimi.isalpha() == False:
                    print("Palun sisestage kehtiv nimi.")
                    break
                else:
                    inimesed.append(nimi)
                try:
                    palk = int(input("Sisesta töötaja palk: "))
                    if palk < 0:
                        print("Palun sisestage kehtiv palk.")
                        break
                    else:
                        palgad.append(palk)
                    print(f"Töötaja {nimi} palk on lisatud.")
                except:
                    print("Palun sisestage kehtiv palk.")
                    break
        elif u_choice == 2:
            for x in range(palju):
                palk_auto = randint(20, 100000)
                palgad.append(palk_auto)
                nimi = ["Toomas", "John", "Martha", "Anna", "Katrin", "Albert"]
                r_nimi = choice(nimi)
                inimesed.append(r_nimi)
                print(f"Töötaja {r_nimi} palk on lisatud.")
        else:
            print("Viga!")

def del_palgad()-> None:
    """
    Kustutage nimekirjadest töötajate nimed ja palgad.
    """
    while True:
        try:
            nimi = input("Sisestage töötaja nimi: ").capitalize()
            if nimi in inimesed:
                for j in range(len(inimesed)):
                    if inimesed[j] == nimi:
                        palga = palgad[j]
                        print(f"Töötaja {nimi} palk on {palga}.")
            palga = int(input("Sisestage töötaja palk: "))
            if palga in palgad:
                index = palgad.index(palga)
                palgad.pop(index)
                inimesed.pop(index)
                print(f"Töötaja {nimi} palk on kustutatud.")
            else:
                print("Töötajat ei leitud.")
        except:
            print("Palun sisestage kehtiv number.")
        else:
            break

def best_palgad()-> None:
    """
    Leidke parimad palgad ja neile vastavad töötajad.
    """
    palg_cop = []
    for i in range(len(palgad)):
        palg_cop.append((palgad[i], inimesed[i]))
    palg_cop.sort(reverse=True)
    for i in range(len(palg_cop)):
        print(f"{i+1}. {palg_cop[i][1]}: {palg_cop[i][0]}")

def worst_palgad()-> None:
    """
    Leidke halvimad palgad ja neile vastavad töötajad.
    """
    palg_cop = []
    for i in range(len(palgad)):
        palg_cop.append((palgad[i], inimesed[i]))
    palg_cop.sort(reverse=False)
    for i in range(len(palg_cop)):
        print(f"{i+1}. {palg_cop[i][1]}: {palg_cop[i][0]}")

def palga_sort()-> None:
    """
    Sorteeri palgad kasutaja sisendi alusel.
    """
    try:
        choice1 = int(input("Kas soovite palka sorteerida? (1 - 1-100, 0 - 100-1): "))
        if choice1 == 1:
            best_palgad()
        elif choice1 == 2:
            worst_palgad()
    except :
        print("Viga!")

def similar_palga()-> None:
    """
    Leidke sarnased palgad ja neile vastavad töötajad.
    """

    for j in range(len(palgad)):
        for i in range(len(palgad)):
            if palgad[j] == palgad[i] and j != i:
                print(f"{inimesed[j]}:{palgad[j]} sarnased {inimesed[i]}:{palgad[i]}")

def palga_otsing()-> None:
    """
    Otsige üles konkreetne palk ja sellele vastav töötaja.
    """
    try:
        nimi = input("Sisestage inimesed nimi: ")
        for i in range(len(inimesed)):
            if inimesed[i] == nimi:
                print(f"{nimi} palgad on {palgad[i]}")
    except:
        print("Viga!")
def palga_show()-> None:
    """
    Näidake konkreetse töötaja töötasu.
    """
    try:
        palga_wr = int(input("Sisestage palga: "))
        choice2 = int(input("1 - Suurem ; 2 - Väiksem: "))
        if choice2 == 1:
            best_palgad()
        elif choice2 == 2:
            worst_palgad()
    except:
        print("Viga!")

def top()-> None:
    """
    Kuva 5 parimat kõrgeimat või madalaimat palka kasutaja sisendi põhjal.
    """
    top_choice = int(input("1 - vaeseimad ; 0 - rikkamad: "))
    if top_choice == 0:
        palg_cop = []
        for i in range(len(palgad)):
            palg_cop.append((palgad[i], inimesed[i]))
        palg_cop.sort(reverse=True)
        for i in range(5):
            print(f"{i+1}. {palg_cop[i][1]}: {palg_cop[i][0]}")

    elif top_choice == 1:
        palg_cop = []
        for i in range(len(palgad)):
            palg_cop.append((palgad[i], inimesed[i]))
        palg_cop.sort(reverse=False)
        for i in range(5):
            print(f"{i+1}. {palg_cop[i][1]}: {palg_cop[i][0]}")
    else:
        print("Viga!")

def min_palk() -> None:
    """
    Funktsioon otsib ja eemaldab keskmisest madalama palgaga töötajaid.
    """
    
    kesk_palga = int(input("Sisestage keskmine palk: "))

    for i in range(len(palgad)-1, 0, -1):
        if palgad[i] <= kesk_palga:
            print(f"{inimesed[i]} palk on {palgad[i]} ja on väiksem kui {kesk_palga}")
            palgad.pop(i)
            inimesed.pop(i)

        


def menu():
    while True:
        print("1. Lisa palk")
        print("2. Kustuta palk")
        print("3. Parimad palgad")
        print("4. Halvimad palgad")
        print("5. Palga sorteerimine")
        print("6. Sarnased palgad")
        print("7. Otsi palk")
        print("8. Näita palka")
        print("9. Top 5")
        print("10. Kasutamine minimaalne palk")
        print("0. Välja")
        choice = int(input("Vali tegevus: "))
        if choice == 1:
            add_palgad()
        elif choice == 2:
            del_palgad()
        elif choice == 3:
            best_palgad()
        elif choice == 4:
            worst_palgad()
        elif choice == 5:
            palga_sort()
        elif choice == 6:
            similar_palga()
        elif choice == 7:
            palga_otsing()
        elif choice == 8:
            palga_show()
        elif choice == 9:
            top()
        elif choice == 10:
            min_palk()
        elif choice == 100:
            print(palgad)
            print(inimesed)
        elif choice == 0:
            break
        else:
            print("Vale valik!")