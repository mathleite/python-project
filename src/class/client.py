import time


class Client:
    def __init__(self, name, date_of_birth, cpf):
        self.name = name
        self.date_of_birth = date_of_birth
        self.cpf = cpf
        self.registration_date = time.strftime('%d/%b/%Y')

    def get_name(self):
        return self.name

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_cpf(self):
        return self.cpf

    def get_registration_date(self):
        return self.registration_date
