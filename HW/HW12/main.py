from models import *
import pickle
import os


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

        input_ssn = input('Please enter your ssn')
        with open(f'/home/peaman/Desktop/MANA/PEAMAN/maktab-e sharif/maktab89/HW/HW12/Client/{input_ssn}.cli', 'rb') as client_info_file:
            client_info = pickle.load(client_info_file)

    elif use_type == 2:
        print('Registering')
        input_ssn = input('Please enter your ssn:')
        input_first_name = input('Please enter your firstName:')
        input_last_name = input('Please enter your lastName:')
        print('''
        select one ticket of ticket_type:
        \t1_one way ticket
        \t2_chargable ticket
        \t3_chargable and time zone ticket''')
        ticket_type = int(input())
        ticket = Ticket(ticket_type)
        client = Client(first_name=input_first_name, last_name=input_last_name, ssn=input_ssn)
        client.buy_ticket(ticket)
        with open(f'/home/peaman/Desktop/MANA/PEAMAN/maktab-e sharif/maktab89/HW/HW12/Client/{input_ssn}.cli', 'wb') as client_info_file:
            pickle.dump(client_info_file, client_info_file)
        # baiad user ro azash besazim

print('\t1_buy a ticket')
print('\t2_Trip')
print('\t3_exit')




client_amount = len(os.listdir('/home/peaman/Desktop/MANA/PEAMAN/maktab-e sharif/maktab89/HW/HW12/Client/'))
if client_amount <= 0:
    print('No any Client ')

else:
    print(f'There is/are {client_amount} client')



