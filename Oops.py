class AccountHolder:
    def __init__(self, account_number, account_holder_name, account_balance, type_of_account):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.account_balance = account_balance
        self.type_of_account = type_of_account

    def display_account_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder Name: {self.account_holder_name}")
        print(f"Account Balance: Rs. {self.account_balance}")
        print(f"Type of Account: {self.type_of_account}")
        

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Successfully deposited Rs.{amount} and Available Balance: Rs.{self.account_balance}")
        else:
            print("Invalid deposit amount. Please enter correct value.")

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Sucessful withdraw Rs.{amount} and Available balance Rs.{self.account_balance}")
        else:
            print(f"Invalid amount entered, unable to withdraw")
        
account = AccountHolder("123456789", "Prashanth", 15000, "Savings")

account.display_account_details()
account.deposit(500)
account.withdraw(800)
account.withdraw(1000)
account.withdraw(200)
