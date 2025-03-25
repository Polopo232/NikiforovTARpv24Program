import random

# Списки для хранения данных
sportlased = []
tulemused = []

# Функция для создания случайных имен
def random_name(n):
    names = ["Jaan", "Kalle", "Mati", "Toomas", "Jüri", "Karl", "Joosep", "Kaido"]
    for i in range(n):
        valik = random.choice(names)
        sportlased.append(valik)

# Функция для создания случайных результатов
def random_numbers(n):
    for i in range(n):
        tulemused.append(random.randint(1, 100))

# Показать лучшие результаты
def show_best_results():
    try:
        n = int(input("Sisestage parimate sportlaste arv: "))
        
        # Создаем копию результатов и сортируем
        koopia = tulemused.copy()
        koopia.sort(reverse=True)
        
        # Выводим топ N результатов
        for i in range(n):
            if i >= len(koopia):
                break
            tulemus = koopia[i]
            index = tulemused.index(tulemus)
            nimi = sportlased[index]
            print(f"{i+1}. {nimi}: {tulemus}")
    except:
        print("Viga! Proovige uuesti.")

# Сортировка результатов
def sort_results():
    # Создаем список кортежей (результат, имя)
    andmed = []
    for i in range(len(tulemused)):
        andmed.append((tulemused[i], sportlased[i]))
    
    # Сортируем
    andmed.sort()
    
    # Выводим
    for i in range(len(andmed)):
        print(f"{i+1}. {andmed[i][1]}: {andmed[i][0]}")

# Поиск результата спортсмена
def show_athlete_result():
    nimi = input("Sisestage sportlase nimi: ")
    if nimi in sportlased:
        index = sportlased.index(nimi)
        print(f"{nimi} tulemus on {tulemused[index]}")
    else:
        print("Sellist sportlast ei leitud!")

# Дисквалификация
def disqualify_athletes():
    try:
        kriteerium = int(input("Sisestage kriteerium: "))
        i = 0
        while i < len(tulemused):
            if tulemused[i] < kriteerium:
                # Удаляем и спортсмена, и результат
                del sportlased[i]
                del tulemused[i]
            else:
                i += 1
        print("Diskvalifitseerimine lõpetatud.")
    except:
        print("Vigane sisend!")

# Показать всех
def show_all_athletes():
    for i in range(len(sportlased)):
        print(f"{sportlased[i]}: {tulemused[i]}")

# Меню
def menu():
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
            show_athlete_result()
        elif valik == "4":
            disqualify_athletes()
        elif valik == "5":
            show_all_athletes()
        elif valik == "6":
            print("Head aega!")
            break
        else:
            print("Vale valik!")

# Основная программа
print("Tere tulemast spordiprogrammi!")
try:
    arv = int(input("Sisestage sportlaste arv: "))
    random_name(arv)
    random_numbers(arv)
    menu()
except:
    print("Midagi läks valesti! Proovige uuesti.")
