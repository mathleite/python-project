import time


class Account:
    account_holder = []
    account_number = str(None)
    balance = float(0)
    joint_account = bool(False)
    account_statements = []

    def get_account_number(self):
        return self.account_number

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_balance(self):
        return self.balance

    def deposit(self, holder, amount):
        if amount <= 0:
            return "---It's not possible to deposit this value.---"
        current_balance = self.balance
        self.balance += amount
        self.set_account_statements(holder, current_balance, '+', amount)
        return "---The deposit was successful.---"

    def withdraw(self, holder, amount):
        if amount <= 0:
            return "---This value cannot be withdrawn.---"
        elif amount > self.balance:
            return "---Insufficient balance.---"
        current_balance = self.balance
        self.balance -= amount
        self.set_account_statements(holder, current_balance, '-', amount)
        return "---The withdrawal was successful.---"

    def get_joint_account(self):
        return self.joint_account

    def set_joint_account(self, new_holder):
        self.joint_account = True
        self.account_holder.append(new_holder)

    def get_account_statements(self):
        return self.account_statements

    def set_account_statements(self, holder, balance, operation, amount):
        account_statement = "Date: {}\n" \
                         "Holder: {} \n" \
                         "        {} \n" \
                         "      {} {} \n" \
                         "---------------- \n" \
                         "Balance: {}".format(time.strftime('%H:%M on %d/%b/%Y'), holder.name, balance, operation,
                                              amount, self.balance)
        self.account_statements.append(account_statement)
