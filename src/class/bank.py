from president import President


class Bank:
    name = str(None)
    address = str('Endereço: ')
    street = str('Rua Oswaldo Luiz da Silva,')
    number = str('número 585,')
    neighborhood = str('bairro Jd. Lugar Nenhum,')
    state = str('estado Sem Saber - (SS).')

    def __init__(self, bank_name, president_name):
        self.set_name(bank_name)
        self.president = President(president_name, self)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_address(self):
        return self.street, self.number, self.neighborhood, self.state

    def get_president(self):
        return self.president.get_name()
