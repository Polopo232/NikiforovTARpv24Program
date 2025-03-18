#Ulesanne 3

def square(wall:float)->any:
    """Funktsioon ruudu pindala, ümbermõõdu ja diagonaali leidmiseks
    wall: int
    """
    S = wall ** 2
    P = wall * 4
    D = (2)**(1/2)*wall
    return S,P,D

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