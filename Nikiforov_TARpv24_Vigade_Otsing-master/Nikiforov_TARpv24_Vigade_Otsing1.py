﻿from math import *  #вначале название библиотеки потом уже звездочка

print("Ruudu karakteristikud")
a = float(input('Sisesta ruudu külje pikkus => '))  #не добавлен float
try:
    if a > 0:
        S = a ** 2  
        print("Ruudu pindala", S)
        P = 4 * a 
        print("Ruudu ümbermõõt", P)  #Ковычка закрыта не правильно
        di = a * sqrt(2)
        print("Ruudu diagonaal", round(di, 2))
        print()
    else:
        print("Külje pikkus peab olema positiivne arv!")
except:
        print("Sisestatud arv!")


print("Ristküliku karakteristikud") #2 ковычки в конце
b = float(input("Sisesta ristküliku 1. külje pikkus => "))  #не добавлен float
c = float(input("Sisesta ristküliku 2. külje pikkus => "))  #не добавлен float
try:
    if b > 0 and c > 0:
        S = b * c
        print("Ristküliku pindala", S)
        P = 2 * (b + c)
        print("Ristküliku ümbermõõt", P)
        di = sqrt(b ** 2 + c ** 2) #возведение в корень а не просто умножение
        print("Ristküliku diagonaal", round(di))  # Функция print осталась открытой
        print()
    else:
        print("Külje pikkus peab olema positiivne arv!")
except:
    print("Sisestatud arv!")

print("Ringi karakteristikud")
r = float(input("Sisesta ringi raadiusi pikkus => "))  # Используя одиночные ковычки, строка открывается и сразу закрывается, а не считывает их как за 2 ковычки, не добавлен float
try:
    if r > 0:
        d = 2 * r
        print("Ringi läbimõõt", d)  # Нет разделения между текстом и переменной
        S = pi * r ** 2
        print("Ringi pindala", round(S))
        C = 2 * pi * r
        print("Ringjoone pikkus", round(C))  # Функция print осталась открытой
    else:
        print("Raadius peab olema positiivne arv!")
except :
    print("Sisestatud arv!")

d = 2 * r
print("Ringi läbimõõt", d)  # Нет разделения между текстом и переменной
S = pi * r ** 2
print("Ringi pindala", round(S))
C = 2 * pi * r
print("Ringjoone pikkus", round(C))  # Функция print осталась открытой
