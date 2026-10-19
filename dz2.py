class BankAccount:
    def __init__(self,account_number,blance):
        self.account_number = account_number
        self.blance = blance
        

    def deposit(self, amount):
        self.blance += amount
        print("Кошти успішно додано!")


    def withdraw(self,amount):
        if amount <= self.blance:
            self.blance -= amount
            print("Кошти успішно знято!")
        else:
            print("Недостатньо коштів на рахунку!")
 
         def display_info(self):
            print("Номер рахунку:", self.account_number)
            print("Баланс:", self.balance, "грн")


account = BankAccount("123456789", 1000)


account.display_info()
account.deposit(500)
account.withdraw(300)
account.display_info()