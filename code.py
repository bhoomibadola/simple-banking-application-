balance = 0.0
kyc_document = {}

def balance_check():
    print(f"Your balance is {balance}")
    print("======================")

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
    else:
        print("Cannot deposit negative or zero amount")
        print("======================")

def withdraw(amount):
    global balance
    if amount <= 0:
        print("Cannot withdraw negative or zero amount")
        print("======================")
    elif amount > balance:
        print("Cannot withdraw. Insufficient funds")
        print("======================")
    else:
        balance -= amount

def update_kyc(doc):
    global kyc_document
    kyc_document.update(doc)

def kyc_check():
    if len(kyc_document) == 0:
        print("No KYC document")
        print("======================")
    else:
        for doc in kyc_document:
            print(f"KYC {doc}: {kyc_document[doc]}")
            print("======================")

if __name__ == "__main__":
    print("======================")
    print("WELCOME TO THE BANKING APPLICATION")
    print("======================")
    print()

    while True:
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check KYC")
        print("5. Update KYC")
        print("6. Quit")
        choice = input("Enter your choice: ")
        print("======================")

        if choice == "1":
            balance_check()
        elif choice == "2":
            amt = int(input("Enter amount: "))
            deposit(amt)
            if amt > 0:
                print(f"Amount deposited: {amt}")
                print("======================")
        elif choice == "3":
            amt = int(input("Enter amount: "))
            if amt > 0 and amt <= balance:
                withdraw(amt)
                print(f"Amount withdrawn: {amt}")
                print("======================")
            else:
                withdraw(amt)
        elif choice == "4":
            kyc_check()
        elif choice == "5":
            kyc_doc = {}
            n_documents = int(input("Enter number of documents: "))
            for i in range(n_documents):
                key = str(input("Enter key for document: "))
                value = str(input("Enter value for document: "))
                kyc_doc[key] = value
            update_kyc(kyc_doc)
            print("KYC updated")
            print("======================")
        elif choice == "6":
            print("Quit")
            break
        else:
            print("Invalid choice")
            print("======================")
            print()

    print("Thank you for banking with us!")
