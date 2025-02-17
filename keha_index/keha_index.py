from traceback import print_tb

#Ввод имени
print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Sisesta nimi: ")
print(nimi, ", oi kui ilus nimi!" )


try:
    #Вопрос
    choice = int(input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
    #Ввод данных
    if choice == 1:
        try:
            pikkus = int(input("Sisesta pikkus (cm): "))
            try:
                mass = float(input("Sisesta mass (kg): "))
            except:
                print("Vale kaalu formaat!")
        except:
            print("Vale pikkuse formaat")
        indeks = mass / (0.01 * pikkus) ** 2 #формула расчета индекса
        #if в зависимости от ответа index
        if indeks <= 16:
            print(f"{nimi}! Tervisele ohtlik alakaal. Sinu index: {indeks}")
        elif 16 < indeks <= 19:
            print(f"{nimi}! Alakaal. Sinu index: {indeks}")
        elif 19 < indeks <= 25:
            print(f"{nimi}! Normaalkaal. Sinu index: {indeks}")
        elif 25 < indeks <= 30:
            print(f"{nimi}! Ülekaal. Sinu index: {indeks}")
        elif 30 < indeks <= 35:
            print(f"{nimi}! Rasvumine. Sinu index: {indeks}")
        elif 35 < indeks <= 40:
            print(f"{nimi}! Tugev rasvumine. Sinu index: {indeks}")
        elif indeks > 40:
            print(f"{nimi}! Tervisele ohtlik rasvumine. Sinu index: {indeks}")
    elif choice == 0:
        print("Kahju! See on väga kasulik info! ")

    else:
        print("Kahju! See on väga kasulik info! ")
        print(" ")

except:
    print("Viga!")
