from pydantic import BaseModel, validator
class User(BaseModel):
    username: str
    password: str
    email: str
    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('your password must be longer than 8 letters')

user_data = {}

all_user = []

while True:
    username1 = input('input username:')
    if username1 == 'exit':
        break
    password = input('input password')
    email = input('input email')


    user_data['username'] = username1
    user_data['password'] = password
    user_data['email'] = email
    new_user = User(**user_data)
    if all_user:
        for user in all_user:
            print(type(user))
            if new_user.username == user.username:
                print(new_user.username)
                print(user.username)
                print('user already exists')
                break
            else:
                all_user.append(new_user)
                break
    else:
        all_user.append(new_user)
    print(all_user)




