from datetime import datetime


class TimeList(list):
    @staticmethod
    def add_timestamp(txt):
        now = datetime.now().strftime("%Y-%m-%d (%H:%M:%S)")
        return f'{now}   >>>   {txt} '

    def __setitem__(self, index, value):
        value = TimeList.add_timestamp(value)
        list.__setitem__(self, index, value)

    def append(self, value):
        value = TimeList.add_timestamp(value)
        list.append(self, value)

    def insert(self, index, value):
        value = TimeList.add_timestamp(value)
        list.insert(self, index, value)


class AccountException(Exception):
    pass

class BankAccount:
    def __init__(self, acc_num, balance):
        self.__acc_num = acc_num
        self.__balance = balance
        self.__history = TimeList()
        self.__history.append('Account Created')

    @property
    def account_number(self):
        return self.__acc_num

    @account_number.setter
    def account_number(self, num): 
        return AccountException('Cannot edit your account number.')

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, num):
        if num < 0:
            raise AccountException('Cannot set negative balance.')
        else:
            self.__balance = num
            self.__history.append(f'Updated Balance: {self.__balance}')

    @balance.deleter
    def balance(self):
        if self.__balance == 0:
            self.__history = None
        else:
            raise AccountException('Cant do that, balance is not 0')

    @property
    def history(self):
        return self.__history
    
    def transact(self, amount):
        if self.__balance + amount < 0:
            raise AccountException('Insufficient funds')
        if amount > 100000 or amount < -100000:
            print('Thats a heckin large transaction mate (>100000)')
            self.__history.append(f'Large Transaction detected, Size: {amount}')
        self.__balance += amount
        self.__history.append(f'Transaction Succesful, Balance: {self.__balance}')


def neat_history(BA_obj):
    for i in BA_obj.history:
        print(i)

myac = BankAccount(1234, 10)
myac.transact(10)
myac.transact(20)
myac.transact(-10)
myac.transact(50)
myac.transact(124231)

neat_history(myac)

