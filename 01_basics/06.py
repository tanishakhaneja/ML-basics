while True:
    try:
        num = int(input("enter a no b/w 1 and 10: "))
        if 1 <= num <= 10:
            print("thanks")
            break
        else:
            print("invalid no, try again")
    except ValueError:
        print("pls enter a valid int")
