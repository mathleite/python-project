from president import President


class Bank:
    name = str(None)
    address = str('Endereço: ')
    street = str('Rua Oswaldo Luiz da Silva,')
    number = str('número 585,')
    neighborhood = str('bairro Jd. Lugar Nenhum,')
    state = str('estado Sem Saber - (SS).')

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_address(self):
        print(self.street, self.number, self.neighborhood, self.state)


bank = Bank()
president = President()
bank.get_address()
