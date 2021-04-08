                                #### EXAMPLE GETTERS AND SETTERS ####


class AccountException(Exception):
    pass

class BankAccount():
    def __init__(self, acc_num, balance):
        self.__acc_num = acc_num
        self.__balance = balance

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

    @balance.deleter
    def balance(self):
        if self.__balance == 0:
            del self
        else:
            raise AccountException('Cant do that, balance is not 0')
    
    def transact(self, amount):
        if amount > 100000:
            print('Thats a heckin large transaction mate (>100000)')
        self.__balance += amount


myac = BankAccount(11223344, 100)
print(myac.balance)
myac.balance = 1000
print(myac.balance)
#myac.balance = -200

myac.account_number = 22334455
myac.transact(1000000)
print(myac.balance)
del myac
