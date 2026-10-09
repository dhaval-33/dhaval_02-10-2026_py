ammount=int(input("enter your initial ammount = "))

if ammount>0:

    print("1)press 1 for deposit")
    print("2)press 2 for withdraw")
    choice=int(input("enter your choice here = "))

    if choice == 1:
        deposit=int(input("enter how much you want to deposit = "))
        ammount += deposit

        print(f"your new bank balance after deposit amount ({deposit}) is = {ammount}")

    elif choice==2:
        withdraw=int(input("enter how much you want to withdraw = "))
        ammount -= withdraw

        print(f"your new bank balance after withdraw amount ({withdraw}) is = {ammount}")

    else:
        print("enter valid choice")

else:
    print("insufficient ammount")