class Card:
    def __init__(self):
        self.debit_card = []
        self.credit_card = []

    def set_debit_card(self, debit_card):
        self.debit_card.append(debit_card)

    def get_debit_card(self):
        return self.debit_card

    def set_credit_card(self, credit_card):
        self.credit_card.append(credit_card)

    def get_credit_card(self):
        return self.credit_card
