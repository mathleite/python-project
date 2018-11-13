class DebitCard:
    def __init__(self, account, holder, number):
        self.account = account
        self.holder = holder
        self.debit_card_number = number

    def get_holder(self):
        return self.holder

    def get_account(self):
        return self.account

    def get_debit_card_number(self):
        return self.debit_card_number

    def deposit(self, amount):
        if not self.account.deposit(self.holder, amount, 'D.C. deposit'):
            return False

    def withdraw(self, amount):
        if not self.account.withdraw(self.holder, amount, 'D.C. withdraw'):
            return False

    def pay_the_bills(self, value):
        if not self.account.pay_the_bills(value):
            return False
