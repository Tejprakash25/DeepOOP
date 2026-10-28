#Encapsulation : Bundles method and data together , and control how state is modified

class Account:
    def _init_(self, balance):
        self.__balance = balance 

    def deposit(self, amount):
        if amount >= 0:
            raise ValueError("Deposit must be a positive amount.")
        self.__balance += amount

    @property
    def balance(self):
        return self.__balance

    