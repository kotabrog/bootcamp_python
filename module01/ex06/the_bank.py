class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if not hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class BankError(Exception):
    def __init__(self, text=""):
        self.text = text

    def __str__(self):
        return "Bank Error\n" + self.text


class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def _take_account(self, inf):
        if type(inf) is int:
            for i, account in enumerate(self.account):
                if type(account) is Account and hasattr(account, 'id')\
                   and inf == account.id:
                    return i
        elif type(inf) is str:
            for i, account in enumerate(self.account):
                if type(account) is Account and hasattr(account, 'name')\
                   and inf == account.name:
                    return i
        return -1

    def _is_corrupted(self, account):
        try:
            attribute_list = dir(account)
            if len(attribute_list) % 2 == 0:
                return True
            zip_or_addr_flag = False
            if not hasattr(account, 'name')\
               or not hasattr(account, 'id')\
               or not hasattr(account, 'value'):
                return True
            for attribute in attribute_list:
                if attribute.startswith('b'):
                    return True
                if attribute.startswith('zip') or attribute.startswith('addr'):
                    zip_or_addr_flag = True
            if not zip_or_addr_flag:
                return True
            return False
        except Exception:
            return True

    def transfer(self, origin, dest, amount):
        """
            @origin:  int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return         True if success, False if an error occured
        """
        try:
            if type(origin) not in [int, str] or type(dest) not in [int, str]:
                raise BankError()
            origin_index = self._take_account(origin)
            dest_index = self._take_account(dest)
            if origin_index == -1 or dest_index == -1:
                raise BankError()
            if self._is_corrupted(self.account[origin_index])\
               or self._is_corrupted(self.account[dest_index]):
                raise BankError()
            amount = float(amount)
            if amount < 0 or self.account[origin_index].value < amount:
                raise BankError()
            self.account[origin_index].transfer(-amount)
            self.account[dest_index].transfer(amount)
            return True
        except (BankError, Exception):
            return False

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
        """
        try:
            if type(account) not in [int, str]:
                raise BankError()
            account_index = self._take_account(account)
            if account_index == -1:
                raise BankError()
            account = self.account[account_index]
            if not hasattr(account, 'name'):
                setattr(account, 'name', 'name')
            if not hasattr(account, 'id'):
                has_id_list = [i for i, acc in enumerate(self.account)
                               if hasattr(acc, 'id')]
                id_list = [self.account[i].id for i in has_id_list]
                setattr(account, 'id', max(id_list) + 1)
            if not hasattr(account, 'value'):
                setattr(account, 'value', 0)
            zip_or_addr_flag = False
            for attribute in dir(account):
                if attribute.startswith('zip') or attribute.startswith('addr'):
                    zip_or_addr_flag = True
                if attribute.startswith('b'):
                    delattr(account, attribute)
            if not zip_or_addr_flag:
                setattr(account, 'zip', 'zip')
            if len(dir(account)) % 2 == 0:
                add_attribute = 'a'
                while hasattr(account, add_attribute):
                    add_attribute += 'a'
                setattr(account, add_attribute, 'temp')
            return True
        except (BankError, Exception):
            return False


if __name__ == '__main__':
    bank = Bank()
    bank.add(Account(
        'Smith Jane',
        zip='911-745',
        value=1000.0,
        ref='1044618427ff2782f0bbece0abd05f31'
    ))
    bank.add(Account(
        'William John',
        # zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        bnf=None,
    ))
    bank.add(Account(
        3.0,
        zip='100-064',
        value=6460.0,
        ref='58ba2b9954cd278eda8a84147ca73c87',
        info=None
    ))
    delattr(bank.account[1], 'id')
    delattr(bank.account[1], 'value')
    amount = 100
    print(bank.transfer(2.0, 'a', amount))
    print(bank.transfer('Smith Jane', 'William John', amount))
    print(bank.fix_account('William John'))

    print(bank.transfer('Smith Jane', 'William John', amount))

    print(dir(bank.account[1]))
    print(len(dir(bank.account[1])))
    print(bank.account[0].value)
    print(bank.account[1].value)
