a = int(input("enter a lucky number between 1 and 10: "))

match a:
    case 1:
        print("you won a car")
    case 2:
        print("you won a bike")
    case 3:
        print("you won a phone")
    case 4:
        print("you won a laptop")
    case _:
        print("you won nothing, try again next time")