import random
import random

# Ülesanne 31
k = random.randint(15, 50)
m = random.randint(4, 8)
print(f"Tal on {k} kotlette ja pannile mahub {m} kotlette")
print(f"On vaja praadida {k // m} täis pannid, ja {k % m} kotletid jäävad ära")
print()

# Ülesanne 30
n = random.randint(1, 10)
m = random.randint(20, 30)
print(f"N = {n}, M = {m}")
print("N kuni M:")
for i in range(n, m + 1):
    print(i, end=" ")
print()
print("M kuni N:")
for i in range(m, n - 1, -1):
    print(i, end=" ")
print()

# Ülesanne 29
for y in range(9):
    for x in range(9):
        if x == 0 or x == y:
            print("x", end=" ")
        else:
            print("0", end=" ")
    print()
print()

# Ülesanne 28
arv = random.randint(1, 10)
katsed = 0
print("Arvake arv vahemikus 1-10")
while True:
    while True:
        try:
            a = int(input("Arvake: "))
            break
        except:
            print("Sisesta täisarv!")
            continue
    if a == arv:
        break
    katsed += 1
print(f"Sa võitsid! Arv oli {arv}. Sinu katsed: {katsed}")
print()

# Ülesanne 23
r = random.randint(8, 16)
rS = r ** 2
a = random.randint(-10, 10)
b = random.randint(-10, 10)
print(f"Ring raadiusega {r}, koordinaatides ({a},{b})")
while True:
    try:
        n = int(input("Kui palju punkte tahad sisestada: "))
        break
    except:
        print("Sisesta täisarv!")
c = 0
for i in range(n):
    while True:
        try:
            x = int(input("Sisesta x: "))
            break
        except:
            print("Sisesta täisarv!")
    while True:
        try:
            y = int(input("Sisesta y: "))
            break
        except:
            print("Sisesta täisarv!")
    dx = x - a
    dy = y - b
    if dx ** 2 + dy ** 2 <= rS:
        print("Punkt jääb ringi sisse!")
        c += 1
    else:
        print("Punkt ei jää ringi sisse.")
print(f"Kokku on {c} punktid, mis jäävad ringi sisse.")
print()

# Ülesanne 18
for i in range(20, 51):
    if i % 3 == 0 and i % 5 != 0:
        print(f"{i} jagub 3-ga ja ei jaga 5-ga")
print()

# Ülesanne 17
arv = random.randint(1, 9)
for i in range(1, 10):
    print(f"{arv}*{i}={arv * i}")
print()

# Ülesanne 16
for y in range(9):
    for x in range(9):
        if x == y:
            print(x + 1, end=" ")
        else:
            print("0", end=" ")
    print()
print()

# Ülesanne 15
for x in range(10):
    for i in range(10):
        print(i, end=" ")
    print()
print()

# Ülesanne 14
n = random.randint(5, 20)
print(f"N = {n}")
korrutis = 1
for i in range(1, n + 1):
    korrutis *= i
print(f"Korrutis on {korrutis}")
print()


#Ulesanne 15
for x in range(10):
    for i in range(10):
        print(i, end=" ")
    print()
#Ulesanne 13

a = 100
b = 1000
k = 7

count = 0
total_sum = 0

for number in range(a, b+1, k):
    print(f"Kokku : {number}")
    count += 1
    total_sum += number

print(f"Kokku :  {count}")

#Ulesanne 12
N = random.randint(1, 30)
m = 0
print(f"Arv N: {N}")
for x in range(N):
    m += 10
N = m / 60
print(f"Kokku: {round(N, 2)} tundi")
#Ulesanne 11





#Ulesanne 10
for x in range (10):
    A = int(input("Siseta arv:"))
    B = int(input("Siseta arv:"))

    if A > B:
        print("A on suurem kui B")
    else:
        print("B on suurem kui A")

#Ulesanne 9
euro = random.randint(1, 100)
age = random.randint(1, 10)

print(f"Euros: {euro}")
print(f"Age: {age}")

for x in range(age):
    age1 = age * 0.3
    age += age1

print("Age : ", age)

#Ulesanne 8
for x in range(1, 21):
    print(x * 2.5, "cm")


#Ulesanne 7
a = int(input("Sisesta esimene arv: "))
b = int(input("Sisesta teine arv: "))
k = int(input("Sisesta intervall arv: "))

for numbers in range(a, b+1, k):
    if numbers % k == 0:
        print(numbers)

#Ulesanne 6
zero = 0
sum_negative = 0
sum_positive = 0
N = int(input("Arv N: "))
for i in range(N):
    num = float(input(f"Sisesta arv {i+1}: "))
    if num < 0:
        sum_negative += 1
    elif num > 0:
        sum_positive += 1
    elif num == 0:
        zero += 1
print(f"Positive : {sum_positive}, Negative: {sum_negative}, Zeros: {zero}")


#Ulesanne 5

N = int(input("Arv N: "))
sum_negative = 0

for i in range(N):
    num = float(input(f"Sesitav arv {i+1}: "))
    if num < 0:
        sum_negative += num

print(f"Summ: {sum_negative}")




#Ulesanne 4
root = 0
for x in range(1, 21):
    root += x
    print(root ** 2)

#Ulesanne 3
x = int(input("Sisesta arv: "))
for x in range (8):
    num = int(input("Sisesta arv: "))
    if num < 0:
        print("Viga")
        break
print(sum(x))


#Ulesanne 2
x_sum = 0
while True:
    try: 
        x = int(input("Sisesta arv: "))

        for i in range (1,x):
            if i > 1:
                x_sum += 1
                break
        else:
            print("Viga")

        print(x_sum)

    except:
        print("Viga")
        break

#Ulesanne 1
taisarv = 0
for x in range (15):
    arv=float(input(f"Sisesta {x+1} arv: "))

    if arv == int(arv): 
        taisarv += 1
 
print(taisarv)       
