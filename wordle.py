import random
from colorama import Fore, Style, init

init(autoreset=True)

sõnad = ['RAAMAT', 'VANKER', 'LINNAD', 'SININE', 'TALVEL', 'KASSID', 'TÄHEND']

while True:
    peidetud_sõnad = random.choice(sõnad)
    katse = 6

    print("Arva sõna, mis koosneb", len(peidetud_sõnad), "tähenurgast.")

    for attempt in range(1, katse + 1):
        try:
            guess = input(f"Katse {attempt}/{katse}. Sisesta sõna: ").upper()
        except:
            print("Sisestusviga.")

        if len(guess) != len(peidetud_sõnad):
            print(f"Sõna peab olema {len(peidetud_sõnad)} tähemärgist.")

        result = []

        for letter in guess:
            if letter in peidetud_sõnad:
                if guess.find(letter) == peidetud_sõnad.find(letter):
                    result.append(Fore.GREEN + letter + Style.RESET_ALL)
                else:
                    result.append(Fore.YELLOW + letter + Style.RESET_ALL)
            else:
                result.append(letter)

        print("Tulemus: ")
        for letter in result:
            print(letter)
        print()

        if guess == peidetud_sõnad:
            print(Fore.GREEN + "Õnnitleme! Sa arvasid sõna õigesti!" + Style.RESET_ALL)
            break
    else:
        print(Fore.RED + f"Kahjuks! Sa ei arvanud sõna õigesti. Õige sõna oli: {peidetud_sõnad}" + Style.RESET_ALL)

    choice1 = input("Kas tahad mängida uuesti? (y/n): ")
    if choice1.lower() == 'y':
        continue
    else:
        break
