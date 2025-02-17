# Ввод имени
print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Sisesta nimi: ")
print(nimi, ", oi kui ilus nimi!" )
while True:
    try:
        #Вопрос
        choice = int(input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
        #Ввод данных с цыклом
        if choice == 1:
            while True:
                try: #Высота
                    pikkus = int(input("Sisesta pikkus (cm): "))
                    break
                except:
                    print("Vale pikkuse formaat")
            while True:
                try:#Вес
                    mass = float(input("Sisesta mass (kg): "))
                    break
                except:
                    print("Vale kaalu formaat!")
            indeks = round(mass / (0.01 * pikkus) ** 2, 2) #формула расчета индекса
            #if в зависимости от ответа index
            if indeks <= 16:
                print(f"{nimi}! Tervisele ohtlik alakaal. Sinu index: {indeks}")
                break
            elif 16 < indeks <= 19:
                print(f"{nimi}! Alakaal. Sinu index: {indeks}")
                break
            elif 19 < indeks <= 25:
                print(f"{nimi}! Normaalkaal. Sinu index: {indeks}")
                break
            elif 25 < indeks <= 30:
                print(f"{nimi}! Ülekaal. Sinu index: {indeks}")
                break
            elif 30 < indeks <= 35:
                print(f"{nimi}! Rasvumine. Sinu index: {indeks}")
                break
            elif 35 < indeks <= 40:
                print(f"{nimi}! Tugev rasvumine. Sinu index: {indeks}")
                break
            elif indeks > 40:
                print(f"{nimi}! Tervisele ohtlik rasvumine. Sinu index: {indeks}")
                break
        elif choice == 0:
            print("Kahju! See on väga kasulik info! ")
            break

        else:
            print("Kahju! See on väga kasulik info! ")
            print(" ")

    except:
        print("Viga!")
