import datetime
import os
import psycopg2

connection = psycopg2.connect(
    database="CW16",
    user="postgres",
    password="  ",
    host="127.0.0.1",
    port=""
)


def clear(): os.system('cls' or 'clear')


# cur.execute("""CREATE TABLE users(
# 	id SERIAL PRIMARY KEY,
# 	username VARCHAR(50) UNIQUE NOT NULL,
# 	password VARCHAR(100) NOT NULL,
# 	created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
# );""")
#
# cur.execute("""CREATE TABLE posts(
# id SERIAL PRIMARY KEY,
# user_id INTEGER REFERENCES users(id),
# title VARCHAR(100) NOT NULL,
# body TEXT NOT NULL,
# created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
# );""")

def create_user():
    clear()
    user_name = input("Write your user name: ")
    user_password = input("Write your user password: ")
    cur = connection.cursor()
    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (user_name, user_password))
    connection.commit()
    cur.close()
    print("Account created.")
    input("Press enter to continue...")


def login():
    clear()
    user_name = input("Write your user name: ")
    cur = connection.cursor()
    cur.execute("SELECT * FROM users WHERE username = '%s'" % user_name)
    if user_info := list(cur.fetchall()):
        cur.close()
        user_password = input("Write your user password: ")
        # print(user_info, type(user_info))
        if user_info[0][2] == user_password:
            user_menu(user_info)
        else:
            print("Invalid password.")
    else:
        print('Invalid user name.')


def make_post(user_id):
    cur = connection.cursor()
    title = input("Write the title: ")
    body = input("Write the body: ")
    cur.execute("INSERT INTO posts(user_id, title, body) VALUES (%s, %s, %s)", (user_id, title, body))
    connection.commit()
    cur.close()
    print("Post created successfully.")
    input("Press enter to continue...")


def view_all_posts():
    clear()
    cur = connection.cursor()
    cur.execute("SELECT title, body FROM posts ORDER BY created_at DESC")
    for title, body in cur.fetchall():
        print(f"{title}: {body}.")
    cur.close()
    input("Press enter to continue...")


def view_all_my_posts(owner_id):
    clear()
    cur = connection.cursor()
    cur.execute("SELECT title, body FROM posts WHERE user_id = '%s' ORDER BY created_at DESC" % owner_id)
    for title, body in cur.fetchall():
        print(f"{title}: {body}.")
    cur.close()
    input("Press enter to continue...")


def user_menu(user_info):
    clear()
    while True:
        print("""
What do you want to do:
    1) Post something
    2) View my posts
    3) View all posts
        """)
        choice = input(">>>: ")
        if choice == '1':
            make_post(user_info[0][0])
        elif choice == '2':
            view_all_posts()
        elif choice == '3':
            view_all_my_posts(user_info[0][0])


def main_menu():
    clear()
    while True:
        print("""
Hello, What do you want to do.
    1) Log in
    2) Sign up
        """)
        choice = input(">>>:")
        if choice == '1':
            login()
        elif choice == '2':
            create_user()


main_menu()
