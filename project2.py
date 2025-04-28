class ATM:
    balance = 0  # balance is a class variable

    def set_balance(self, initial_balance):
        ATM.balance = initial_balance

    def check_balance(self):
        print(f"Your current balance is: ${ATM.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            ATM.balance += amount
            print(f"You have deposited ${amount:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > ATM.balance:
            print("Insufficient balance.")
        else:
            ATM.balance -= amount
            print(f"You have withdrawn ${amount:.2f}.")

    def menu(self):
        while True:
            print("\n==== ATM Menu ====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter amount to deposit: $"))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: $"))
                self.withdraw(amount)
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Main program
atm = ATM()
atm.set_balance(1000.00)  # Setting initial balance manually
atm.menu()

# def check_balance(balance):
#     print(f"Your current balance is: ${balance:.2f}")

# def deposit(balance,amount):
#     if amount > 0:
#         balance += amount
#         print(f"You have deposited ${amount:.2f}.")
#     else:
#         print("Deposit amount must be positive.")
#     return balance

# def withdraw(balance,amount):
#     if amount <= 0:
#         print("Withdrawal amount must be positive.")
#     elif amount > balance:
#         print("Insufficient balance.")
#     else:
#         balance -= amount
#         print(f"You have withdrawn ${amount:.2f}.")
#     return balance

# def menu():
#     balance = 0
#     while True:
#         print("\n==== ATM Menu ====")
#         print("1. Check Balance")
#         print("2. Deposit Money")
#         print("3. Withdraw Money")
#         print("4. Exit")

#         choice = input("Enter your choice (1-4): ")

#         if choice == '1':
#             check_balance(balance)
#         elif choice == '2':
#             amount = float(input("Enter amount to deposit: $"))
#             balance = deposit(balance,amount)
#         elif choice == '3':
#             amount = float(input("Enter amount to withdraw: $"))
#             balance = withdraw(balance,amount)
#         elif choice == '4':
#             print("Thank you for using the ATM. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# # Start the ATM
# menu()