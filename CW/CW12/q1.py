import argparse
import pickle
import datetime


class User:
    def __init__(self, fname, lname, age, phone_number, email):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.phone_number = phone_number
        self.email = email

class Super(User):
    def __init__(self, fname, lname, age, phone_number, email,admin):
        super().__init__(fname, lname, age, phone_number, email)
        self.admin = admin



parser = argparse.ArgumentParser(prog="our_action", description="action:")

parser.add_argument("-cu", "--create_user", action="store_true")
parser.add_argument("-o", "--owner", action="store_true")
parser.add_argument("-sl", "--show_list", action="store_true")
parser.add_argument("-bu", "--back_up", action="store_true")

parser.add_argument("-r", "--restore", action="store_true")
parser.add_argument("-fn", "--file_name", action="store")





# parser.add_argument("-cu","--r",action="store_true")
# dict = {}
# with open("user.txt","wb") as u:
#     pickle.dump(dict,u)

args = parser.parse_args()


#1
if args.create_user:
    fname = input("enter the first name: ")
    lname = input("enter the last name: ")
    age = int(input("enter the age: "))
    phone_number = input("enter the phone number: ")
    email = input("enter the email: ")

    with open("user.txt","rb") as u:
        dict1 = pickle.load(u)

    with open("user.txt","wb") as u:
        dict1[phone_number] = User(fname, lname, age, phone_number, email)
        pickle.dump(dict1,u)

    # pickle.dump(User(fname, lname, age, phone_number, email), open("user.txt", "ab"))
#2
if args.owner:
    fname = input("enter the first name: ")
    lname = input("enter the last name: ")
    age = int(input("enter the age: "))
    phone_number = input("enter the phone number: ")
    email = input("enter the email: ")
    with open("admin.txt","rb") as u:
        dict1 = pickle.load(u)

    with open("admin.txt","wb") as u:
        dict1[phone_number] = User(fname, lname, age, phone_number, email)
        pickle.dump(dict1,u)
#3
if args.show_list:
    with open("user.txt","rb") as u:
        users = pickle.load(u)
        for i in users:
            print(users[i].__dict__)
#4
if args.back_up:

    with open("user.txt","rb") as u:
        text = pickle.load(u)
        today = datetime.datetime.now()
        # filename = datetime.date.today()
        filename = f"{today.year}-{today.month}-{today.day}.txt"
        with open(filename,"wb") as bu:
            pickle.dump(text,bu)
#5
if args.restore:

    file_name = f"{args.file_name}.txt"

    with open(file_name,"r") as f:
        text = f.read()
        print(text)





