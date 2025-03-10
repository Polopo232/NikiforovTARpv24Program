from random import *

sone = "Programmerimine"
print(sone)
#Возведение строки в лист
sone_list = list(sone)
print(sone_list)
#Перевернуть список
sone_list.reverse()
print(sone_list)
#Подсчет букв до большой P
print(sone_list.index("P"))
#Подсчет симовлов в листи и строке при помощи len()
print(len(sone_list))
print(len(sone))
#Удаление буквы m
sone_list.remove("m")
print(sone_list)
#Удаление всех букв m 
kogus_m = sone_list.count("m")
for m in range(kogus_m):
    sone_list.remove("m")
print(sone_list)
#Добавление рандомного количества значений в список
tähe = randint(1, 2)
for x in range (tähe):
    while True:
        try:
            b = input("Sesista taht: ")
            if b.isalpha: break
        except :
            print("Viga!")
    while True:
        try:
            inx = input("Sesista taht: ")
            if inx.isnumeric() & int(inx) < len(sone_list): break
        except :
            print("Viga!")
    sone_list.insert(int(inx), b) #Ввод в список значения введенные ранее
print(sone_list)

print(sone_list.cente)
print(sone_list.title)
print(sone_list.swapcase())

print(sone_list.sort()) #сортировка reverse развернуть соортировку A-Z to Z-A, key нужен для того чтобы вставить функцию

        