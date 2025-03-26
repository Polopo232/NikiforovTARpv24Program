from Moodle_def_arvestus_too import *

try:
    arv = int(input("Sisestage sportlaste arv: "))
    random_name(arv)
    random_numbers(arv)
    menu()
except:
    print("Midagi läks valesti! Proovige uuesti.")