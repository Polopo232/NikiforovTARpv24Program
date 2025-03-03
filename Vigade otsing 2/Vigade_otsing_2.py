print("*** ARVUMÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = abs(int(input("Sisesta täisarv => ")))  # Исправил запись abs
        break
    except ValueError:
        print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a == 0:
    print("Nulliga pole mõtet midagi teha")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrame, kui palju on arvus paarisarve ja kui palju paaritut")
    print()
    c = b = a  # Заменил a == b == c на c = b = a
    paaris = 0  # Убрал 1 =
    paaritu = 0  # Убрал 1 =
    while b > 0:  # Заменил ; на :
        digit = b % 10  # Чтобы узнать последние число, добавил b % 10
        if digit % 2 == 0:  # Добавил еще одно =
            paaris += 1  # Заменил =+ на +=
        else:
            paaritu += 1  # Заменил =+ на +=
        b = b // 10  # Исправил табуляцию
    
    print("Paarisarve:", paaris)  # Добавил запятую для правильного синтаксиса
    print("Paarituid arve:", paaritu)  # Добавил запятую для правильного синтаксиса
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörame* sisestatud arvu ümber")
    print()
    b = 0
    while a > 0:  # Добавил :
        number = a % 10  # Чтобы узнать последние число добавил a % 10
        a = a // 10
        b = b * 10
        b += number  # Заменил =+ на +=
    print("*Pööratud* arv", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Kontrollime Sirakuza hüpoteesi")  # Удалил лишнюю скобку
    print()
    c = b
    if c % 2 == 0:  # Добавил =
        print('{:>4}'.format(c), "Paarisarv. Jagame kahega.")  # Добавил '{:>4}'.format(c)
    else:
        print('{:>4}'.format(c), "Korrutame 3-ga, liidame 1 ja jagame kahega.")
    while c != 1:
        if c % 2 == 0:  # Добавил =
            c = c // 2
        else:
            c = (3 * c + 1) // 2  # Сделаем деление целым числом
        print(c, end=" ")  # Закрыл ковычку, для правильной работы и добавил пробел
    print()
    print("Hüpotees on õige")  # Заменил '' на "
