

def shop():
    total = 0
    while True:

        print(fruits)
        cart = input("Choose what items to bag, enter'done'if done: ").lower()

        if cart in isle_one:
            amount = int(input("How many are you buying?: "))
            total += isle_one[cart]*amount

        if cart == "done":
            print("Your total is: "+str(total)+"$")
            print("Thank you for shopping, Have a nice day!")
            break

fruits = ["grapes 2$","banana 2$","citrus 1$","peach 2$"]
#poultry = ["pork","beef","chicken","seafood"]
#beverages = ["tea","soft drinks","juice"]

isle_one = {"grapes":2,"banana":2,"citrus":1,"peach":2}
#isle_two = {"pork":"pork","beef":2,"chicken":3,"seafood":4}

shop()



