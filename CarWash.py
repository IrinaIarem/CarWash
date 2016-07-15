while True:
    input1 = input("What type of car wash do you prefer? Self-Service or automated car wash or hand-wash?")
    input2 = input("what type of car do you have? SUV, track or regular ?")
    input1 = input1.lower()
    input2 = input2.lower()
    price = 0
    def tax(a):
        tx = (a*1.0878)
        return tx
    if input2 == "suv":
        if input1 == "self-service":
            price = 50

        elif input1 == "automated":
            price = 100

        elif input1 == "hand-wash":
            price = 60

    elif input2 == "regular":
        if input1 == "self-service":
            price = 70

        elif input1 == "automated":
            price = 120

        elif input1 == "hand-wash":
            price = 60

    elif input2 == "track":
        if input1 == "self service":
            price = 40

        elif input1 == "automated":
            price = 120

        elif input1 == "hand-wash":
            price = 60
    price = tax(price)


    print("You've chosen", input1, "for", input2, "and your price is: $", price)

    car = input("would you like to continue?")
    if car == "no":
        break