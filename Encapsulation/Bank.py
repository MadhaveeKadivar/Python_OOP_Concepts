class Bank:
    def __init__(self):
        """ 
        Description: 
            constructor
        Parameter:
            It takes one self as argument
        Return:
            None
        """
        self._balance = 100000 # Protected variable
class Operation(Bank):
    def withdraw(self,bal):
        """ 
        Description: 
            This function is used for withdraw money
        Parameter:
            It takes self and withdraw amount as argument
        Return:
            None
        """
        self._balance = self._balance - bal
    def credit(self,bal):
        """ 
        Description: 
            This function is used for credit money
        Parameter:
            It takes self and credit amount as argument
        Return:
            None
        """
        self._balance = self._balance + bal
    def get_balance(self):
        """ 
        Description: 
            This function is returning balance
        Parameter:
            It takes one self as argument
        Return:
            Balance
        """
        return self._balance

    
class Test:
    def get_balance(self):
        """ 
        Description: 
            This function is printing balance
        Parameter:
            It takes one self as argument
        Return:
            None
        """
        print(self._balance) # Not accesible _balance variable due to protected