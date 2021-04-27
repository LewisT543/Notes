                                #### EXTENDED EXAMPLE, GETS+SETS AND CUSTOM-BUILT-INS ####

from datetime import datetime

class AccountException(Exception):
    pass

class LoggingDict(dict):
    def __init__(self, *args, **kwargs):
        # Init the base dict uisng super()
        super().__init__(*args, **kwargs)
        # Init log list
        self.log = list()
        # log the timestamp of opperation
        self.log_timestamp('List created')
    
    def __getitem__(self, key):
        val = super().__getitem__(key)
        self.log_timestamp(f'Value: {val} for key: {key} retrieved')
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
        self.__transac_history = LoggingDict()
        self.__transac_history[f'{datetime.now()} \t Account Created'] = acc_num

    @property
    def account_number(self):
        self.__transac_history.log_timestamp(f'Accessing account number: {self.__acc_num}')
        now = datetime.now()
        self.__transac_history[f'{now} \t Account Number Accessed'] = self.__acc_num
        return self.__acc_num

    @account_number.setter
    def account_number(self, num):
        now = datetime.now()
        self.__transac_history[f'{now} \t Access Denied'] = num
        return AccountException('Cannot edit your account number.')

    @property
    def balance(self):
        self.__transac_history.log_timestamp(f'Accessing Balance: {self.__balance}')
        now = datetime.now()
        self.__transac_history[f' \t Balance Accessed'] = self.__balance
        return self.__balance

    @balance.setter
    def balance(self, num):
        if num < 0:
            msg = f'Tried and failed to set a negative balance. ({num})'
            raise AccountException('Cannot set negative balance.')     
        else:
            self.__balance = num
            msg = f'Balance Updated: {self.__balance}'
        self.__transac_history.log_timestamp(msg)
    
    @balance.deleter
    def balance(self):
        if self.__balance == 0:
            msg = 'Successfully deleting account.'
            del self
        else:
            msg = f'Tried and failed to delete account. Balance not 0. Current Balance: {self.__balance}'
            raise AccountException('Cant do that, balance is not 0') 
        self.__transac_history.log_timestamp(msg)
    
    def transact(self, amount):
        msg = f'Transaction successful. Amount: {amount}'
        if amount > 100000:
            print('Thats a heckin large transaction mate (>100000)')
            msg += '\t >>> LARGE TRANSACTION <<<'
        self.__balance += amount
        self.__transac_history.log_timestamp(msg)

    @property
    def get_history_dict(self):
        for key, val in self.__transac_history.items():
            self.__transac_history[key]

    @property
    def get_logs(self):
        return self.__transac_history.log
       

    @get_logs.deleter
    def get_logs(self):
        key_press = input('Type "Delete" to delete transaction history.')
        if key_press in ['Delete', 'delete']:
            del self.__transac_history.log


myac = BankAccount(11223344, 100)
myac.balance = 1000
myac.account_num = 22334455
myac.transact(10)
myac.transact(50)
myac.transact(-20)

print()


print(myac.balance)


