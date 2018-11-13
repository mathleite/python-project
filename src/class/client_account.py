class ClientAccount:
    def __init__(self):
        self.client = []
        self.account = []

    def get_client(self):
        return self.client

    def set_client(self, client):
        self.client.append(client)

    def get_account(self):
        return self.account

    def set_account(self, account):
        self.account.append(account)
