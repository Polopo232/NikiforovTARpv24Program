import random
# Operation
op = ["+", "-"]
op1 = ["+", "-", "*", "/"]
op2 = ["+", "-", "*", "/", "**"]

while True:
    # Choose level
    try:
        choice1 = int(input("Tase (1, 2, 3):  "))
    except:
        print("Palun sisestage number")
    # First level
    if choice1 == 1:
        oige = 0
        #Loop for (in order to be 10 problems)
        for x in range(1, 11):
            try:
                #Random number 1 to 50
                num1 = random.randint(1, 50)
                num2 = random.randint(1, 50)
                #Random operation
                random_op = random.choice(op)
                #Show the problem
                ans = int(input(f"{num1} {random_op} {num2} = "))
                #Solve the problem
                correct_answer = eval(f"{num1} {random_op} {num2}")
                #Count right answers
                if ans == correct_answer:
                    print("Õige vastus")
                    oige += 1
                else:
                    print("Vale vastus")
            except:
                print("Palun sisestage number")
        #Math the mark
        oige_percentage = (oige / 10) * 100
        print(f"Õigeid vastuseid: {oige}")
        print(f"Hinne: {oige_percentage}%")
        if oige_percentage >= 90:
            print("See on 5")
        elif oige_percentage >= 75:
            print("See on 4")
        elif oige_percentage >= 60:
            print("See on 3")
        elif oige_percentage >= 50:
            print("See on 2")
        else:
            print("See on 1")
        choice_q = input("Kas sa jätkama? (y/n): ")
        if choice_q == "n":
            break



    # Level 2
    if choice1 == 2:
        oige = 0
        for x in range(1, 11):
            try:
                num1 = random.randint(1, 100)
                num2 = random.randint(1, 100)
                random_op = random.choice(op1)
                ans = int(input(f"{num1} {random_op} {num2} = "))
                if ans == eval(str(num1) + random_op + str(num2)):
                    print("Õige vastus")
                    oige += 1
                else:
                    print("Vale vastus")
            except:
                print("Palun sisestage number")

        oige_percentage = (oige / 10) * 100
        print(f"Õigeid vastuseid: {oige}")
        print(f"Hinne: {oige_percentage}%")
        if oige_percentage >= 90:
            print("See on 5")
        elif oige_percentage >= 75:
            print("See on 4")
        elif oige_percentage >= 60:
            print("See on 3")
        elif oige_percentage >= 50:
            print("See on 2")
        else:
            print("See on 1")
        choice_q = input("Kas sa jätkama? (y/n): ")
        if choice_q == "n":
            break
    # Level 3
    if choice1 == 3:
        oige = 0
        for x in range(1, 11):
            try:
                num1 = random.randint(1, 150)
                num2 = random.randint(1, 150)
                random_op = random.choice(op2)
                ans = int(input(f"{num1} {random_op} {num2} = "))
                if ans == eval(str(num1) + random_op + str(num2)):
                    print("Õige vastus")
                    oige += 1
                else:
                    print("Vale vastus")
            except:
                print("Palun sisestage number")

        oige_percentage = (oige / 10) * 100
        print(f"Õigeid vastuseid: {oige}")
        print(f"Hinne: {oige_percentage}%")
        if oige_percentage >= 90:
            print("See on 5")
        elif oige_percentage >= 75:
            print("See on 4")
        elif oige_percentage >= 60:
            print("See on 3")
        elif oige_percentage >= 50:
            print("See on 2")
        else:
            print("See on 1")
        choice_q = input("Kas sa jätkama? (y/n): ")
        if choice_q == "n":
            break
