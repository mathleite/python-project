class President:
    name = str(None)

    def __init__(self, name, bank):
        self.set_name(name)
        self.bank_president = bank

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
