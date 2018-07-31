def main():
    user_amount = float(
        input("Enter amount to be converting into Coin and Bills: "))

    peso1000bill = 0
    peso500bill = 0
    peso100bill = 0
    peso20bill = 0
    peso10coin = 0
    peso5coin = 0
    peso1coin = 0

    if(user_amount >= 1000):
        peso1000bill = int(user_amount / 1000)
        user_amount = user_amount % 1000
    if(user_amount >= 500):
        peso500bill = int(user_amount / 500)
        user_amount = user_amount % 500
    if(user_amount >= 100):
        peso100bill = int(user_amount / 100)
        user_amount = user_amount % 100
    if(user_amount >= 20):
        peso20bill = int(user_amount / 20)
        user_amount = user_amount % 20
    if(user_amount >= 10):
        peso10coin = int(user_amount / 10)
        user_amount = user_amount % 10
    if(user_amount >= 5):
        peso5coin = int(user_amount / 5)
        user_amount = user_amount % 5
    if(user_amount >= 1):
        peso1coin = int(user_amount / 1)
        user_amount = user_amount % 1

    print("Take out:")
    print("1000 Peso Bills: " + str(peso1000bill))
    print("500 Peso Bills: " + str(peso500bill))
    print("100 Peso Bills: " + str(peso100bill))
    print("20 Peso Bills: " + str(peso20bill))
    print("10 Peso Coins: " + str(peso10coin))
    print("5 Peso Coins: " + str(peso5coin))
    print("1 Peso Coins: " + str(peso1coin))


main()
