#Encapsulation : Bundles method and data together , and control how state is modified

class Account:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount >= 0:
            raise ValueError("Deposit must be a positive amount.")
        self.__balance += amount

    @property
    def balance(self):
        return self.__balance

#Inheritance : Allows a class to inherit attributes and methods from another class

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def fetch(self):
        return "Fetching the ball!"

dog = Dog()
print(dog.speak())
print(dog.fetch())

#Polymorphism : Different classes expose the same operation but implement it differently.

class CardPayment:
    def pay(self, amount):
        return f"Card: {amount}"

class UPIPayment:
    def pay(self, amount):
        return f"UPI: {amount}"

def checkout(payment, amount):
    return payment.pay(amount)

print(checkout(CardPayment(), 500))
print(checkout(UPIPayment(), 500))