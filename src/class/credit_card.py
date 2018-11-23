class CreditCard:
    def __init__(self, holder, income, credit_card_number, password):
        self.holder = holder
        self.limit_used = float(0)
        self.credit_limit = float(0)
        self.set_credit_limit(income)
        self.credit_card_number = credit_card_number
        self.password = password
        self.credit_card_bill = []

    def get_holder(self):
        return self.holder

    def get_credit_card_bill(self):
        return self.credit_card_bill

    def set_credit_card_bill(self, amount, description):
        credit_card_bill = '{:10} - R${:5.2f}\n{}'.format(description, amount, '-' * 25)
        self.credit_card_bill.append(credit_card_bill)

    def get_credit_limit(self):
        return self.credit_limit

    def set_credit_limit(self, income):
        self.credit_limit = income * 0.30

    def get_credit_limit_used(self):
        return self.limit_used

    def get_credit_card_number(self):
        return self.credit_card_number

    def get_password(self):
        return self.password

    def pay_with_credit_card(self, amount, description):
        if self.credit_limit - self.limit_used >= amount:
            self.limit_used += amount
            self.set_credit_card_bill(amount, description)
            return True
        return False

    def credit_card_bill_paid(self):
        self.limit_used = 0
        self.credit_card_bill = []
