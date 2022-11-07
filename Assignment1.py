"""Health management system"""



def getdate():
    import datetime
    return datetime.datetime.now()


def log():
    b = int(input("which client you want to choose? \npress 1 for Batman\npress 2 for Ironman\npress 3 for Superman"))
    if b == 1:
        c = int(input("What do you want to add among Food or Exercise?\nfor food press 1\nfor exercise press 2: "))
        if c == 1:
            with open("Batman_diet.txt","a") as xf:
                print("What does he eat?")
                f1 = input()
                xf.write(str(getdate())+":"+f1)
            print("Diet add successfully.")
        elif c == 2:
            with open("Batman_exercise.txt","a") as xe:
                print("What does he do?")
                e1 = input()
                xe.write(str(getdate())+":"+e1)
            print("Exercise add successfully.")
        elif b == 2:
            c = int(input("What do you want to add among Food or Exercise?\nfor food press 1\nfor exercise press 2"))
            if c == 1:
                with open("Ironman_diet.txt", "a") as yf:
                    print("What does he eat?")
                    f2 = input()
                    yf.write(str(getdate()) + ":" + f2)
                    print("Diet add successfully.")
            elif c == 2:
                with open("Ironman_exercise.txt", "a") as ye:
                    print("What does he do?")
                    e2 = input()
                    ye.write(str(getdate()) + ":" + e2)
                    print("Exercise add successfully.")
        elif b == 3:
            c = int(input("What do you want to add among Food or Exercise?\nfor food press 1\nfor exercise press 2"))
            if c == 1:
                with open("Superman_diet.txt", "a") as zf:
                    print("What does he eat?")
                    f3 = input()
                    zf.write(str(getdate()) + ":" + f3)
                    print("Diet add successfully.")
            elif c == 2:
                with open("Superman_exercise.txt", "a") as ze:
                    print("What does he do?")
                    e3 = input()
                    ze.write(str(getdate()) + ":" + e3)
                    print("Exercise add successfully.")


def retrieve():
    b = int(input("which client you want to choose?\npress 1 for Batman\npress 2 for Ironman\npress 3 for Superman\n"))
    if b == 1:
        c = int(input("What do you want to retrieve among Food or Exercise?\nfor food press 1\nfor exercise press 2"))
        if c == 1:
            food_b = open("Batman_diet.txt")
            print(food_b.read())
        elif c == 2:
            ex_b = open("Batman_exercise.txt")
            print(ex_b.read())
    if b == 2:
        c = int(input("What do you want to retrieve among Food or Exercise?\nfor food press 1\nfor exercise press 2"))
        if c == 1:
            food_i = open("Ironman_diet.txt")
            print(food_i.read())
        elif c == 2:
            ex_i = open("Ironman_exercise.txt")
            print(ex_i.read())
    if b == 3:
        c = int(input("What do you want to retrieve among Food or Exercise?\nfor food press 1\nfor exercise press 2"))
        if c == 1:
            food_s = open("Superman_diet.txt")
            print(food_s.read())
        elif c == 2:
            ex_s = open("Superman_exercise.txt")
            print(ex_s.read())


print("welcome to health management system designed by Hrithik")
while True:
    print("To Log press 1\nTo Retrieve press 2")
    selection = int(input())
    if selection == 1:
        log()
    elif selection == 2:
        retrieve()
    else:
        print("input valid terms")
    ask = input("would you like to continue?\npress Y for continue\npress N for close\n").upper()
    if ask == "Y":
        continue
    elif ask == "N":
        break
