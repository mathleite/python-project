import os

from bank import Bank
from client import Client
from account import Account
from card import Card
from client_account import ClientAccount


def menu():
    print('\n', bank.get_name())
    print('====Menu====')
    print('1 - Accounts')
    print('2 - New Account')
    print('3 - Clients')
    print('4 - Bank Details')
    print('5 - Cash Machine')
    print('6 - Exit')
    choice = int(input('Option: '))

    if choice == 1:
        print()
        for accounts in client_account.get_account():
            print('Number account:{} | Balance:R${:15.2f} | Joint account:{} | Creation date:{}'.
                  format(accounts.get_account_number(), accounts.get_balance(), accounts.get_joint_account(),
                         accounts.get_creation_date()))
        input("Press the <ENTER> key to continue...")

    if choice == 2:
        print('\n====Account Menu====')
        print('1 - New Account')
        print('2 - New registered client Account')
        choice = int(input('Option: '))

        if choice == 1:
            name = str(input('Client name: '))
            date_of_birth = str(input('Date of birth: '))
            cpf = str(input('Cpf: '))
            account_password = str(input('Account password: '))
            account_number = str(input('Account number: '))
            new_account(name, date_of_birth, cpf, account_password, account_number)
            input("Press the <ENTER> key to continue...")
        elif choice == 2:
            client_cpf = str(input('Client cpf: '))
            client = find_client(client_cpf)
            if client is None:
                print('Client does not exist')
                input("Press the <ENTER> key to continue...")
            else:
                print('Client: {}'.format(client.get_name()))
                account_password = str(input('Account password: '))
                account_number = str(input('Account number: '))
                new_client_account(client, account_password, account_number)
                input("Press the <ENTER> key to continue...")

    if choice == 3:
        print()
        for clients in client_account.get_client():
            print('Name:{:20} | Cpf:{} | Date of Birth:{} | Client since:{}'.
                  format(clients.get_name(), clients.get_cpf(), clients.get_date_of_birth(),
                         clients.get_registration_date()))
        input("Press the <ENTER> key to continue...")

    if choice == 4:
        print('\n{} | President:{} | Address:{}'.format(bank.get_name(), bank.get_president(), bank.get_address()))
        input("Press the <ENTER> key to continue...")

    if choice == 5:
        cash_machine()

    if choice == 6:
        exit(-1)


def new_account(name, date_of_birth, cpf, account_password, account_number):
    client = Client(name, date_of_birth, cpf)
    account = Account(bank, client, account_password, account_number, card)
    client_account.set_client(client)
    client_account.set_account(account)


def new_client_account(registered_client, account_password, account_number):
    account = Account(bank, registered_client, account_password, account_number, card)
    client_account.set_account(account)


def find_client(cpf):
    for client in client_account.get_client():
        if cpf == client.get_cpf():
            return client
    return None


def find_account(number_account):
    for account in client_account.get_account():
        if number_account == account.get_account_number():
            return account
    return None


def login(debit_card_number, password_account):
    for dc in card.debit_card:
        if dc.debit_card_number == debit_card_number:
            for pw in dc.account.password:
                password = '{}{}'.format(dc.holder.get_cpf(), password_account)
                print(password)
                if pw == password:
                    return dc
    return None


def show_account(debit_card):
    print('\n{} | Joint account: {} | Account Number: {} | Creation Date: {} | Balance: {:.2f}'.
          format(debit_card.get_account().get_bank().get_name(), debit_card.get_account().get_joint_account(),
                 debit_card.get_account().get_account_number(), debit_card.get_account().get_creation_date(),
                 debit_card.account.get_balance()))
    print('Holder(s)')
    for holder in debit_card.get_account().get_account_holder():
        if debit_card.get_holder() == holder:
            print('{:20}<<<'.format(holder.get_name()))
        else:
            print('{:20}'.format(holder.get_name()))


def banking_operations(debit_card):
    print('1 - Deposit')
    print('2 - Withdraw')
    print('3 - Bank Transfer')
    print('4 - Add Holder')
    print('5 - Account Statement')
    print('6 - Return')
    choice = int(input('Option: '))

    if choice == 1:
        print('\n====Deposit====')
        amount = float(input('Amount R$'))
        debit_card.account.deposit(debit_card.get_holder(), amount, 'Deposit')
    if choice == 2:
        print('\n====Withdraw====')
        amount = float(input('Amount R$'))
        debit_card.account.withdraw(debit_card.get_holder(), amount, 'Withdraw')
    if choice == 3:
        print('\n====Bank Transfer====')
        number_account = str(input('Number Account: '))
        account = find_account(number_account)
        if account is None:
            print('\nAccount does not exist')
        else:
            amount = float(input('Amount R$'))
            debit_card.account.bank_transfer(debit_card.get_holder(), account, amount)
    if choice == 4:
        print('\n====Add Holder====')
        print('1 - Registered Client')
        print('2 - New Client')
        choice = int(input('Option: '))

        if choice == 1:
            cpf = str(input('Client cpf: '))
            client = find_client(cpf)
            password = str(input('Password: '))
            debit_card.account.set_joint_account(client, password)

        if choice == 2:
            name = str(input('Client name: '))
            date_of_birth = str(input('Date of birth: '))
            cpf = str(input('Cpf: '))
            password = str(input('Password: '))
            client = Client(name, date_of_birth, cpf)
            client_account.set_client(client)
            debit_card.account.set_joint_account(client, password)

    if choice == 5:
        print()
        for statement in debit_card.get_account().get_account_statements():
            print(statement, '\n')

    if choice == 6:
        return 0


def cash_machine():
    print('\n====Cash Machine====')
    print('Login with Debit card and password')
    debit_card_number = str(input('Debit Card number:'))
    password = str(input('Password: '))
    debit_card = login(debit_card_number, password)

    if debit_card is None:
        print('Account does not exist')
        input("Press the <ENTER> key to continue...")
        return

    asw = 'n'

    while asw != 'y':
        show_account(debit_card)
        banking_operations(debit_card)
        asw = str(input('Exit? [y/n] '))


bank_name = str(input('Bank name: '))

president_name = str(input('President name: '))

bank = Bank(bank_name, president_name)

card = Card()

client_account = ClientAccount()

while True:
    menu()
