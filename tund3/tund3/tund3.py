
from random import *
#naidis 4


n1 = str(input("esimese nimi: "))
n2 = str(input("teise nimi: "))

if n1.lower() == n2.lower():
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

