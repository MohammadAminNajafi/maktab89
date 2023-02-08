from models import *
import pickle
import os
# with open('user.pickle', 'wb') as u:
#     dict1 = {}
#     pickle.dump(dict1, u)
def update_data(input_client: Client):
    assert isinstance(input_client, Client)
    with open("user.pickle", "rb") as u:
        dict1 = pickle.load(u)

    with open("user.pickle", "wb") as u:
        dict1[input_client.ssn] = Client(input_client.first_name, input_client.last_name, input_client.ssn)
        pickle.dump(dict1, u)
print('Welcome to the metro of Tehran ')
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
        with open(f'client.pickle', 'rb') as client_info_file:
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
        update_data(client)

        #ravel_time = int(input())

        with open(f'client.pickle', 'wb') as client_info_file:
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
        Gate = Gate()
        Gate.process_ticket(client, selected_ticket_type)
        update_data(client)
    elif option == 3:
        pass









