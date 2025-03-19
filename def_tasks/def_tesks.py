from Moodul_def_tesks import *




#is_prime
for ghffg in range (1, 11):
    x = int(input("Sisend arv: "))
    print(is_prime(x))


#back_cred
summa = float(input("Summa of euro: "))
years = int(input("How many year?: "))
if summa > 0 and years > 0:
    i = bank_cred(summa, years)
    print(i)
else:
    print("Just zero years or euro")


#season
month = int(input("Number of month: "))
if month > 0 :
    x = season(month)
    print(x)

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


