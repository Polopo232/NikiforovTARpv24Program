
from random import *
#naidis 14

inimesed = int(input("Kui palju inimesi?: "))
buss_koht = int(input("Mitu kohta on bussis?: "))

bussid_vaja = inimesed // buss_koht
viimane_buss = inimesed % buss_koht

if viimane_buss > 0:
    bussid_vaja += 1
else:
    viimane_buss = buss_koht

print(f"{bussid_vaja} bussi.")
print(f"vimane bussi on {viimane_buss} inimest.")

    

#nadis 13

gender = input("sugu (m/n): ").lower()

if gender == 'm':
    age = int(input("Kui vana oled?: "))
    if 16 <= age <= 18:
        print("Sa sobid")
    else:
        print("Sa ei sobi.")
else:
    print("Sa ei sobi.")



#nadis 12 

hinna1 = float(input("Hinna?: "))
if hinna1 >= 10:
    hinna2 = hinna1 * 0.1
    hinna1 -= hinna2
    print(hinna1)
if hinna1 <= 11:
    hinna2 = hinna1 * 0.2
    hinna1 -= hinna2
    print(hinna1)


#nadis 11

bithday = input("Mis on minu sunnipaev?(day-month(01-01)): ")
if bithday == "15-03":
    print("See on minu sunnipaev")
else:
    print("See ei ole mine sunnipaev")

#nadis 10

arv1 = float(input("esimine arv: "))
arv2 = float(input("teine arv: "))

choice3 = input("Mis operatsion sa tahad teha?: ")

if choice3 == "+":
    print(arv1 + arv2)
if choice3 == "-":
    print(arv1 - arv2)
if choice3 == "*":
    print(arv1 * arv2)
if choice3 == "/":
    print(arv1 / arv2)


#nadis 9
pool1 = float(input("esimene pool: "))
pool2 = float(input("teine pool: "))
pool3 = float(input("kolma pool: "))
pool4 = float(input("nelja pool: "))

if pool1 == pool2 == pool3 == pool4:
    print("See on ruut")
else:
    print("See ei ole ruut")

#naidis 8

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
    


#naidis 7

pikk = float(input("Kuidas sinu pikk?: "))
if pikk <= 120:
    print("sa oled goblin")
elif pikk <= 160:
    print("sa oled keskmine")
elif pikk >= 180:
    print("Sa oled hiiglane")
else:
    print("Midagi läks valesti")


#naidis 5

temp = float(input("Kuidas temp?: "))
if temp <= 18:
    print("Soovitav")
else:
    print("Soovitav toasoojus talvel")


#naidis 4
price1 = float(input("Kuidas hinna?: "))

if price1 >= 700:
    price1 = price1 * 0.7
    print(price1)
else:
    print("ei")

#naidis 3
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




#naidis 2   
n1 = input("esimese nimi: ")
n2 = input("teise nimi: ")

if n1.isalpha() and n2.isalpha() and n1 == "nikita" and n2 == "artjom":
    print(f"{n1} ja {n2} pinginaabrid")
else:
    print(f"{n1} ja {n2} ei ole pinginaabrid.")

#naidis 1
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

