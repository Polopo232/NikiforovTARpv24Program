ex_list = []

while True:
    print(ex_list)
    print()
    print("1. Lisage loendisse sõnu või tähti")
    print("2. Kustuta loend")
    print("3. Kirjade suurtähtede muudatused")
    print("4. Sorteeri loend (A-Z)")
    print("5. Sorteeri loend (Z-A)")
    print("6. Lisage kõik sõnad kokku")
    print("7. Ühe tähemärgi loendamine")
    print("8. Loendi kõigi märkide loendamine")
    print("9. Tükeldatud loend")
    print("0. Lõpeta programm")

    choose1 = input("Sinu valik: ")

    if choose1 == "1":
        try:
            ask1 = int(input("Kui palju sõnu või tähti lisada?: "))
            for x in range(ask1):
                ex_list_input = input("Sisesta sõna või täht: ")
                ex_list.append(ex_list_input)
            print("Loend pärast lisamist:", ex_list)
        except:
            print("Viga! Palun sisesta number.")

    elif choose1 == "2":
        ex_list.clear()
        print("Loend on tühi:", ex_list)

    elif choose1 == "3":
        print("1. Tehke kõik tähed suureks")
        print("2. Kõik tähed on väikesed")
        print("3. Vahetage suur- ja väiketähed")
        try:
            choose2 = int(input("Mida sa tahad teda?: "))
            if choose2 == '1':
                ex_list = [x.upper() for x in ex_list]
                print(ex_list)
            elif choose1 == '2':
                ex_list = [x.lower() for x in ex_list]
                print(ex_list)
            elif choose1 == '3':
                ex_list = [x.swapcase() for x in ex_list]
                print(ex_list)
            else: 
                print("Viga! Sesita arv")


        except :
            print("Viga!")


    elif choose1 == "4":
        ex_list.sort()
        print("Loend pärast sorteerimist A-Z:", ex_list)

    elif choose1 == "5":
        ex_list.sort(reverse=True)
        print("Loend pärast sorteerimist Z-A:", ex_list)

    elif choose1 == "6":
        ex_list_sum = ''.join(ex_list)
        print("Kokku ühendatud sõnad:", ex_list_sum)

    elif choose1 == "7":
        ex_list_count_input = input("Mis me otsime?: ")
        ex_list_count = ex_list.count(ex_list_count_input)
        print(f"Leitud sõnade arv: {ex_list_count}")

    elif choose1 == "8":
        ex_list_count = len(ex_list)
        print(f"Loendi elementide arv: {ex_list_count}")

    elif choose1 == "9":
         ex_list = [x.split() for x in ex_list]
         print(ex_list)


    elif choose1 == "0":
        print("Head aega!")
        break

    else:
        print("Vale valik! Proovige uuesti.")
