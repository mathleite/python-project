import time
from debit_card import DebitCard


class Account:
    def __init__(self, bank, holder, password, account_number, card):
        self.bank = bank
        self.account_holder = []
        self.account_holder.append(holder)
        self.password = []
        self.set_password(holder, password)
        self.account_number = account_number
        self.balance = float(0)
        self.joint_account = bool(False)
        self.account_statements = []
        self.creation_date = time.strftime('%d/%b/%Y')
        self.card = card
        self.new_debit_card(self.card, holder)

    def get_bank(self):
        return self.bank

    def get_account_holder(self):
        return self.account_holder

    def get_password(self):
        return self.password

    def set_password(self, holder, password):
        pw = '{}{}'.format(holder.get_cpf(), password)
        self.password.append(pw)

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_balance(self):
        return self.balance

    def deposit(self, holder, amount, description):
        if amount <= 0:
            return False  # "---It's not possible to deposit this value.---"
        current_balance = self.balance
        self.balance += amount
        self.set_account_statements(holder, current_balance, description, '+', amount)
        return True  # "---The deposit was successful.---"

    def withdraw(self, holder, amount, description):
        if amount <= 0:
            return False  # "---This value cannot be withdrawn.---"
        elif amount > self.balance:
            return False  # "---Insufficient balance.---"
        current_balance = self.balance
        self.balance -= amount
        self.set_account_statements(holder, current_balance, description, '-', amount)
        return True  # "---The withdrawal was successful.---"

    def bank_transfer(self, holder, account, amount):
        if self.withdraw(holder, amount, 'Transference'):
            account.deposit(None, amount, 'Transference')
            return True
        return False

    def get_joint_account(self):
        return self.joint_account

    def set_joint_account(self, new_holder, password):
        self.joint_account = True
        self.account_holder.append(new_holder)
        self.set_password(new_holder, password)
        # new_holder.account.append(self)
        self.new_debit_card(self.card, new_holder)

    def get_account_statements(self):
        return self.account_statements

    def set_account_statements(self, holder, balance, description, operation, amount):
        account_statement = "Date: {}\n" \
                         "Holder:  {}\n" \
                         "        {:>11}{:.2f} \n" \
                         "{:15} {}R${:.2f} \n" \
                         "------------------------- \n" \
                         "Balance: {:>10}{:.2f}".format(time.strftime('%H:%M on %d/%b/%Y'),
                                                        (None if holder is None else holder.name), 'R$', balance,
                                                        description, operation, amount, 'R$', self.balance)
        self.account_statements.append(account_statement)

    def get_creation_date(self):
        return self.creation_date

    def get_debit_card_number(self):
        return '{}-{}'.format(self.account_number, len(self.account_holder))

    def new_debit_card(self, card, holder):
        debit_card = DebitCard(self, holder, self.get_debit_card_number())
        card.debit_card.append(debit_card)

    def pay_the_bills(self, value, holder):
        if self.withdraw(value, holder, 'Paid Account'):
            return True
        return False
