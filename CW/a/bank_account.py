import re

import bank_account


class Customer:
    def __init__(self, first_name, last_name, phone, email) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def cfname(fn):
        assert fn.isalpha(), 'your name is invalid'

    @staticmethod
    def clname(ln):
        assert ln.isalpha(), 'your last name is invalid'

    @staticmethod
    def cphone(pn):
        assert pn.isnumeric(), 'your phone is invalid'

    @staticmethod
    def cemail(em):
        email = re.match(r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9]"
                                    r"(?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?", em)
        assert email is not None, 'your email is invalid'


class BankAccount:
    WAGE_AMOUNT = 0  # کارمزد
    MIN_BALANCE = 1000  # حداقل موجودی

    class MinBalanceError(Exception):
        pass

    def __init__(self, owner: Customer, initial_balance: int = 0) -> None:
        self.__owner = owner  # صاحب حساب
        self.__balance = None
        self.yechi(initial_balance)

    def yechi(self, x):
        # self.balance = x
        assert type(x) == int and x >= self.MIN_BALANCE, 'invalid amount'
        self.__balance = x

    def check_minimum_balance(self, amount_to_withdraw):  # چک کردن حداقل موجودی
        assert type(amount_to_withdraw) == int and (self.__balance - amount_to_withdraw) >= self.MIN_BALANCE , 'you can not withdraw'
        return (self.__balance - int(amount_to_withdraw)) >= self.MIN_BALANCE

    def set_owner(self, owner):  # تغییر صاحب حساب
        self.__owner = owner

    def get_owner(self):  # مشاهده صاحب حساب
        return self.__owner

    def withdraw(self, amount):  # برداشت وجه
        print('*' * 60)
        if self.check_minimum_balance(amount):
            self.__balance -= amount
            self.__balance -= self.WAGE_AMOUNT
            print('salam' * 60)
        else:
            raise bank_account.BankAccount.MinBalanceError('your balance is not enough')

    def deposit(self, amount):  # واریز وجه
        assert type(amount) == int, 'invalid amount'
        self.__balance += amount

    def get_balance(self):  # مشاهده موجودی
        self.__balance -= self.WAGE_AMOUNT   # برداشت کارمزد
        return self.__balance

    def transfer(self, target_account, amount: int):  # انتقال وجه
        assert isinstance(target_account, BankAccount), 'your target not found'
        self.withdraw(amount)  # برداشت از حساب خود
        target_account.deposit(amount)  # واریز به حساب مقصد
        print('*'*60)
    @classmethod
    def change_wage(cls, new_amount):
        assert type(new_amount) == int and new_amount >= 0, 'invalid amount'
        cls.WAGE_AMOUNT = max(new_amount, 0)   # حداقل مقدار برابر صفر است

    @classmethod
    def change_min_balance(cls, new_amount):
        assert type(new_amount) == int and new_amount >= 0, 'invalid amount'
        cls.MIN_BALANCE = max(new_amount, 0)  # حداقل مقدار برابر صفر است


