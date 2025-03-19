#Ulesanne 7
import calendar
from datetime import date


def date_check(day:int, month:int, year:int)->any:
    """
    """
    daysInMonth = calendar.monthrange(year, month)
    if year > 2025:
        return False
    elif month > 12:
        return False
    elif day < 1 or day > daysInMonth:
        return False

#Ulesanne 6
def is_prime (x:int) ->any:
    """ Just return True if number is easy or False in another situation

    x: int
    :rtype: any
    """
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
#Ulesanne 5
def bank_cred(euro:float, years:int) -> any:
    """Funcion just calculate, it multiplication numbers of euro on 10 procent

    euro:float
    years:int
    :rtype: any


    """
    for i in range(years):
        euro *= 1.1
    return euro
#Ulesanne 4
def season(nr_month:int) -> any:
    """Person input the number of month
    and funcion gives name of season

    nr_month : int
    :rtype: any
    """
    if nr_month in [3, 4, 5]:
        return 'kevad'
    if nr_month in [6, 7, 8]:
        return 'suve'
    if nr_month in [9, 10, 11]:
        return 'sügis'
    if nr_month in [12, 1, 2]:
        return 'talv'
    else:
        return 'Tundmatu kuu'
#Ulesanne 4 1
def seasonWhile() -> str:
    """Person input the number of month
    and funcion gives name of season

    nr_month : int
    :rtype: str
    """
    k = int(input(": "))
    while True:
        if k in range(1, 13):
            break
        else:
            k = int(input("Sisesta kuu number: "))
        return season(k)
#Ulesanne 3
def square(wall:float)->any:
    """Funktsioon ruudu pindala, ümbermõõdu ja diagonaali leidmiseks
    wall: int
    :rtype: any
    """
    S = wall ** 2
    P = wall * 4
    D = (2)**(1/2)*wall
    return S,P,D
#Ulesanne 3 with list
def square_list(wall:float)->list:
    """Funktsioon ruudu pindala, ümbermõõdu ja diagonaali leidmiseks
    wall: int
    Tõstab nimekirja (list)
    """
    S = wall ** 2
    P = wall * 4
    D = (2)**(1/2)*wall
    s_list = [S,P,D]
    return s_list
#Ulesanne 2 
def is_year_leap(aasta:int)->bool:
    """Liigaasta ledmine
    Tagastab True, kui liigaasta ja False kui on
    tavaline aasta:
    :param int aasta: aasta number
    :rtype: bool tagastab loogilises formaadis tulemus
    """

    if aasta % 4 == 0:
        v = True
    else:
        v=False
    return v
#Ulesanne 1
def arithmetic(a:float, b:float, operation:str)->any:
    """Lihtne kalkulaator
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float a: Sisend kasutajalt, mingi ujukomaarv:
    :param float b: Sisend kasutajalt, mingi ujukomaarv:
    :param str operation: aritmeetiline tehe, mis valib kasutaja
    :rtype: Määrata tüüp(float või str)
    """
    if operation in ["+","-","*","/"]:
        if b == 0 and operation =="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(a)+operation+str(b))
    else:
        vastus = "Tundmatu tehe"
    return vastus
