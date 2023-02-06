from models import *
import pickle
import os


print('Welcome to the metro of Tehran ')
client_amount = len(os.listdir('/home/peaman/Desktop/MANA/PEAMAN/maktab-e sharif/maktab89/HW/HW12/Client/'))
if client_amount <= 0:
    print('No any Client ')

else:
    print(f'There is/are {client_amount} client')

print('1_Client login')
print('2_Admin login')

while True:
    login_type = int(input('please select[1, 2]:'))
    if login_type in [1, 2]:
        break
    else:
        print('Please enter valid input')


if login_type == 1:
    print('\t1_login')
    print('\t2_signup')
    while True:
        use_type = int(input('please select[1, 2]:'))
        if use_type in [1, 2]:
            break
        else:
            print('Please enter valid input')

    if use_type == 1:

        input_ssn = input('Please enter your ssn:')
        with open(f'/home/peaman/Desktop/MANA/PEAMAN/maktab-e sharif/maktab89/HW/HW12/Client/{input_ssn}.cli', 'rb') as client_info_file:
            client = pickle.load(client_info_file)
            print(client.first_name)##

    elif use_type == 2:
        print('Registering')
        input_ssn = input('Please enter your ssn:')
        input_first_name = input('Please enter your firstName:')
        input_last_name = input('Please enter your lastName:')
        print('''
        \t1_one way ticket
        \t2_chargable ticket
        \t3_chargable and time zone ticket''')
        ticket_type = int(input('select one ticket of ticket_type:'))
        ticket = Ticket(ticket_type)
        client = Client(first_name=input_first_name, last_name=input_last_name, ssn=input_ssn)
        client.buy_ticket(ticket)
        with open(f'/home/peaman/Desktop/MANA/PEAMAN/maktab-e sharif/maktab89/HW/HW12/Client/{input_ssn}.cli', 'wb') as client_info_file:
            pickle.dump(client, client_info_file)
        # baiad user ro azash besazim

    print('\t1_buy a ticket')
    print('\t2_Trip')
    print('\t3_exit')

    option = int(input())
    for ticket in client.tickets:
        if ticket.status:
            print(ticket.ticket_type)

    print('Choose one of ticket types: ')
    selected_ticket_type = int(input())
    if option == 1:
        pass
    elif option == 2:
        bank_account_management = BankAccountManagement()
        bank_account_management.process_ticket(client, selected_ticket_type)
    elif option == 3:
        pass







