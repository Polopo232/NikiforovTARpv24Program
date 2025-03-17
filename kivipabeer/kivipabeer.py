
import random

while True:
    choices = ['kivi', 'käärid', 'paber']
    print("Valige: kivi, käärid või paber")
    try:
        user_choice = input().lower()
    except:
        print("Viga !")

    computer_choice = random.choice(choices)
    print(f"Arvuti on valinud: {computer_choice}")

    if user_choice == computer_choice:
        print("Viik !")
    elif (user_choice == 'kivi' and computer_choice == 'käärid') or \
         (user_choice == 'käärid' and computer_choice == 'paber') or \
         (user_choice == 'paber' and computer_choice == 'kivi'):
        print("Sa oled võitnud!")
    else:
        print("Sa kaotasid!")