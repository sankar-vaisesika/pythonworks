# Mini ATM Simulator

accounts={"1001":{"pin":"1234","balance":10000}}

acc=input("Enter account number:")
pin=input("Enter PIN:")

if acc in accounts and accounts[acc]["pin"]==pin:

    print("Login successful")

    while True:
        print("\n1.Check Balance \n2.Withdraw \n3.Deposit \n4.Exit")
        choice=input("CHoose options:")

        if choice=="1":
            print("Balance is:",accounts[acc]['balance'])

        elif choice=="2":
            amount=float(input("ENter withdrawel amount:"))
            if amount<=accounts[acc]["balance"]:
                accounts[acc]["balance"]-=amount
                print("Amount withdrawn \nNew balance:",accounts[acc]["balance"])
            else:
                print("Insufficient balance")

        elif choice =="3":
            amount=float(input("Enter deposit amount:"))
            accounts[acc]["balance"]+=amount
            print("Amount deposited \nNew balance:",accounts[acc]["balance"])

        elif choice=="4":
            print("Thanku Visit again!")
            break

        else:
            print("Invalid choice . Try again")
else:

    print("Invalid account number or PIN")