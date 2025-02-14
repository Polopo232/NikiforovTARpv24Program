
from random import *
#naidis 14

    

#naidis 9

tsekk=0

choice2 = input("Kas sa tahad osta piim?(y/n): ")
if choice2 == "y":
    palju = int(input("Kui palju?: "))
    tsekk = tsekk + palju * 0.8
choice2 = input("Kas sa tahad osta leib?(y/n): ")
if choice2 == "y":
    palju = int(input("Kui palju?: "))
    tsekk = tsekk + palju * 1.2
choice2 = input("Kas sa tahad osta juust?(y/n): ")
if choice2 == "y":
    palju = int(input("Kui palju?: "))
    tsekk = tsekk + palju * 2

print(tsekk)
    


#naidis 8

pikk = float(input("Kuidas sinu pikk?: "))
if pikk <= 120:
    print("sa oled goblin")
elif pikk <= 160:
    print("sa oled keskmine")
elif pikk >= 180:
    print("Sa oled hiiglane")
else:
    print("Midagi läks valesti")


#naidis 7

temp = float(input("Kuidas temp?: "))
if temp <= 18:
    print("Soovitav")
else:
    print("Soovitav toasoojus talvel")


#naidis 6
price1 = float(input("Kuidas hinna?: "))

if price1 >= 700:
    price1 = price1 * 0.7
    print(price1)
else:
    print("ei")

#naidis 5
wall1 = float(input("esimene sein: "))
wall2 = float(input("teine sein: "))

Sfloor = wall1 * wall2
print(f"{Sfloor} m2")
choice = input("Kas sa tahad remontide teha?(y/n): ")
if choice.lower() == "y":
    price = float(input("Kui palju maksab 1 ruutmeeter?: "))
    price *= Sfloor
    print(price)
elif choice.lower() == "n":
    print("Hästi")
else:
    print("Midagi läks valesti")




#naidis 4
n1 = input("esimese nimi: ")
n2 = input("teise nimi: ")

if n1.isalpha() and n2.isalpha() and n1 == "nikita" and n2 == "artjom":
    print(f"{n1} ja {n2} pinginaabrid")
else:
    print(f"{n1} ja {n2} ei ole pinginaabrid.")

#naidis 3
# nimi=input("Mis on sinu nimi?: ")
# if nimi.isupper() and nimi.lower()=="juku":
#     print("Lahme kinnosse")
try:
    age = int(input(""))
    if age<0 or age>100:
        pilet="!!!"
    elif age < 6:
        pilet = "tasuta"
    elif age <= 14:
        pilet = "lastepilet"
    elif age <= 65:
        pilet = "täispilet"
    elif age <= 100:
        pilet = "sooduspilet"
    else:
        print("viga")
    print(pilet)
except Exception as e:
    print("Tekkis viga: ", e)





#Näidis 1

# arv = randint(0,10)
# print(arv)
# if arv > 5:
#     print("***********************")
#     print(f"Arv {arv} surem kui 5")
#     print("***********************")
# if arv>5: print(f"Arv {arv} suurem kui 5")

#Näidis 2
arv1 = randint(-10,10)
print(arv1)
# if arv1 > 0:
#     print("Positiivne")
# else:
#     print("Negatiivne") #viga

if arv1 > 0:
    print("Positiivne")
elif arv1 == 0:
    print("See on null")
else:
    print("Negatiivne")

