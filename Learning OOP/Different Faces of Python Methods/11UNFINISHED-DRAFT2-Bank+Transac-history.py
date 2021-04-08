from datetime import date, datetime

class AccountException(Exception):
    pass

class LoggingDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = list()
        self.log_timestamp('List created')

    def __getitem__(self, key):
        val = super().__getitem__(key)
        self.log_timestamp
        return val

    def __setitem__(self, key, val):
        super().__setitem__(key, val)
        self.log_timestamp(f'Set value: {val} to key: {key}')

    def log_timestamp(self, txt):
        timestampStr = datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")
        self.log.append(f'{timestampStr}: {txt}')



class BankAccount:
    
    def __init__(self, acc_num, balance):
        self.__acc_num = acc_num
        self.__balance = balance
        self.trans_hist = LoggingDict()
        self.trans_hist[datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")] = f'Account created, ({self.__acc_num}).'

    @property
    def account_num(self):
        self.trans_hist[datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")] = f'Account accessed, ({self.__acc_num}).'
        return self.__acc_num

    @account_num.setter
    def account_num(self, num):
        self.trans_hist[datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")] = 'Denied. Cannot change account number.'
        return AccountException('Cannot change account number.')

    @property
    def balance(self):
        self.trans_hist[datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")] = f'Balance accessed, ({self.__balance})'
        return self.__balance

    @balance.setter
    def balance(self, num):
        if num < 0:
            self.trans_hist[datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")] = f'Denied. Tried to set negatibe balance, ({self.__balance}).'
            raise AccountException('Tried to set negatibe balance.')
        else:
            self.__balance = num
            self.trans_hist[datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")] = f'Balance updated, ({self.__balance})'
    
    @balance.deleter
    def balance(self):
        if self.__balance == 0:
            self.trans_hist[datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")] = f'Successfully deleting account, ({self.__acc_num})'
            del self
        else:
            self.trans_hist[datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")] = f'Tried and failed to delete account. Balance not 0. Current Balance, {self.__balance}'
            raise AccountException('Cant do that, balance is not 0')
    
    def transaction(self, amount):
        if self.__balance + amount < 0:
            self.trans_hist[datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")] = f'Tried to withdraw more than in account, {self.__balance}'
            raise AccountException('Tried to withdraw more than in account.')
        else:
            if amount > 100000 or amount < -100000:
                self.trans_hist[datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")] = f'Large transaction, {amount}'
            self.__balance += amount
            self.trans_hist[datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")] = f'Transaction successful, {self.__balance}'



myac = BankAccount(11223344, 100)
myac.balance = 1000
myac.account_num = 22334455
myac.transaction(10)
myac.transaction(50)
myac.transaction(-20)

