# In this assignment you will help a new bank get up and running. 
# This bank has two kinds of accounts, a savings account and a debit account. 
# You will need to use inheritance in this assignment 
# so you will need to figure out what the account types have in common 
# and what they don´t. 
# The accounts should have a method called update_balance() which updates the balance.

# A savings account updates the balance as follows:

# It updates the balance by its yearly interest rate and adds a bonus rate to it.
#  For a savings account the interest rate is 5% and the bonus rate is 10%.

# A debet account updates the balance as follows:
# It updates the balance by its yearly interest rate which is 2 %.
# HINT: think about using class variables for the constants (interest rate and bonus rate).

# You also need to implement the __str__() method. 
# Think about where you should implement it. 
# You only need to implement it once. 
# Look at the output example here below to figure out what string the method should return.

# You also need to implement the functions print_accounts() 
# which should print each account and update_accounts() which should update each account.


class Account():
    def __init__(self,balance):
        self.balance = balance
    
    def __str__(self):
        return "Balance: {:.2f}".format(self.balance)


class SavingsAccount(Account):
    INTEREST_RATE = 0.05
    BONUS_RATE = 0.1

    def update_balance(self):
        self.balance += self.balance * (self.INTEREST_RATE + self.BONUS_RATE)
        return self.balance 

class DebitAccount(Account):
    INTEREST_RATE = 0.02

    def update_balance(self):
        self.balance += self.balance * self.INTEREST_RATE 
        return self.balance 
    



s1 = SavingsAccount(1000)
d1 = DebitAccount(1000)
s2 = SavingsAccount(2000)
d2 = DebitAccount(4000)


