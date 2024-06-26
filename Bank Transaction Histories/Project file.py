class Txn:
  def __init__(self, amt, txn_type):        #Self is used to access and manipulate the variables and methods within a class
      self.amt = amt
      self.txn_type = txn_type 

  def __repr__(self):
      return f"{self.txn_type.title()}: ${self.amt:.2f}"        # f string formatted string literals #Title to make 1st letter uppercase

class AccountHolder:            #adding holders
  def __init__(self, name, initial_bal=0.0):
      self.name = name
      self.bal = initial_bal
      self.txns = []

  def credit(self, amt):        #Credit
      self.bal += amt           #Adding
      self.txns.append(Txn(amt, 'credit'))          #Adding at the back
      print(f"Credited ${amt:.2f} to {self.name}'s account. New balance: ${self.bal:.2f}")          #The way displays

  def debit(self, amt):         #Debit
      if amt > self.bal:        #demo for insufficient
          print(f"Insufficient funds for {self.name}. Transaction aborted.")
      else:
          self.bal -= amt 
          self.txns.append(Txn(amt, 'debit'))
          print(f"Debited ${amt:.2f} from {self.name}'s account. New balance: ${self.bal:.2f}")

  def display_txns(self):       #Maimtain  BAlance
      print(f"\nTransaction history for {self.name}:")
      for txn in self.txns:
          print(txn)
      print(f"Current balance: ${self.bal:.2f}")
if __name__ == "__main__":
  p1 = AccountHolder(input("Enter Cust 1 name:"))
  p2 = AccountHolder(input("Enter Cust 2 name:"))

  p1.credit(float(input(f"Enter {p1.name} credit:")))
  p1.debit(float(input(f"Enter {p1.name} Debit:")))  
  p2.debit(float(input(f"Enter {p2.name} Debit:"))) #Demo unit for insufficient display
  p2.credit(float(input(f"Enter {p2.name} Credit:")))
  p2.debit(float(input(f"Enter {p2.name} Debit:")))

#Display
  p1.display_txns()
  p2.display_txns()
  
       #return f"{self.txn_type.title()}: ${self.amt:.2f}" 
       #return "{}: ${:.2f}".format(self.txn_type.title(), self.amt)