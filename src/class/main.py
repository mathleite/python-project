from bank import Bank
from client import Client
from account import Account
from card import Card
from client_account import ClientAccount


def menu():
    print('\n### ', bank.get_name(), ' ###')
    print('\t======Menu======')
    print('\t 1 - Accounts')
    print('\t 2 - New Account')
    print('\t 3 - Clients')
    print('\t 4 - Bank Details')
    print('\t 5 - Cash Machine')
    print('\t 6 - Exit')
    choice = str(input('Option: '))

    if choice == '1':
        show_account(None, 'all_accounts')
    elif choice == '2':
        account_menu()
    elif choice == '3':
        show_client()
    elif choice == '4':
        bank_detail()
    elif choice == '5':
        cash_machine()
    elif choice == '6':
        exit(-1)
    else:
        print('This option does not exist')
        input("Press the <ENTER> key to continue...")


def show_account(debit_card, show_option):
    if show_option == 'all_accounts':
        print('\n\t==== Accounts ====')
        for accounts in client_account.get_account():
            print('Number account:{} | Balance:R${:10.2f} | Joint account:{} | Creation date:{}'.
                  format(accounts.get_account_number(), accounts.get_balance(), accounts.get_joint_account(),
                         accounts.get_creation_date()))
        input("Press the <ENTER> key to continue...")
    elif show_option == 'specific_account':
        print('\n{} | Joint account: {} | Account Number: {} | Creation Date: {} | Balance: R${:.2f}'.
              format(debit_card.get_account().get_bank().get_name(), debit_card.get_account().get_joint_account(),
                     debit_card.get_account().get_account_number(), debit_card.get_account().get_creation_date(),
                     debit_card.get_account().get_balance()))
        print('Holder(s)')
        for holder in debit_card.get_account().get_account_holder():
            if debit_card.get_holder() == holder:
                print('{:20}<<<'.format(holder.get_name()))
            else:
                print('{:20}'.format(holder.get_name()))


def account_menu():
    print('\n\t====Account Menu====')
    print('\t 1 - New Account')
    print('\t 2 - New registered client Account')
    print('\t 3 - Return')
    choice = str(input('Option: '))

    if choice == '1':
        client = new_client()
        account = new_account(client)
        print('Your debit card number is ', account.get_debit_card_number())
        input("Press the <ENTER> key to continue...")
    elif choice == '2':
        print('\n\t==== Find the registered Client ====')
        cpf = str(input('Cpf: '))
        client = find_client(cpf)
        if client is None:
            print('Client does not exist')
            input("Press the <ENTER> key to continue...")
        else:
            print('Client: {}'.format(client.get_name()))
            account = new_account(client)
            print('Your debit card number is ', account.get_debit_card_number())
            input("Press the <ENTER> key to continue...")
    elif choice == '3':
        return
    else:
        print('This option does not exist')
        input("Press the <ENTER> key to continue...")


def show_client():
    print('\n\t==== Clients ====')
    for clients in client_account.get_client():
        print('Name:{:20} | Cpf:{} | Date of Birth:{} | Client since:{}'.
              format(clients.get_name(), clients.get_cpf(), clients.get_date_of_birth(),
                     clients.get_registration_date()))
    input("Press the <ENTER> key to continue...")


def bank_detail():
    print('\n\t==== Bank Details ====')
    print('{} | President:{} | Address:{}'.format(bank.get_name(), bank.get_president(), bank.get_address()))
    input("Press the <ENTER> key to continue...")


def cash_machine():
    print('\n\t====Cash Machine====')
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
        show_account(debit_card, 'specific_account')
        asw = banking_operations(debit_card)


def new_client():
    print('\n\t==== Client Registration ====')
    test = True
    while test:
        name = str(input('Client name: '))
        date_of_birth = str(input('Date of birth: '))
        cpf = str(input('Cpf: '))
        if find_client(cpf) is not None:
            print('Client already registered.')
            input("Press the <ENTER> key to continue...")
        else:
            client = Client(name, date_of_birth, cpf)
            client_account.set_client(client)
            return client


