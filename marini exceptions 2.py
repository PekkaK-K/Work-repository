# Example file for Advanced Python by Joe Marini
# Working with basic exception handling

# Try to execute some code that might cause an exception:

try:
    num = input("Enter the first number: ")
    denom = input("Enter the second numnber: ")
    n = int(num)
    d = int(denom)
    result = n/d
except ZeroDivisionError as e:
    print("You can't divide by zero!")
    print(e)
except ValueError as e:
    print("You didn't give me a valid number!")
    print(e)
else:
    print(result)
finally:
    print("Thanks for playing!")

# Example file for Advanced Python by Joe Marini
# Programming challenge for working with Exceptions

class InvalidTempError(Exception):
    """Raised when the oven is set to an invalid temperature"""
    def __init__(self, temp):
        super().__init__(f"Invalid temperature setting: {temp}")

class DigitalOven:
    def __init__(self):
        self.temp = 0

    def set_temp(self, temp):
        if temp == 0:
            self.temp = 0
        elif temp < 100 or temp > 500:
            raise InvalidTempError(temp)
        self.temp = temp

    def get_temp(self):
        return self.temp

def test_oven(test_temp):
    global oven
    try:
        oven.set_temp(test_temp)
    except InvalidTempError as e:
        print(f"Error: {e}")
    else:
        print(f"New temp: {oven.get_temp()}")
    finally:
        print(f"Current temp setting is {oven.get_temp()}")

oven = DigitalOven()
test_oven(250)
test_oven(50)
test_oven(0)
test_oven(600)

# Example file for Advanced Python by Joe Marini
# Understanding the built-in exception classes in Python

import os

# IndexError occurs when you try to access an index that is out of range
int_list = [0,3,6,1,8,7,3,5]
print(int_list[10])


# KeyError is similar - it is raised when a key is not found in a Dictionary
my_dict = {1: "one", 2: "two", 3: "three"}
print(my_dict[4])


# FileNotFoundError is raised when you try to access a file that doesn't exist
with open("myfile.txt", "r") as my_file:
    print(my_file)


# FileExistsError is raised when a file or directory already exists
os.mkdir("testdir")
# NotADirectoryError is raised when try to perform a dir operation on a non-dir object
os.listdir("myfile.txt")

# Example file for Advanced Python by Joe Marini
# Defining and using custom exceptions in Python

# Define a custom exception class
class InsufficientFundsError(Exception):
    """Raised when the account balance is insufficient for a transaction."""
    def __init__(self, balance, amount):
        message = f"Insufficient balance: ${balance:.2f} (required: ${amount:.2f})"
        super().__init__(message)


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if (amount > self.balance):
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount

    def get_balance(self):
        return self.balance

# Create a bank account with an initial balance of $100
account = BankAccount(100)

try:
    account.deposit(10)
    # should work
    account.withdraw(50)
    # Attempt to withdraw $100, which exceeds the balance
    account.withdraw(100)
except InsufficientFundsError as e:
    print(f"Error: {e}")
else:
    print("Withdrawal successful.")
finally:
    print(f"Current balance: ${account.get_balance():.2f}")

    