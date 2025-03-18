from Moodul_def_tesks import *



#square_list
s_list = square(float(input("Sisesta külg: ")))
for x in s_list:
    print(x)

#square
S,P,D = square(float(input("Sisesta külg: ")))
print(S,P,D)

#is_year_leap
aasta = int(input("Sisend aasta: "))
if aasta > 0: v = is_year_leap(aasta)
if v == True:
    print("Respect ! ")
else:
    print("Un respect !")


#arithmetic funksiooni kasutamine
a = float(input("Sisesta arv 1: "))
b = float(input("Sisrsta arv 2: "))
t = input("Tehe: ")
v = arithmetic(a,b,t)
print(v)