def new_account(client):
    print('\n\t==== Account Registration ====')
    account_password = str(input('Account password: '))
    test = True
    while test:
        account_number = str(input('Account number: '))
        if find_account(account_number) is not None:
            print('This account already exists, try another.')
            test = True
        else:
            account = Account(bank, client, account_password, account_number, card)
            client_account.set_account(account)
            return account


def find_client(client_cpf):
    for client in client_account.get_client():
        if client_cpf == client.get_cpf():
            return client
    return None


def find_account(account_number):
    for account in client_account.get_account():
        if account_number == account.get_account_number():
            return account
    return None


def login(debit_card_number, password_account):
    for dc in card.get_debit_card():
        if dc.get_debit_card_number() == debit_card_number:
            for pw in dc.get_account().get_password():
                password = '{}{}'.format(dc.get_holder().get_cpf(), password_account)
                if pw == password:
                    return dc
    return None


def banking_operations(debit_card):
    print('\t1 - Deposit')
    print('\t2 - Withdraw')
    print('\t3 - Bank Transfer')
    print('\t4 - Add Holder')
    print('\t5 - Account Statement')
    print('\t6 - Return')
    choice = str(input('Option: '))

    if choice == '1':
        deposit(debit_card)
    elif choice == '2':
        withdraw(debit_card)
    elif choice == '3':
        bank_transfer(debit_card)
    elif choice == '4':
        add_holder(debit_card)
    elif choice == '5':
        account_statement(debit_card)
    elif choice == '6':
        return 'y'
    else:
        print('This option does not exist')
        input("Press the <ENTER> key to continue...")


def deposit(debit_card):
    print('\n\t====Deposit====')
    amount = float(input('Amount R$'))
    debit_card.get_account().deposit(debit_card.get_holder(), amount, 'Deposit')


def withdraw(debit_card):
    print('\n\t====Withdraw====')
    amount = float(input('Amount R$'))
    debit_card.get_account().withdraw(debit_card.get_holder(), amount, 'Withdraw')


def bank_transfer(debit_card):
    print('\n\t====Bank Transfer====')
    number_account = str(input('Number Account: '))
    account = find_account(number_account)
    if account is None:
        print('\nAccount does not exist')
    else:
        amount = float(input('Amount R$'))
        debit_card.get_account().bank_transfer(debit_card.get_holder(), account, amount)


def add_holder(debit_card):
    print('\n\t====Add Holder====')
    print('\t 1 - Registered Client')
    print('\t 2 - New Client')
    print('\t 3 - Return')
    choice = str(input('Option: '))

    if choice == '1':
        print('\n\t==== Find the registered Client ====')
        cpf = str(input('Cpf: '))
        client = find_client(cpf)
        if client is None:
            print('Client does not exist')
            input("Press the <ENTER> key to continue...")
        else:
            print('Client: {}'.format(client.get_name()))
            password = str(input('Password for access: '))
            debit_card.get_account().set_joint_account(client, password)
            print('Your debit card number is ', debit_card.get_account().get_debit_card_number())
            input("Press the <ENTER> key to continue...")
    elif choice == '2':
        client = new_client()
        password = str(input('Password for access: '))
        debit_card.get_account().set_joint_account(client, password)
        print('You debit card number is ', debit_card.get_account().get_debit_card_number())
        input("Press the <ENTER> key to continue...")
    elif choice == '3':
        return 
    else:
        print('This option does not exist')
        input("Press the <ENTER> key to continue...")


def account_statement(debit_card):
    print()
    for statement in debit_card.get_account().get_account_statements():
        print(statement, '\n')
    input("Press the <ENTER> key to continue...")


bank_name = str(input('Bank name: '))

president_name = str(input('President name: '))

bank = Bank(bank_name, president_name)

card = Card()

client_account = ClientAccount()

while True:
    menu()
