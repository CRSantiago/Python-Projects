class Bank_Account():

  def __init__(self,owner,balance):
    self.owner = owner
    self.balance = balance

  def deposit(self,amount):
    self.balance += amount
    print("Deposit Accepted")

  def withdraw(self,amount):
    if amount <= self.balance:
      self.balance -= amount
      print("Withdraw Accepted")
    else:
      print("Funds Unavailable")

  def __str__(self):
    return "Owner: {} \nBalance: ${} \n".format(self.owner,self.balance)