import random

#5 При помощи цикла распечатать ряд Фибоначчи: 0 1 1 2 3 5 8 13 21. (Первые два числа равны 0 и 1, а каждое последующее число равно сумме двух предыдущих чисел.)
a = 0
b = 1

for x in range (1, 20):
    print(a, end=" ")
    a1 = a
    a = b
    b = a1 + b
print()

#4 Мой богатый дядюшка подарил мне один доллар в мой первый день рождения. В каждый день рождения он увеличивал свой подарок и прибавлял к нему столько долларов, сколько лет мне исполнилось. Написать программу, указывающую, к какому дню рождения подарок превысит 100$.
start = 0
final = 100 
age = 1
while start < final:
    start += age
    if start >= final:
        print(f"Age: {age}")
        break
    age += 1


#3 Известны оценки по физике каждого из  учеников класса. Определить среднюю оценку. (Оценки и количество учеников получаем случайным образом)
stud = random.randint(1, 10)
kokku_marks = 0

for x in range(stud):
    kokku_marks += random.randint(1, 6)

studkesk = kokku_marks / stud
print(f"Keskmine hinne on: {studkesk}")
print(f"Kokku students on: {stud}")


#2 Вывести степени натуральных чисел, не превосходящие данного числа n**3. Пользователь задает показатель степени и число n.
try:
    ruut = int(input("Sisesta ruut: "))
    n = int(input("Sisesta arv: "))
    max_value = n**3
    for x in range(1, n + 1):
        result = x ** ruut
        if result <= max_value:
            print(f"{x} ** {ruut} = {result}")
except:
    print("Viga! Sisesta palun tervislik arv") 

#1 Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n скворечников. Между двумя соседними скворечниками также имеется пустой (из пробелов) столбец. Разрешается вывести пустой столбец после последнего скворечника. Для упрощения рисования скопируйте скворечник из примера в среду разработки.
n1 = random.randint(1, 9)
for n in range (n1):
        print(f"   -----")
        print(f"  |  O  |")
        print(f"  !  -  !")
        print(f"   -----")


