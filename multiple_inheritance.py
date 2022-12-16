class bank:

    def transaction(self):
        print('Total transaction value')
    def account_opening(self):
        print('This is show your bank opening status.')
    def deposite(self):
        print('This will show your deposite amount.')

class HDFC_bank(bank):
    def hdfc_to_icici(self):
        print('This will show your all the transactions.')


class ICICI_Bank(HDFC_bank):
    pass

i = ICICI_Bank()
i.account_opening()
i.transaction()
i.deposite()
i.hdfc_to_icici()